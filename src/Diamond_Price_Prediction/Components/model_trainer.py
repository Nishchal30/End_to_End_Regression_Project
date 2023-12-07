# Import all the required packages

import os, sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

from src.Diamond_Price_Prediction.utils.utils import save_object, evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_obj = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self):
        
        try:
            logging.info("split dependent & independent variables from train & test data")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models = {
                "LinearRegression": LinearRegression(),
                "RidgeRegression": Ridge(),
                "LassoRegression": Lasso(),
                "ElasticNetRegression": ElasticNet
            }

            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print("\n==================================================================\n")
            logging.info(f"Model report: {model_report}")


            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]        

            best_model = models[best_model_name]

            print(f"Best model found, model name: {best_model_name}, R2_score: {best_model_score}")
            print("\n==================================================================\n")
            logging.info(f"Best model found, model name: {best_model_name}, R2_score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_obj,
                obj=best_model
            )

        except Exception as e:
            logging.info("Exception occured in model training")
            raise CustomExecption(e, sys)