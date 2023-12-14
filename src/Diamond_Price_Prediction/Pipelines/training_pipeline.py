from src.Diamond_Price_Prediction.Components.data_ingestion import DataIngestion
from src.Diamond_Price_Prediction.Components.data_transformation import DataTransformation
from src.Diamond_Price_Prediction.Components.model_trainer import ModelTrainer
import os, sys

import sys
sys.path.append(r'D:\Machine_Learning_Projects\End_to_End_Regression_Project\src\Diamond_Price_Prediction\Pipelines')

from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption
import pandas as pd



ingest_obj = DataIngestion()

train_path, test_path = ingest_obj.initiate_data_ingestion()

transform_obj = DataTransformation()

train_data, test_data = transform_obj.initiate_data_transformation(train_path, test_path)

model_trainer_obj = ModelTrainer()

model_trainer_obj.initiate_model_training(train_data, test_data)



