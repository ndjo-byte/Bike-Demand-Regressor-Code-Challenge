1. confirm data types info(), pd.to_datetime
    - date has been split, and is now -apart from determining range- redundant because it has lost its hour granularity
3. confirm date range max()- min()
4. check missing hours pd.date_range(min ,max ,freq='h') 
5. check missing values .isna().sum() and 
6. vizualise variable distribution to identify potential outliers 
7. cnt statistics as feature engineering
8. vizualise heatmap correlation between variables
9. cnt will be target.

classes 
1. data processing 
class methods: 
- manage data types (from any issues found in EDA)
- display missing values 
- impute missing values 
- date feature engineering 
- cnt statistics feature engineering 
    - cnt statistics store (class attribute)
    - cnt statistics apply to test

2. model mananger
class methods: 
- split 
- train 
- test
- evaluate 
- feature importance
- save 
- predict 
