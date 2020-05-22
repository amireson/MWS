---
---

[home](home.html)

# 6. Towards a solution

Overall, the MESH model performance was very poor for all the scenarios. That said, there were valuable trends and comparisons observed. Future recommendations for further research to improve understanding and outcome of the model are as follows:

- Explore the effect of calibrating to logNSE instead of NSE.
    - Given the prevalence of low flows in the basin, this would likely improve the overall NSE value.
- Revisit the parameters and consider modifying some of the values and/or expanding the parameter ranges to see if better results can be obtained. This may include swapping out which parameters were calibrated.
    - Concurrently, it would be a good idea to perform a sensitivity analysis to hone in on the most sensitive parameters. This may result in a reduction of the number of calibrations required, and thus allow for more calibration iterations in the same run time. Examples of calibration tools include VisId (Gábor, Villaverde, & Banga, 2017) and VARS (Razavi & Gupta, 2016).
- Improve the parameterization of soils in Scenario 1 to better represent an "effective" soil type for the entire basin.
- Consider adding a reservoir(s) to represent the behavior of the large lakes in the basin (see Yassin et al., 2019).
- Consider using the LATFLOW as another alternative to represent the fill-spill behavior of the basin (see Hosain, 2017).
- Since streamflow is such a small part of the water balance in this basin - especially during dry years - consider calibrating to a differnt metric, such as evaporation and/or snow depth since both are available for the basin for several years. 
- Calibrate just to the spring peaks, just the fall peaks, and/or only the higher flow period. This may result in better performance, but may also provide more information on the key parameters for each of those dominant behaviors.
- Iteratively run the spin-up period to initialize the model (particularly the soil moisture and thermal properties) rather than only 1 year. The initial conditions were chosen based on the average soil moisutre and temperature measurements over a number of years, which may not have been representative of the conditions at the start of the modelling period. This may be particularly important due to the discontinuous permafrost in the area and the lack of deeper soil temperature measurements. 
- Define GRUs by hydrological response in the watershed rather than by landcover type, since the same landcover in different areas of the basin can respond differently.
- Improve the parameterization of bedrock in the model, either explicitly or effectively.
