#rank frequency analysis, see Suarrez-Gutierrez 2021
import rank_histograms as rh
import xskillscore as xs
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import bias_spread as bs
from scipy.stats import chisquare

def freq_test(ds,var,lvl):
    nmem=len(ds['member'])
    freq_stats=np.empty((nmem,nmem+1))
    for mem in range(nmem):
        observations=ds.isel(member=mem)
        rank_stats=rh.get_rank_stats(observations,ds,var,'1979-01-01','2014-31-12',lvl,'time','member')
        freq_stats[mem,:]=rank_stats
    perc5=np.percentile(freq_stats[:,:],5,axis=0)*nmem/(nmem+1)
    perc95=np.percentile(freq_stats[:,:],95,axis=0)*nmem/(nmem+1)
    return perc5,perc95


if __name__=='__main__':
    era_reanalysis=rh.get_dataset(rh.path_to_data+'ERA5_moments@10and50and100hPa_NHonly.nc')
    vars=list(era_reanalysis.keys())
    for model in rh.file_name:
        forecast=rh.get_dataset(rh.path_to_data+rh.file_name[model])
        #make sure member dimension has the right name
        if 'member_id' in list(forecast.dims):
            forecast=forecast.rename(name_dict={'member_id':'member'})
        #plot and save rank histogram for every variable and pressure level
        for n in range(len(forecast['plev'])):
            plev=float(forecast['plev'][n])
            for var in vars[:]:
                rank_hist=rh.get_rank_stats(era_reanalysis,forecast,
                                    var,'1979-01-01','2014-12-31',forecast['plev'][n],dim='time',member_dim='member')
                plt.step(rank_hist['rank'],rank_hist,'r',where='mid')
                expected=np.empty(len(rank_hist))
                expected[:]=np.sum(rank_hist)/len(rank_hist)
                plt.step(rank_hist['rank'],expected,'b',where='mid')
                #plot 5th and 95th percentiles from rank frequency test
                perc5,perc95=freq_test(forecast,var=var,lvl=plev)
                perc5[0],perc5[-1]=np.NaN,np.NaN
                perc95[0],perc95[-1]=np.NaN,np.NaN
                plt.plot(rank_hist['rank'],perc5,c='grey',ls='--')
                plt.plot(rank_hist['rank'],perc95,c='grey',ls='--')
                plt.xlim([1,len(rank_hist)])
                plt.ylim(bottom=0)
                #calculate statistics and add them to the plot
                bias=bs.bias(rank_hist)
                spread=bs.spread(rank_hist)
                chisq,pval=chisquare(rank_hist)
                ax=plt.gca()
                plt.text(0.1,0.1,'Bias: {bias:.3f}'.format(bias=bias),transform=ax.transAxes)
                plt.text(0.4,0.1,'Spread: {spread:.3f}'.format(spread=spread),transform=ax.transAxes)
                plt.text(0.7,0.1,'pvalue: '+rh.round_format(pval),transform=ax.transAxes)
                title='Rank histogram '+model+' '+var+' {plev:.0f}hPa'.format(plev=plev/100)
                plt.title(title)
                #save histogram
                plt.savefig('../figures/rank_frequency_test/'+model+'_'+var+'_{plev:.0f}hPa.png'.format(plev=plev/100))
                plt.close()
                print(model,var,('{plev:.0f}hPa'.format(plev=plev/100)))

    
