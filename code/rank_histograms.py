#program to plot rank histograms 
import xarray as xr
import xskillscore as xs
import matplotlib.pyplot as plt
import bias_spread as bs
import numpy as np
from scipy.stats import chisquare

path_to_data='../data/'

file_name={'CanESM2':'moments_day_CanESM2_historical_rcp85_19500101-21001231.nc',
           'CanESM5': 'CMIP.CCCma.CanESM5.historical.day.gn_moments@10and50and100hPa.nc',
            #'CESM1':'moments_day_CESM_historical_19191201-20051231_new.nc',
            'CESM2':'CESM2-LE-CMIP6_moments@10and50and100hPa_1920-2014_new.nc',
            'CNRM-CM6-1': 'CMIP.CNRM-CERFACS.CNRM-CM6-1.historical.day.gr_moments@10and50and100hPa.nc',
            'INM-CM5-0': 'CMIP.INM.INM-CM5-0.historical.day.gr1_moments@10and50and100hPa.nc',
            'IPSL-CM6A-LR': 'CMIP.IPSL.IPSL-CM6A-LR.historical.day.gr_moments@10and50and100hPa.nc',
            'MIROC6': 'CMIP.MIROC.MIROC6.historical.day.gn_moments@10and50and100hPa.nc',
            'UKESM1-0-LL': 'CMIP.MOHC.UKESM1-0-LL.historical.day.gn_moments@10and50and100hPa.nc',
            'MPI-ESM1-2-HR': 'CMIP.MPI-M.MPI-ESM1-2-HR.historical.day.gn_moments@10and50and100hPa.nc',
            'MPI-ESM1-2-LR': 'CMIP.MPI-M.MPI-ESM1-2-LR.historical.day.gn_moments@10and50and100hPa.nc',
            'GFDL-CM3':'moments_day_GFDL-CM3_historical_rcp85_19200101-21001231.nc'}
    
def get_dataset(path_to_file):
    ds=xr.open_dataset(path_to_file)
    #make sure timestamps of the datasets are equal
    ds['time']=ds['time'].dt.strftime('%Y-%m-%d')
    #ds=ds.where(ds.time.str[5:]!='02-29',drop=True)
    ds=ds.where(ds.time.str[8:]!='29',drop=True)
    ds=ds.where(ds.time.str[8:]!='30',drop=True)
    ds=ds.where(ds.time.str[8:]!='31',drop=True)
    #make sure member dimension has the right name
    if 'member_id' in list(ds.dims):
        ds=ds.rename(name_dict={'member_id':'member'})
    return ds

def get_rank_stats(observations,forecast,var_name,start_date,end_date,
                        lvl,dim='time',member_dim='member'):
    #select variable, time and pressure level
    forecast_var=forecast[var_name].loc[:,start_date:end_date,lvl]
    observations_var=observations[var_name].loc[start_date:end_date,lvl]
    #get values for rank histogram and plot it
    rank_hist=xs.rank_histogram(observations_var,forecast_var,dim,member_dim)
    return rank_hist

#round number to 3 decimal places or return scientific notation if too small
def round_format(num,bound=0.01):
    if abs(num)<bound:
        return '{:.2e}'.format(num)
    else:
        return str(round(num,3))

    
if __name__=='__main__':
    #open observation dataset
    era_reanalysis=get_dataset(path_to_data+'ERA5_moments@10and50and100hPa_NHonly.nc')
    vars=list(era_reanalysis.keys())
    for model in file_name:
        #open forecast dataset and make sure timestamps are equal
        forecast=get_dataset(path_to_data+file_name[model])
        #plot and save rank histogram for every variable and pressure level
        for n in range(len(forecast['plev'])):
            plev=float(forecast['plev'][n])
            for var in vars[:]:
                rank_hist=get_rank_stats(era_reanalysis,forecast,
                                    var,'1979-01-01','2014-12-31',forecast['plev'][n],dim='time',member_dim='member')
                plt.step(rank_hist['rank'],rank_hist,'r',where='mid')
                expected=np.empty(len(rank_hist))
                expected[:]=np.sum(rank_hist)/len(rank_hist)
                plt.step(rank_hist['rank'],expected,'b',where='mid')
                plt.xlim([1,len(rank_hist)])
                plt.ylim(bottom=0)
                #calculate statistics and add them to the plot
                bias=bs.bias(rank_hist)
                spread=bs.spread(rank_hist)
                chisq,pval=chisquare(rank_hist)
                ax=plt.gca()
                plt.text(0.1,0.1,'Bias: {bias:.3f}'.format(bias=bias),transform=ax.transAxes)
                plt.text(0.4,0.1,'Spread: {spread:.3f}'.format(spread=spread),transform=ax.transAxes)
                plt.text(0.7,0.1,'pvalue: '+round_format(pval),transform=ax.transAxes)
                title='Rank histogram '+model+' '+var+' {plev:.0f}hPa'.format(plev=plev/100)
                plt.title(title)
                #save histogram
                plt.savefig('../figures/rank_histograms/'+model+'_'+var+'_{plev:.0f}hPa.png'.format(plev=plev/100))
                plt.close()
                print(model,var,('{plev:.0f}hPa'.format(plev=plev/100)))
    

