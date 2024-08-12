import logging
import pandas as pd
import numpy as np

class Preprocessing:
    @staticmethod
    def preprocessing(raw_data: pd.DataFrame):
        try:
            # Remove duplicate rows.
            raw_data.drop_duplicates(inplace=True)

            # Remove unnecessary columns.
            columns_to_keep = ["BSR", "Monthly Sales"]
            data = raw_data[columns_to_keep].copy()
            
            # Remove null rows.
            data.dropna(inplace=True)
            
            logging.info("Successfully completed preprocessing.")
            return data
        except Exception as e:
            logging.error(f"Error in preprocessing. {e}")
            raise e