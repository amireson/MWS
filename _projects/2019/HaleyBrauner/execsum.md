---
---

[home](home.html)

# Executive Summary

The purpose of this project was to compare performance of various representations of spatial heterogeneity in the Baker Creek Watershed (NWT) using the MESH model, building on the work of former Master's of Water Security student, H. Mkandla (2017, University of Saskatchewan). The heterogeneous and variable nature of the earth continues to be a challenge to represent in hydrological models (Haghnegahdar, Tolson, Craig, & Paya, 2015). Therefore, it is important to choose a model configuration(s) that will give the best results within the limititations of observations, time, and computational efficiency.

The project was completed in 3 phases:

1. Replicate the methodology used in the White Gull Creek basin in order to compare the results (Scenario 1 and 2);
2. Increase the complexity of the model by increasing the number of grid cells in the basin (Scenario 3); and
3. Repeat the scenarios 1 and 2 using the PDMROF runoff algorithm (Scenario 1-P and 2-P).

The Baker Creek Watershed is located in the Northwest Territories of Canada near the capital city of Yellowknife in a subarctic climate and zone of discontinuous permafrost. The basin is approximately 155 km^2^ and receives 289 mm of precipitation annually, 41% of which as snowfall (Environment and Climate Change Canada, 2019a). The landcover in the basin is primarily bedrock, lakes, and coniferous forest hillslopes   (Spence & Hedstrom, 2018). The hydrology of the site is dominated by large lakes connected by short streams with a complex runoff regime due to a highly variable contributing area that depends on a number of factors.

Driving data for the model was sourced from three main sources and combined into one continuous set for the modelling period. Streamflow observations from the Water Survey of Canada station 07SB013 - Baker Creek at the Outlet of Lower Martin Lake - were used to calibrate and validate the model (Water Survey of Canada, 2019).

The modelling period was 2006-2016, and each scenario was calibrated for 3 years during a wetter-than-normal period and 2 years during a drier-than-normal period with a 1 year spin-up period; the remaining years were used for model validation. A calibration program called OSTRICH (Matott, 2017) was used to run 1000 iterations per trial for 100 trials using the Nash-Sutcliffe Efficiency (NSE) as the objective parameter (Nash & Sutcliffe, 1970)

All the NSE results from the Baker Creek calibration were much lower than those for White Gull Creek and barely better than the no-model case. Regardless, the trends observed between the calibration and validation periods, and between scenarios, provided useful information about the behavior of the MESH model in the watershed and clues for future improvements to the model setup.

The results of the modelling showed that performance (NSE) improved with increasing complexity, but so did the average run time per trial, and performance during calibration was consistently better than validation with the exception of Scenario 1-P. Using the PDMROF runoff algorithm showed improved performance versus the WATROF algorithm. The model consistently underestimated large spring peakflows and overestimated low spring peakflows; it also either highly underestimated or completely missed fall peakflows.

Going forward, it is recommended that a sensitivity analysis be conducted and key parameters adjusted to improve the model performance. It is also recommended to test a configuration where the Grouped Response Units (GRUs) are defined by hydrological function and location in the watershed rather than by landcover type.

