#functions to calculate bias and spread for rank histograms
#see Jolliffe and Primo 2008
import numpy as np

def bias(rank_hist_vals): #spot linear trend in rank histogram
    rank_hist_vals=np.array(rank_hist_vals)
    k=len(rank_hist_vals)
    #set values for k even
    if k%2==0:
        half=k/2
        a=-(2*half-1)
        b=2
    #set values for k odd
    if k%2==1:
        half=(k-1)/2
        a=-half
        b=1
    vec=np.empty(k)
    #calculate elements of the vector
    for n in range(k):
        vec[n]=a+n*b
    #normalize vector so it has length 1
    vec=vec/np.sqrt(np.sum(vec**2))
    #calculate x values
    e=np.sum(rank_hist_vals)/k
    x=np.sqrt(e)*(rank_hist_vals-e)/e
    
    u=np.sum(np.multiply(vec,x))
    return u**2

def spread(rank_hist_vals):
    rank_hist_vals=np.array(rank_hist_vals)
    k=len(rank_hist_vals)
    #set values for k even
    if k%2==0:
        half=int(k/2)
        a=(half-1)
        b=2
    #set values for k odd
    if k%2==1:
        half=int((k-1)/2)
        a=half**2
        b=2*half+1
    vec=np.empty(k)
    for n in range(half):
        vec[n]=a-n*b
    if k%2==0:
        vec[half:]=np.flip(vec[:half])
    if k%2==1:
        vec[half]=a-half*b
        vec[half+1:]=np.flip(vec[:half])
    #normalize vector so it has length 1
    vec=vec/np.sqrt(np.sum(vec**2))
    #calculate x values
    e=np.sum(rank_hist_vals)/k
    x=np.sqrt(e)*(rank_hist_vals-e)/e
    
    u=np.sum(np.multiply(vec,x))
    return u**2

def chisquared(rank_hist_vals):
    rank_hist_vals=np.array(rank_hist_vals)
    k=len(rank_hist_vals)
    e=np.sum(rank_hist_vals)/k
    x=np.sqrt(e)*(rank_hist_vals-e)/e
    chisq=np.sum(np.multiply(x,x))
    return chisq
            

    
