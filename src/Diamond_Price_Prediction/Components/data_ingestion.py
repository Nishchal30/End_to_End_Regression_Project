import pandas as pd
import numpy as np
from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os,sys


class DataIngestionConfig:
    
    raw_data_path : str = os.path.join("artifacts", "raw.csv")
    train_data_path : str = os.path.join("artifacts","train.csv")
    test_data_path : str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        logging.info("Data ingestion started here")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks","data", "train.csv")))
            logging.info("Read the training data")

            os.makedirs(os.path.join(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved the raw data in artifacts folder")

            train_data, test_data = train_test_split(data, test_size=0.3)
            logging.info("train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Saved the train & test data in artifacts folder")
            logging.info("The data ingestion part is completed here")



        except Exception as e:
            logging.info("Exception occured at the data ingestion stage")
            raise CustomExecption(e, sys)