from src.Diamond_Price_Prediction.Pipelines.prediction_pipeline import CustomData

data = CustomData(0.32,62.3,55.0,4.41,4.43,2.75,"Very Good","H","VS1")
df = data.get_data_as_df()

print(df)