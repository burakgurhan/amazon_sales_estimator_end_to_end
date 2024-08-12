import os

class Config:
    DATA_PATH = "/Users/salihburakgurhan/Python/end_to_end_sales_estimator/data/data.csv"
    MODEL_PATH = "models/random_forest.pkl"
    RANDOM_STATE = 42
    TEST_SIZE = 0.2
    N_ESTIMATORS = 200
#print(os.listdir())