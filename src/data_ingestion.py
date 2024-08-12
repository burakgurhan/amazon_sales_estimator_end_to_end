import logging
import pandas as pd
#from src.config import Config


class DataIngestion:
    @staticmethod
    def read_data(path):
        try: 
            raw_data = pd.read_csv(path)
            logging.info("Successfully read data.")
            return raw_data
        except FileNotFoundError:
            logging.error(f"File not found: {path}")
            raise
        except pd.errors.EmptyDataError:
            logging.error(f"No data: {path} is empty.")
            raise
        except pd.errors.ParserError:
            logging.error(f"Error parsing data: {path}.")
            raise
        except Exception as e:
            logging.error(f"Error reading data: {str(e)}")
            raise