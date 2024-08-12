import logging
import pandas as pd
import numpy as np
from src.data_ingestion import DataIngestion
from src.data_preprocessing import Preprocessing
from src.model_training import ModelBuilding
from src.evaluation import Evaluation
from src.model_inference import ModelInferences
from src.config import Config
from src.features_target import FeatureTarget

try:
    path = Config.DATA_PATH
    data = DataIngestion.read_data(path=path)
    logging.info(f"Data successfully ingested from {Config.DATA_PATH}.")
except Exception as e:
    logging.error(f"Failed in data ingestion of pipeline. {str(e)}")
    raise e

try:
    data = Preprocessing.preprocessing(data)
    logging.info("Data preprocessing completed successfully.")
except Exception as e:
    logging.error(f"Failed in preprocessing of pipeline. {str(e)}")
    raise e

try:
    X, y = FeatureTarget.features_and_target(data)
    logging.info("Features and target variables successfully selected.")
except Exception as e:
    logging.error(f"Failed in features_and_target of pipeline. {str(e)}")
    raise e
try:
    X_train, X_test, y_train, y_test = FeatureTarget.train_and_test_split(X, y)
    logging.info("Data successfully split into train and test sets.")
except Exception as e:
    logging.error(f"Failed in train_and_test_split of pipeline. {str(e)}")
    raise e

best_params = {
            "n_estimators" : 450,
            "criterion" : 'squared_error',
            "max_leaf_nodes" : 160,
            "random_state" : 42,
            "max_depth":5          
        }

try:
    model = ModelBuilding.model_building(X, y, best_params)
    logging.info("Model successfully built and predictions made.")
except Exception as e:
    logging.error(f"Failed in model_building of pipeline. {str(e)}")
    raise e
"""
try:
    rmse, mape, r2 = Evaluation.evaluate_model(y_test, y_pred)
    logging.info(f"Model evaluation metrics - RMSE: {rmse}, MAPE: {mape}, R²: {r2}")
except Exception as e:
    logging.error(f"Failed in evaluate_model of pipeline. {str(e)}")
    raise e
"""
try:
    prediction = ModelInferences.model_inference(model, input=np.array(int(11311)).reshape(-1, 1))
    logging.info(f"Model inference successful. Predictions: {prediction}")
except Exception as e:
    logging.error(f"Failed in model_inference of pipeline. {str(e)}")
    raise e

