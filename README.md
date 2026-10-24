# Retail_Sales-Robustness-Experiment-Project

## Project Overview

This exploratory‑machine‑learning mini‑project investigates how a standard Random Forest regression model responds to real‑world data‑quality issues, focusing especially on extreme‑value outliers and missing‑value patterns in retail‑transaction data. The work supports the broader research theme: developing explainable, robust predictive‑analytics workflows for imperfect operational datasets. It uses the public UCI Online Retail dataset rather than the earlier Superstore‑based analysis, offering a second practical case‑study for my portfolio.
 
## Dataset Details

‑ Source: UCI Machine‑Learning Repository Online Retail Dataset
‑ Scope: 546 501 retail‑transaction records including InvoiceNo, Quantity, UnitPrice, Country and other transaction fields
‑ Identified data‑quality features:
  ‑ 4 592 rows with missing UnitPrice entries
  ‑ 2 rows containing very large‑negative UnitPrice values (−11 062.06), representing unusual high‑magnitude product‑return records
 
## Tools & Libraries Used

‑ Python (VS Code development environment)
‑ pandas ‑ data loading, filtering, missing‑value inspection, cleaning
‑ scikit‑learn ‑ Random Forest regressor, train‑test splitting, RMSE evaluation
‑ matplotlib ‑ RMSE‑comparison bar‑chart visualisation
‑ Excel ‑ initial quick preview of source‑data structure
 
## Experimental Workflow

1. Load dataset with correct  latin‑1  encoding; inspect basic dimensions
2. Count missing UnitPrice values; identify negative‑price outlier rows
3. Create two dataset variants:
  ‑ Original: keeps all rows including the two extreme‑negative‑price entries
  ‑ Correct‑cleaned: only removes the two explicit‑negative‑price rows, retains missing‑UnitPrice records
4. Compute TotalPrice = Quantity × UnitPrice as the prediction‑target variable
5. Train identical‑setup Random Forest regressors (n_estimators = 50, random_state = 42) on both datasets
6. Compare test‑set RMSE scores; plot comparison chart
7. Export cleaned‑data file, comparison‑chart image and textual‑summary record
 
## Key Results

‑ Model on correct‑cleaned dataset (2 outliers removed): Test‑set RMSE = 123.96
‑ Model on original dataset (includes 2 extreme‑value rows): Test‑set RMSE = 403.80
‑ Visual output:  rmse_comparison.png  ‑ bar‑chart showing large error difference between runs
‑ Main finding: Even only two extreme‑price outlier records substantially increased prediction error; this baseline Random Forest implementation proved sensitive to such rare extreme‑value cases, highlighting a real‑world robustness challenge.
 
## Repository Contents

‑  data.py  ‑ full Python‑analysis script
‑  data.csv  ‑ original UCI Online Retail source file
‑  data_cleaned_correct.csv  ‑ prepared dataset (only negative‑price rows dropped)
‑  rmse_comparison.png  ‑ RMSE‑comparison bar‑chart
‑  robustness_summary.txt  ‑ short textual record of main experimental‑result values
 
## Future Possible Extensions

‑ Test outlier‑detection algorithms to flag extreme values automatically
‑ Try robust‑regression models less affected by outliers
‑ Evaluate effects of different missing‑value‑handling strategies (removal, imputation) on prediction‑stability

## Prepared by: Shumaila

Mini‑Project for Data‑Analytics & Robust‑Machine‑Learning Portfolio
