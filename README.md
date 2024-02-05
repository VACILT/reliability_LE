<!--- 
 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8234027.svg)](https://doi.org/10.5281/zenodo.8234027)
 [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-369/)
--> 





[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8234027.svg)](https://doi.org/10.5281/zenodo.8234027)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Large ensemble assessment of Arctic SPV
**[A. Kuchar](https://github.com/kuchaale), [M. Öhlert](https://github.com/maoehlert), R. Eichinger, [Ch. Jacobi](https://github.com/christophjacobi)**

In review in [WCD](https://egusphere.copernicus.org/preprints/2023/egusphere-2023-1831/).

Code used to process and visualise the model and other data outputs in order to reproduce figures in the manuscript.
Model data are available via  the Multi-Model Large Ensemble Archive
(MMLEA) provided by the US CLIVAR (Climate and Ocean - Variability, Predictability, and Change) working group on large
ensembles ([Deser et al., 2020](https://www.nature.com/articles/s41558-020-0731-2)) as well as ensembles from the Coupled Model Intercomparison Project 6 (CMIP6; [Eyring et al.,
2016](https://gmd.copernicus.org/articles/9/1937/2016/)). 

All datasets already preprocessed can be found [here](https://data.mendeley.com/datasets/d6yg8ncppg/1).

Notebooks for each individual figure as well as for two data tables are in the [`code/` directory](code), while the figures themselves are in the [`plots/` directory](plots).


### Figures
|  #  | Figure                                                                                                                                                                                                    | Notebook / Script                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [Geopotential height climatology at 10 hPa](plots/gh10_model_climatology_comparison.pdf) | [gh10_visualization.ipynb](code/gh10_visualization.ipynb) | |
|  2 | [ROC for displacements and splits in CanESM5](plots/ROC_example_CanESM5.pdf) | [ROC_values.ipynb](code/ROC_values.ipynb) |  |
|  3 | [Rank histograms of aspect ratio at 10 hPa](plots/aspect_ratio_10hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |
|  4 | [Rank histograms of centroid latitude at 10 hPa](plots/centroid_latitude_10hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |
|  5 | [Rank histograms of centroid longitude at 10 hPa](plots/centroid_longitude_10hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |
|  6 | [Rank histograms of kurtosis at 10 hPa](plots/kurtosis_10hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |
|  7 | [Rank histograms of objective area at 10 hPa](plots/objective_area_10hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |
|  8 | [AOC for displacement and split events](plots/areas_displacement_split_new.pdf) | [roc_diagrams.py](code/roc_diagrams.py) |  |
|  9 | [Scatter plots of modal centroid latitude and frequency of displacement SSWs, and modal aspect ratio and frequency of split SSWs](plots/both_frequency_vs_mode_with-compl-MPI-ESM-LR2-final.pdf) | [SSW_frequency_vs_mode_Hallet2021_MPI-ESMs-final.ipynb](code/SSW_frequency_vs_mode_Hallet2021_MPI-ESMs-final.ipynb) | [ERA5_SSW.ipynb](code/ERA5_SSW.ipynb) | 



#### Tables
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [Analyzed climate model ensembles from CMIP5 and CMIP6](tables/models.tex)                                               |               | |\
|  S1 | [Summary table including metrics: bias, spread and AOC](tables/table.tex)                                               |    [ROC_values.ipynb](code/ROC_values.ipynb)           | [rank_histograms.py](code/rank_histograms.py) |\
| S2  | [List of SSWs in ERA5](tables/SSWs_ERA5.tex)                                               |      [ERA5_SSWs_export_latex.ipynb](code/ERA5_SSWs_export_latex.ipynb)         | [ERA5_SSW.ipynb](code/ERA5_SSW.ipynb), [get_ERA5_moments-netcdf.ipynb](code/get_ERA5_moments-netcdf.ipynb) |

#### Supplementary figures
|  #  | Figure                                                                                                                                                                                                    | Notebook / Script                                                                             | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  S1 | [ROC curves for displacement events](plots/ROCs_displacements.pdf) | [roc_diagrams_plots.py](code/roc_diagrams_plots.py) | [rank_histograms.py](code/rank_histograms.py) |    
|  S2 | [ROC curves for split events](plots/ROCs_splits.pdf) | [roc_diagrams_plots.py](code/roc_diagrams_plots.py) | [rank_histograms.py](code/rank_histograms.py) | 
|  S3 | [Rank histograms of aspect ratio at 50 hPa](plots/aspect_ratio_50hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |    
|  S4 | [Rank histograms of centroid latitude at 50 hPa](plots/centroid_latitude_50hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) | 
|  S5 | [Rank histograms of centroid longitude at 50 hPa](plots/centroid_longitude_50hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |   
|  S6 | [Rank histograms of kurtosis at 50 hPa](plots/kurtosis_50hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |   
|  S7 | [Rank histograms of objective area at 50 hPa](plots/objective_area_50hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |   
|  S8 | [Rank histograms of aspect ratio at 100 hPa](plots/aspect_ratio_100hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |    
|  S9 | [Rank histograms of centroid latitude at 100 hPa](plots/centroid_latitude_100hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) | 
|  S10 | [Rank histograms of centroid longitude at 100 hPa](plots/centroid_longitude_100hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |   
|  S11 | [Rank histograms of kurtosis at 100 hPa](plots/kurtosis_100hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) |   
|  S12 | [Rank histograms of objective area at 100 hPa](plots/objective_area_100hPa.pdf) | [summary_plots.py](code/summary_plots.py) | [rank_histograms.py](code/rank_histograms.py), [rank_frequency_test.py](code/rank_frequency_test.py), [bias_spread.py](code/bias_spread.py) | 
