import pandas as pd
import numpy as np
import logging

class ModelInferences:
    @staticmethod
    def model_inference(model, input:pd.Series):
        try:
            prediction = model.predict(input)
            prediction_value = int(prediction[0]) if isinstance(prediction, np.ndarray) else int(prediction)
            print(prediction_value)
            logging.info("Prediction completed.")
            return prediction
        except Exception as e:
            logging.error(f"Prediction failed. {str(e)}")
            raise e