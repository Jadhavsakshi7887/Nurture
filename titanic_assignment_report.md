# Titanic Dataset - EDA & Preprocessing Report


## Part 1: Data Understanding & Preprocessing


Columns used: Pclass, Sex, Age, SibSp, Parch, Fare, Emb_C, Emb_Q, Emb_S



### Numeric feature statistics

|        |         mean |    median |     std |
|:-------|-------------:|----------:|--------:|
| Age    |  2.27278e-16 | -0.104637 | 1.00056 |
| Fare   |  3.98733e-18 | -0.357391 | 1.00056 |
| SibSp  |  4.38607e-17 | -0.474545 | 1.00056 |
| Parch  |  5.3829e-17  | -0.473674 | 1.00056 |
| Pclass | -8.77213e-17 |  0.827377 | 1.00056 |


### Outlier info (IQR method)

|      |    lower |    upper |   num_outliers |
|:-----|---------:|---------:|---------------:|
| Age  | -2.06431 | 1.93188  |             66 |
| Fare | -1.1865  | 0.673106 |            116 |


Saved visualizations:

- ./titanic_output/hist_age.png

- ./titanic_output/scatter_age_fare.png

- ./titanic_output/corr_heatmap.png



## Part 3: Model Building


### Baseline performance (before tuning)


**Logistic Regression:**

{'accuracy': 0.8044692737430168, 'precision': 0.7931034482758621, 'recall': 0.6666666666666666, 'f1': 0.7244094488188977, 'confusion_matrix': [[98, 12], [23, 46]]}


**Random Forest:**

{'accuracy': 0.8212290502793296, 'precision': 0.8135593220338984, 'recall': 0.6956521739130435, 'f1': 0.75, 'confusion_matrix': [[99, 11], [21, 48]]}


## Part 4: Optimization (GridSearchCV)


Best params: {'max_depth': None, 'min_samples_split': 4, 'n_estimators': 50}


Performance after tuning:

{'accuracy': 0.8100558659217877, 'precision': 0.7868852459016393, 'recall': 0.6956521739130435, 'f1': 0.7384615384615385, 'confusion_matrix': [[97, 13], [21, 48]]}


Improvements (Random Forest):

{'accuracy_before': 0.8212290502793296, 'accuracy_after': 0.8100558659217877, 'f1_before': 0.75, 'f1_after': 0.7384615384615385}


Saved tuned model to: ./titanic_output/best_random_forest.joblib