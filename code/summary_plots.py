#program plots all rank histograms for one level and variable in the same plot
import rank_histograms as rh
import bias_spread as bs
import rank_frequency_test as rft
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare

medium_size=7
large_size=10
plt.rc('lines', linewidth=0.6) 
plt.rc('xtick', labelsize=medium_size)    # fontsize of the tick labels
plt.rc('ytick', labelsize=medium_size)    # fontsize of the tick labels
    
era_reanalysis=rh.get_dataset(rh.path_to_data+'ERA5_moments@10and50and100hPa_NHonly.nc')
variables=list(era_reanalysis.keys())
lvls=list(era_reanalysis['plev'])

for lvl in lvls[:]:       
    for var in variables[:]:
        plt.figure(dpi=480, figsize=(5,7))   
        if '_' in var:
            var_for_title=var.split('_')[0]+' '+var.split('_')[1]
        else:
            var_for_title=var
            if var_for_title=='angle':
                var_for_title='vortex angle'
        plt.suptitle(var_for_title+' {plev:.0f}hPa'.format(plev=float(lvl)/100),fontsize=16)
        n=0
        axs=[]
        for model in rh.file_name:
            forecast=rh.get_dataset(rh.path_to_data+rh.file_name[model])
            #check if level is available for the model and add subplot 
            if any(forecast['plev'].isin(float(lvl))):
                axs.append(plt.subplot(6,2,n+1))

               
                rank_hist=rh.get_rank_stats(era_reanalysis,forecast,var,'1979-01-01','2014-12-31',
                                            float(lvl),dim='time',member_dim='member')
                axs[n].bar(rank_hist['rank'],rank_hist,color='lightblue')
                expected=np.empty(len(rank_hist))
                expected[:]=np.mean(rank_hist)
                axs[n].plot(rank_hist['rank'],expected,color='black',ls='--')
                #plot 5th and 95th percentiles from rank frequency test
                perc5,perc95=rft.freq_test(forecast,var=var,lvl=lvl)
                perc5[0],perc5[-1]=np.NaN,np.NaN
                perc95[0],perc95[-1]=np.NaN,np.NaN
                axs[n].plot(rank_hist['rank'],perc5,c='grey',ls='--')
                axs[n].plot(rank_hist['rank'],perc95,c='grey',ls='--')
                axs[n].set_ylim(bottom=0)
                axs[n].set_xlim([0.5,len(rank_hist)+0.5])
                #calculate statistics and add them to plot
                bias=bs.bias(rank_hist)
                spread=bs.spread(rank_hist)
                chisq,pval=chisquare(rank_hist)
                axs[n].set_title('{title}\n'.format(title=model)+
                     '$\chi^2$: {chi2:.2f} '.format(chi2=chisq) +
                     '\n Bias: {bias:.2f}  '.format(bias=bias) +
                     'Spread: {spread:.2f}'.format(spread=spread),fontsize=7)
                print(model,var,'{plev:.0f}hPa'.format(plev=float(lvl)/100))
                n+=1
        plt.tight_layout()
        plt.savefig('../figures/summary_plots/'+var+'_{plev:.0f}hPa'.format(plev=float(lvl)/100)+'.png')
        plt.close()

