import pandas as pd
import numpy as np 
import logging
from sklearn.metrics import r2_score, mean_absolute_percentage_error, mean_squared_error

class Evaluation:
    @staticmethod
    def evaluate_model(y_test: pd.Series, y_pred: pd.Series):
        try:
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            mape = mean_absolute_percentage_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print(f"RMSE: {rmse}, MAPE: {mape}, R²: {r2}")
            logging.info("Successfull evaluation.")
            return rmse, mape, r2
        except Exception as e:
            logging.error(f"Failed to evaluate metrics. {str(e)}")
            raise e