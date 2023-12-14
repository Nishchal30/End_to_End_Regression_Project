# Import all the required packages

import os, sys
import pandas as pd
import numpy as np
from pathlib import Path

from dataclasses import dataclass
from src.Diamond_Price_Prediction.logger import logging
from src.Diamond_Price_Prediction.exception import CustomExecption

from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.Diamond_Price_Prediction.utils.utils import save_object

# Create a config class for data transformation

@dataclass
class DataTransformationConfig:

    # create a variable to store the output of data transformation into .pkl file into the artifacts folder
    preprocessor_obj_file_path = os.path.join(Path(os.getcwd()).resolve().parents[2], "artifacts", "preprocessor.pkl")

# Create an actual data transformation class

class DataTransformation:
    def __init__(self):

        # create an object of data transformation config class
        self.data_transformation_config = DataTransformationConfig()

    
    # A method to perform all the necessary data transformation activites
    def get_data_transformation(self):
    
        try:
            logging.info("Data transformation started here")

            # Define which columns should be ordinal encoded and which should be scaled
            categorical_features = ['cut', 'color', 'clarity']
            numerical_features = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Define the custom ranking for each ordinal variable
            cut_categories = ["Fair","Good","Very Good","Premium", "Ideal"]
            color_categories = ["D", "E", "F", "G", "H", "I", "J"]
            clarity_categories = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"] 

            logging.info("Pipeline started here")

            # Numerical Pipeline
            numerical_pipeline = Pipeline(

                    steps = [
                        ("Imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler())
                    ]
            )

            # Categorical Pipeline
            categorical_pipeline = Pipeline(

                    steps = [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("ordinalencoder", OrdinalEncoder(categories = [cut_categories, color_categories, clarity_categories])),
                        ("scaler", StandardScaler())
                    ]
            )

            # tranformation object
            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, categorical_features)
                ]
            )

            return preprocessor

        except Exception as e:
            logging.info("Exception occured in get data transformation")
            raise CustomExecption(e, sys)


    # Method to initiate the above tranformation method on train & test data
    def initiate_data_transformation(self, train_data_path, test_data_path):
        
        try:

            # first read train & test data
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)

            logging.info("train & test data read successfully")
            logging.info(f"train df head: \n{train_data.head().to_string()}")
            logging.info(f"test df head: \n{test_data.head().to_string()}")


            # Object of the above tranformation method
            preprocessor_obj = self.get_data_transformation()

            # Define target columns and drop those columns which we don't need in training data
            target_column = "price"
            drop_columns = [target_column, "id"]

            train_data_updated = train_data.drop(drop_columns, axis=1)
            test_data_updated = test_data.drop(drop_columns, axis=1)
            target_column_train_data = train_data[target_column]
            target_column_test_data = test_data[target_column]

            # Fit & tranform the train data with the transformation object created above
            train_data_updated_tranformed = preprocessor_obj.fit_transform(train_data_updated)
            test_data_updated_tranformed = preprocessor_obj.transform(test_data_updated)

            logging.info("Successfully applied preprocessor object on train & test dataset")

            train_arr = np.c_[train_data_updated_tranformed, np.array(target_column_train_data)]
            test_arr = np.c_[test_data_updated_tranformed, np.array(target_column_test_data)]

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )

            logging.info("preprocessing pickle object created")

            return(
                train_arr, test_arr
            )
        
            logging.info("Data transformation is completed here")
        except Exception as e:
            logging.info("Exception occured in initiate data transformation")
            raise CustomExecption(e, sys)
        
    
