<!--- [![DOI](https://zenodo.org/badge/382086874.svg)](https://zenodo.org/badge/latestdoi/382086874)
 [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-369/)
--> 

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# On the reliability of large ensembles simulating the Northern Hemispheric winter stratospheric polar vortex
**[M. Öhlert](https://github.com/maoehlert), [A. Kuchar](https://github.com/kuchaale), R. Eichinger, [Ch. Jacobi](https://github.com/christophjacobi)**

Submitted to [?](?).

Code used to process and visualise the model and other data outputs in order to reproduce figures in the manuscript.
Model data are available via  the Multi-Model Large Ensemble Archive
(MMLEA) provided by the US CLIVAR (Climate and Ocean - Variability, Predictability, and Change) working group on large
ensembles ([Deser et al., 2020](https://www.nature.com/articles/s41558-020-0731-2)) as well as ensembles from the Coupled Model Intercomparison Project 6 (CMIP6; [Eyring et al.,
2016](https://gmd.copernicus.org/articles/9/1937/2016/)). All datasets already preprocessed can be found [here]([https://data.mendeley.com/datasets/?).

Notebooks for each individual figure as well as for two data tables are in the [`code/` directory](code), while the figures themselves are in the [`plots/` directory](plots).


### Figures
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [Rank histograms of aspect ratio at 10 hPa](plots/aspect_ratio_10hPa.png) | [rank_histograms.py](code/rank_histograms.py) |
|  2 | [Rank histograms of centroid latitude at 10 hPa](plots/centroid_latitude_10hPa.png}) | [rank_histograms.py](code/rank_histograms.py) |
|  3 | [Rank histograms of centroid longitude at 10 hPa](plots/centroid_longitude_10hPa.png) | [rank_histograms.py](code/rank_histograms.py) |
|  4 | [Rank histograms of kurtosis at 10 hPa](plots/kurtosis_10hPa.png) | [rank_histograms.py](code/rank_histograms.py) |
|  5 | [Rank histograms of objective area at 10 hPa](plots/objective_area_10hPa.png) | [rank_histograms.py](code/rank_histograms.py) |
|  6 | [AOC for displacement and split events](plots/areas_displacement_split.png) | [roc_diagrams.py](code/roc_diagrams.py) |


#### Tables
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [Analyzed climate model ensembles from CMIP5 and CMIP6](tables/models.tex)                                               |               | |

#### Supplementary figures
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  S1 | [?](plots/?)                                               | [?](code/?)                     | |
