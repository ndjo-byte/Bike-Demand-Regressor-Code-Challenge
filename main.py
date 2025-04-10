import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from src import DataProcessor, ModelManager

train_path = './data/train/train.csv'
test_path = './data/test/test.csv'

print('-'*10, 'Data Processing', '-'*10)
train_processor = DataProcessor(train_path)
train_processed = (train_processor
                   .manage_datatypes()
                   .show_missing_values()
                   .date_feature_engineering()
                   .cnt_feature_engineering()
                   )

test_processor = DataProcessor(test_path, hourly_stats=train_processor.hourly_stats)
test_processed = (test_processor
                  .manage_datatypes()
                  .show_missing_values()
                  .date_feature_engineering()
                  .cnt_feature_engineering(is_train=False))

train_df = train_processed.df
test_df = test_processed.df

print('-'*10, 'Model Training and Evaluation', '-'*10)
model=RandomForestRegressor(n_estimators=30, max_depth=4)
trainer = ModelManager(model=model)
features = ['temp', 'hum', 'windspeed', 
            'cos_hour',  'sin_hour',
            'cos_month', 'sin_month',
            'mean', 'median', 'std',
            'q10', 'q10']
trained_model = (trainer
                 .split(train_df, features=features)
                 .train())
trained_model.predict()
trained_model.evaluate()


print('-'*10, 'Model Prediction', '-'*10)
X=test_df[features]
trained_model.predict(X=X)
trained_model.get_predictions_json(df=test_df,prediction_file_path='./predictions/predictions.json' )








