import rank_histograms as rh
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import xskillscore as xs
import numpy as np
from string import ascii_lowercase, ascii_uppercase

def plot_roc(roc,model,event_type='split'):
    false_positive=roc.sel(metric='false positive rate')
    true_positive=roc.sel(metric='true positive rate')
    #roc.to_dataset(dim='metric').plot.line(y='true positive rate', x='false positive rate')
    #roc.to_dataset(dim='metric').plot.plot(y='true positive rate', x='false positive rate')
    plt.plot(false_positive, true_positive,'o-')
    plt.xlabel('false positive rate')
    plt.ylabel('true positive rate')
    area=roc.sel(metric='area under curve').values[0]
    plt.plot([0, 1], [0, 1], 'k:')
    #ax.text(0.5,1.08,'ROC curve '+event_type+' events '+model,fontsize=12,ha='center',transform=ax.transAxes)
    plt.text(0.5,1.12,'Area under curve: '+str(round(area,3)),ha='center')#,transform=ax.transAxes)
    plt.title('')

#estimate uncertainty with perfect model range
def freq_test(ds,threshold,lower=True):
    nmem=len(ds['member'])
    freq_stats=np.empty((nmem))
    for mem in range(nmem):
        observations=ds.isel(member=mem)
        if lower:
            roc_areas=roc=xs.roc(observations<threshold, (ds<threshold).mean('member'),
                   return_results='all_as_metric_dim')
        if not lower:
            roc_areas=roc=xs.roc(observations>threshold, (ds>threshold).mean('member'),
                   return_results='all_as_metric_dim')    
        area=roc.sel(metric='area under curve').values[0]
        freq_stats[mem]=area
    mean=np.mean(freq_stats[:])
    perc5=np.percentile(freq_stats[:]-mean,5)
    perc95=np.percentile(freq_stats[:]-mean,95)
    return perc5,perc95


obs=rh.get_dataset(rh.path_to_data+'ERA5_moments@10and50and100hPa_NHonly.nc')
obs_cl=obs['centroid_latitude'].loc['1979-01-01':'2014-12-28',1e3]
obs_ar=obs['aspect_ratio'].loc['1979-01-01':'2014-12-28',1e3]

area_displacements=[]
area_splits=[]
models=[]
for model in rh.file_name:
    forecast=rh.get_dataset(rh.path_to_data+rh.file_name[model])
    #define bin edges
    #edges=np.arange(0,1.02,0.02)
    if any(forecast['plev'].isin(1e3)):
        #roc curve for displacement
        forecast_cl=forecast['centroid_latitude'].loc[:,'1979-01-01':'2014-12-28',1e3]
        roc=xs.roc(obs_cl<66, (forecast_cl<66).mean('member'),return_results='all_as_metric_dim') #thresholds as in Seviour et al. 2013
        area=roc.sel(metric='area under curve').values[0]
        #use rank frequency test to produce error bars
        err_5,err_95=freq_test(forecast_cl,threshold=66,lower=True)
        area_displacements.append('{model}&{area:.3f}&{perc5:.3f}&{perc95:.3f}'.format(
            model=model,area=area,perc5=err_5,perc95=err_95))
        plt.rcParams.update({'font.size': 18})

        plot_roc(roc,model,event_type='displacement')
        # roc.to_dataset(dim='metric').plot.scatter(y='true positive rate', x='false positive rate')
        #plt.plot([0, 1], [0, 1], 'k:')
        #plt.title('ROC curve displacement events '+model)
        plt.savefig('../plots/displacement_'+model+'.pdf', bbox_inches = 'tight')
        plt.close()
        print('displacement',model)

        #roc curve for split
        forecast_ar=forecast['aspect_ratio'].loc[:,'1979-01-01':'2014-12-28',1e3]
        roc=xs.roc(obs_ar>2.4, (forecast_ar>2.4).mean('member'),return_results='all_as_metric_dim')
        area=roc.sel(metric='area under curve').values[0]
        err_5,err_95=freq_test(forecast_ar,threshold=2.4,lower=False)
        area_splits.append('{model}&{area:.3f}&{perc5:.3f}&{perc95:.3f}'.format(
            model=model,area=area,perc5=err_5,perc95=err_95))
        plot_roc(roc,model)
        #plt.plot([0,1], [0, 1], 'k:')
        #plt.title('ROC curver ')
        plt.savefig('../plots/split_'+model+'.pdf', bbox_inches = 'tight')
        plt.close()
        models.append(model)
        print('split',model)
"""
models=[]
area_displacements=[]
err_locs_disp=[]
with open('roc_displacement_new2.txt','r') as f:
    lines=f.readlines()
    for line in lines:
        line=line.split('&')
        models.append(line[0])
        area_displacements.append(float(line[1]))
        err_locs_disp.append([abs(float(line[2])),abs(float(line[3]))])
        
print(err_locs_disp)
ind=np.arange(len(models))
width=0.5


fig, axs=plt.subplots(1,2,sharey=True,figsize=(8,4.5))
#plt.suptitle('ROC area under curve')

for i in ind:
    axs[0].bar(i,area_displacements[i],width,color='lightblue',edgecolor='black')
    axs[0].errorbar(i,area_displacements[i],yerr=[[err_locs_disp[i][0]],[err_locs_disp[i][1]]],
                    ecolor='black',capsize=3,fmt='none')

axs[0].xaxis.set_major_locator(FixedLocator(ind))
axs[0].set_xticklabels(models,rotation=75)
axs[0].axhline(0.5,color='grey',linestyle='--')
axs[0].axvline(2.5,color='black',linestyle='-')
axs[0].set_ylabel('ROC area under curve')
axs[0].set_title('Displacement events')
axs[0].text(0.05, 1.1, ascii_uppercase[0], transform=axs[0].transAxes,
                      fontsize=7, fontweight='bold', va='top', bbox={'alpha': 0.7, 'facecolor': 'white'})
#plt.savefig('../figures/areas_displacement.png')
#plt.close()

area_splits=[]
err_locs_splits=[]
with open('roc_split_new2.txt','r') as f:
    lines=f.readlines()
    for line in lines:
        line=line.split('&')
        area_splits.append(float(line[1]))
        err_locs_splits.append([abs(float(line[2])),abs(float(line[3]))])
        
for i in ind:
    axs[1].bar(i,float(area_splits[i]),width,color='lightblue',edgecolor='black')
    axs[1].errorbar(i,area_splits[i],yerr=[[err_locs_splits[i][0]],[err_locs_splits[i][1]]],
                    ecolor='black',capsize=3,fmt='none')

axs[1].xaxis.set_major_locator(FixedLocator(ind))
axs[1].set_xticklabels(models, rotation=75)
axs[1].axhline(0.5,color='grey',linestyle='--')
axs[1].axvline(2.5,color='black',linestyle='-')
#axs[1].set_ylabel('Area under curve')
axs[1].set_title('Split events')
axs[1].text(0.05, 1.1, ascii_uppercase[1], transform=axs[1].transAxes,
                      fontsize=7, fontweight='bold', va='top', bbox={'alpha': 0.7, 'facecolor': 'white'})

fig.tight_layout()
plt.savefig('../plots/areas_displacement_split_new.pdf', bbox_inches = 'tight')
plt.close()

with open('roc_displacement_new2.txt','w') as f:
    for row in area_displacements:
        f.write(row+'\n')

with open('roc_split_new2.txt','w') as f:
    for row in area_splits:
        f.write(row+'\n')
"""
