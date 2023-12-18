from src.Diamond_Price_Prediction.Pipelines.prediction_pipeline import CustomData, PredictPipeline

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

