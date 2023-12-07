from src.Diamond_Price_Prediction.Components.data_ingestion import DataIngestion
import os, sys
from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption
import pandas as pd

obj = DataIngestion()

obj.initiate_data_ingestion()