import logging
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class ModelBuilding:
    @staticmethod   
    def model_building(X,y, params:dict):
        try:
            model = RandomForestRegressor(**params).fit(X, y)
         
            #y_pred = model.predict(X_test)
            logging.info("Successfully build model")
            return model
        except Exception as e:
            logging.error(f"Failed to build model. {str(e)}")
            raise 