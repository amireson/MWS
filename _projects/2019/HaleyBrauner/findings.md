---
---

[home](home.html)

# 5. Summary of findings

The project was completed in three phases; Phase 1 consisted of Scenario 1 and 2 which replicated the methodology of the MESH modelling in the White Gull Creek watershed (Mkandla, 2017), Phase 2 consisted of Scenario 3, which added complexity by increasing the number of grids in the basin from 1 to 5, and Phase 3, which repeated the calibration of Scenarios 1 and 2 but used the PDMROF runoff algorithm instead of WATROF. A summary of the main findings from the project are discussed below.

Overall, the model performance was very poor for all scenarios, with a maximum optimal Nash-Sutcliffe Efficiency (NSE) value of 0.169 for Scenario 1-P, and minimum optimal NSE value of -0.082. However, meaningful obervations can still be made, and there is hope that with a little more work on the model and a few small, key tweaks, that performance could be substantially improved. 

In Phase 1, comparing the Baker Creek project to the White Gull Creek project, the relationship between model complexity and NSE value, as well as between model complexity and run time, was consistent in both projects. In both models, parameterizing the model using 1 GRU for each landcover type resulted in better NSE values but longer run times compared to using only 1 GRU for the whole basin. Additionally, the more complex configurations resulted in improved identifiability, although Mkandla (2017) found that there was some degradation in the most complex configration compared to the intermediary ones (which weren't replicated in Baker Creek). Both projects also found that calibration NSE does not give an indication of how well the model will perform during validation, and found that the NSE values were consistently higher during calibration than validation.

In Phase 2, there was some improvement in model performance of Scenario 3 in terms of NSE compared to Scenarios 1 and 2. However, the increase in NSE value of 0.024 came at a high computational cost of an additional 25.8 hours per trial, or 262% longer than Scenario 2. That said, were the NSE results better, there may be some applications where the cost is worth the improvement in performance.

In Phase 3, the main findings were that PDMROF performed better than WATROF, but took slightly longer to run (2.3 hours and 2.5 hours longer for Scenarios 1-P and 2-P, respectively). Given the hydrological characteristics of the Baker Creek Basin - the large number of lakes and dominance of large lakes along the main drainage path- this outcome is consistent with what was expected.  

In general, calibrating to streamflow and using NSE as the objective parameter was not ideal given the low runoff ratios in the basin (Spence & Hedstrom, 2018). Additonally, calibrating streamflow to both a wetter-than-normal and drier-than-normal period pushed the limits of MESH's capabilities. The effect of the contrasting conditions during calibration and the use of the NSE was apparent in the underestimation of the majority of low-flow periods and overestimations of low flows - particularly during the spring peaks. All model scenarios also struggled to adequately represent the fall peaks / winter streamflow, with Scenario 1 doing the worst and Scenario 2-P doing the best.

