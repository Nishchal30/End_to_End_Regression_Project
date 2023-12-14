#import all required packages

import pandas as pd
import numpy as np
from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os,sys

# Define a config class to store the data files

class DataIngestionConfig:
    
    raw_data_path : str = os.path.join(Path(os.getcwd()).resolve().parents[2], "artifacts", "raw.csv")
    train_data_path : str = os.path.join(Path(os.getcwd()).resolve().parents[2], "artifacts","train.csv")
    test_data_path : str = os.path.join(Path(os.getcwd()).resolve().parents[2], "artifacts", "test.csv")

# define a class for ingesting the data

class DataIngestion:
    def __init__(self):

        # create a object of config class
        self.ingestion_config = DataIngestionConfig()

    # A method to initiate the data ingestion

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started here")

        try:
            # read the data from the data foler
            data = pd.read_csv(Path(os.path.join(Path(os.getcwd()).resolve().parents[2], 'notebooks', 'data', 'train.csv')))
            logging.info("Read the training data")
            
            # create a directory called artifacts to store the raw data
            os.makedirs(os.path.join(Path(os.getcwd()).resolve().parents[2],"artifacts"), exist_ok=True)
            data.to_csv(os.path.join(Path(os.getcwd()).resolve().parents[2],self.ingestion_config.raw_data_path), index=False)
            logging.info("Saved the raw data in artifacts folder")

            # split the raw data into train & test and store into the artifacts folder
            train_data, test_data = train_test_split(data, test_size=0.3)
            logging.info("train test split completed")

            train_data.to_csv(os.path.join(Path(os.getcwd()).resolve().parents[2],self.ingestion_config.train_data_path), index=False)
            test_data.to_csv(os.path.join(Path(os.getcwd()).resolve().parents[2],self.ingestion_config.test_data_path), index=False)

            logging.info("Saved the train & test data in artifacts folder")
            logging.info("The data ingestion part is completed here")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Exception occured at the data ingestion stage")
            raise CustomExecption(e, sys)
        

