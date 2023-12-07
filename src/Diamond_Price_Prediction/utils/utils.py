import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.Diamond_Price_Prediction.exception import CustomExecption
from src.Diamond_Price_Prediction.logger import logging


from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomExecption(e, sys)
