class ModelManager():

    def __init__(self, model=None):
        self.model = model
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None 
        self.features = None
        self.y_pred_test = None
        self.y_pred_new = None

    def split(self, df, target_col='cnt', features:list=[], test_size=0.15):
        from sklearn.model_selection import train_test_split
        if not features:
             raise ValueError("❌ No features provided. Please specify a list of features to train with.")
        self.features = features
        X = df[features]
        y = df[target_col]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        print(f"✅ Data split complete.")
        print(f"   - X_train shape: {self.X_train.shape}")
        print(f"   - X_test shape: {self.X_test.shape}")
        print(f"   - y_train shape: {self.y_train.shape}")
        print(f"   - y_test shape: {self.y_test.shape}")         
        return self

    def train(self):
        if self.model is None:
            raise ValueError('No model has been set.')
        self.model.fit(self.X_train, self.y_train)
        print("✅ Model training complete.")
        return self
    
    def predict(self, X=None):
        if self.model is None:
            raise ValueError("❌ Model not found. Train model first.")
        if X is None:
            if self.X_test is None: 
                raise ValueError("❌ Test data not found. Split data first.")
            self.y_pred_test = self.model.predict(self.X_test)
            print("✅ Model test prediction complete and saved as list: y_pred_test.")
            return self.y_pred_test
        else:
            self.y_pred_new = self.model.predict(X)
            print("✅ Model new prediction saved as list: y_pred_new.")
            return self.y_pred_new


    def evaluate(self):
        from sklearn.metrics import mean_absolute_error

        print("📊 Evaluation Metrics:")
        print(f"MAE: {mean_absolute_error(self.y_test, self.y_pred_test):.2f}")
        return self


    def save(self):
        pass

    def get_predictions_json(self,df,prediction_file_path: str) -> None:
        """
        Save predictions as JSON in the required format:
            {
                "target": {
                    "datetime_string": prediction_value,
                    ...
                }
            }
        """
        if not prediction_file_path:
            raise ValueError("❌ Path to destination file required. Input prediction_file_path")
        
        import json
        import numpy as np 

        keys = df['dteday'].dt.strftime('%Y-%m-%d %H:%M').tolist()
        values = np.rint(self.y_pred_new).astype(int).tolist()
        new_prediction_dict = {'target': 
                               dict(zip(keys, values))
                               }

        with open(prediction_file_path, "w") as f:
            json.dump(new_prediction_dict, f, indent=4)

        print(f"✅ Predictions saved to {prediction_file_path}")
        
        for dt, pred in list(zip(keys, values))[:5]:
            print(f"{dt}: {pred}")

### Updates 
# save model 
# python pipeline
# bayesion optimisation 
