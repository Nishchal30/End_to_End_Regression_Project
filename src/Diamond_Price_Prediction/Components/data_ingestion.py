import pandas as pd
import numpy as np
from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os


class DataIngestion:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started here")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data", "train.csv")))
            logging.info("Read the training data")

            train_data, test_data = train_test_split(data, test_size=0.3)
            logging.info("train test split completed")

            

        except Exception as e:
            pass