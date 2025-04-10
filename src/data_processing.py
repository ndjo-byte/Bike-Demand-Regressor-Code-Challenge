import pandas as pd 
import numpy as np

class DataProcessor:


    def __init__ (self, path:str, hourly_stats=None):
        '''Load dataset to dataframe from given path'''
        try:
            self.df = pd.read_csv(path)
            print('✅ Dataframe success')
            print(self.df.head(3))
            print(self.df.shape)
            self.hourly_stats = hourly_stats
        except Exception as e:
            print(f'⚠️ Error loading:{e}')
    
    
    def manage_datatypes(self):
        '''Ensure datetime data-type and incorporate hours from "hr" column.'''
        try:
            if 'dteday' in self.df.columns and 'hr' in self.df.columns:
                self.df['dteday'] = pd.to_datetime(self.df['dteday'])
                self.df['dteday'] = pd.to_datetime(self.df['dteday'].astype(str) + ' ' + self.df['hr'].astype(str))
                print('✅ hr correctly incorporated into dteday as datetime')
            else:
                print('⚠️ "dteday" or "hr" not found in dataframe')
        except Exception as e:
            print(f'❌ Error in manage_datetypes{e}')
        return self
    
    def show_missing_values(self):
        '''Display and return missing values in dataset'''
        missing = self.df.isna().sum() 
        missing = missing[missing >0].sort_values(ascending=False)
        if missing.empty:
            print('✅ No missing values')
        else:
            print('⚠️ Missing values detected:', missing)
        return self       

    
    def impute_missing_values(self, strategy="mean"):
        '''Fill missing values with selected imputation technique: mean, median or mode.
        Default is mean. '''

        strategy = strategy.lower()

        if self.df.isna.sum().sum() == 0:
            print('✅ No missing values and imputation not necessary')
            return self #permits method chaining
    
        if strategy == 'mean':
            self.df.fillna(self.df.mean(), inplace=True)
        elif strategy == 'mode':
            self.df.fillna(self.df.mode(), inplace=True)
        elif strategy == 'median':
            for col in self.df.colums:
                self.df['col'].fillna(self.df[col].mode()[0], inplace=True)
        else:
            print(f'⚠️ {strategy} is not supported. Choose from mean, median or mode.')
        
        print(f'✅ Missing values correctly imputed using {strategy}')
        return self
    
    
    def date_feature_engineering(self):
        
        try:
            if 'hr' in self.df.columns and 'mnth' in self.df.columns:
                self.df['cos_hour'] = np.cos(2 * np.pi * self.df['hr'] / 24)
                self.df['sin_hour'] = np.sin(2 * np.pi * self.df['hr'] / 24)


                self.df['cos_month'] = np.cos(2 * np.pi * self.df['mnth'] / 24)
                self.df['sin_month'] = np.sin(2 * np.pi * self.df['mnth'] / 24)
                self.df.drop(columns=['mnth'], inplace=True)

                print('✅ Cyclical features for month and hour created.')

            else:
                print(f'⚠️ "hr" or "month" not found in dataset.')
        
        except Exception as e:
            print(f'❌ Error in date_feature_engineering: {e}')

        return self

    def cnt_feature_engineering(self, is_train=True):
        '''Engineer and store hourly statistical values in (train) dataframe containing (target) cnt values, else use stored statistics.'''
        try:
            if is_train:
                if 'cnt' in self.df.columns:
                    hourly_stats = self.df.groupby('hr')['cnt'].agg(
                        mean = 'mean',
                        median = 'median',
                        std = 'std',
                        q90 = lambda x: x.quantile(0.9),
                        q10 = lambda x: x.quantile(0.1)
                    ).reset_index()

                    #apply to (train) dataset
                    self.df = self.df.merge(hourly_stats, how='left', on='hr')

                    #store as class attribute
                    self.hourly_stats = hourly_stats
                    
                    print('✅ hourly_stats computed, merged and stored.')
                
                else:
                   print(f'⚠️ "cnt" not found in dataset.') 

            elif not is_train and self.hourly_stats is not None and not self.hourly_stats.empty:
                if 'cnt' not in self.df.columns:
                    self.df = self.df.merge(self.hourly_stats, how='left', on='hr')
                    print('✅ hourly_stats applied to test data.')

                    


        except Exception as e:
            print(f'❌ Error in cnt_feature_engineering: {e}')

        return self

