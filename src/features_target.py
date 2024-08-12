import logging
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class FeatureTarget:
    @staticmethod
    def features_and_target(data: pd.DataFrame):
        try:
            X = data.drop("Monthly Sales", axis=1)
            y = data["Monthly Sales"]
            logging.info("Successfully select features and target variables.")
            return X, y
        except Exception as e:
            logging.error(f"Failed to select features and target variables. {str(e)}")
            raise
        
    @staticmethod
    def train_and_test_split(X:pd.DataFrame, y:pd.DataFrame, random_state=42, test_size=0.2):
        
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                                test_size=test_size, 
                                                                random_state=random_state)
            logging.info("Successfully split train and test")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(f"Failed to split train and test. {str(e)}")
            raise