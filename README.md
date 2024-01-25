# Give-Me-Some-Credit

## Problem
Predicting the probability that somebody will experience financial distress in the next two years.

## Objective
Build a delinquency prediction model that lenders can use to help make the best financial decisions.

## Dataset
The GiveMeSomeCredit Kaggle dataset contains the delinquency data and some relevant features of 150000 borrowers. The target column to predict is the SeriousDlqin2yrs column which indicates **whether the person experienced 90 days past due delinquency or worse in the last 2 years.**

- Predictors available
  - RevolvingUtilizationOfUnsecuredLines
  - age
  - DebtRatio
  - MonthlyIncome
  - NumberOfOpenCreditLinesAndLoans
  - NumberRealEstateLoansOrLines
  - NumberOfDependents
  - NumberOfTime30-59DaysPastDueNotWorse
  - NumberOfTime60-89DaysPastDueNotWorse
  - NumberOfTimes90DaysLate
 
## Observation
- Null Rates
  - **MonthlyIncome** and its derived features (**MonthlyIncomePerDependent, MonthlyIncomePerCreditLine**) have a null rate of about **19.8%**
  - **NumberOfDependents** has a null rate of about **2.6%**
  - Other features have a null rate of **0%** (completely filled)

- Insights
  - All the predictor columns are **numerical** and **continuous**.
  - The minimum age of the people is **21** (ignoring entries with age 0).
  - Delinquency rates show an **increasing** trend with increase in **DPDs**, **credit utilisation**, **number of dependents** and **number of real estate loans** for the major part.
  - Delinquency reduces slightly as income increases
  - Delinquency increases with the number of dependents
  - The number of loan products doesn't seem to affect delinquency and neither does debt ratio
  - Delinquency decreases slightly with age
  - The number of real estate loans doesn't seem to affect delinquency
  - Delinquency increases with an increase in unsecured loan utilization
  - DPD columns are very highly correlated
  - The number of open credit lines and loans is correlated to some extent with the number of real estate loans and credit lines
  - The rest of the variables don't show significant correlations
  - Delinquency rates show a **decreasing** trend with an increase in **age** and **monthly income** and its derived features for the major part.
  - All the DPD columns are highly inter-correlated. Hence, only the one with the highest predictive power (**NumberOfTimeGreaterThan30DPD**) is used as a feature.
  - The MonthltIncomePerDependent column has a lower predictive value than the original features used in its creation. Hence, it is not used as a feature.
  - **Credit utilisation** has the greatest predictive value (with a roc-auc score of **77.8%**).

## Conclusion
- The best model has a train and test roc-auc score of **87.44%** and **86.65%** respectively.
- The model has very good risk segmentation as the average delinquency rate is less than **3%** for people in the **first** **7 deciles**, which monotonically increases to a number greater than **30%** in the **last decile**.
- Looking at the feature importances, we can conclude that any DPD greater than 30 and high credit utilisation are good predictors of delinquency.
