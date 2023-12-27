from src.Diamond_Price_Prediction.Pipelines.prediction_pipeline import CustomData, PredictPipeline

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home_page():
    return render_template("index.html")


@app.route("/predict", methods = ["GET", "POST"])
def predict_data():
    if request.method == "GET":
        return render_template("form.html")

    else:
        
        data = CustomData(
            carat=float(request.form.get("carat")),
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x = float(request.form.get("x")),
            y = float(request.form.get("y")),
            z = float(request.form.get("z")),
            cut = str(request.form.get("cut")),
            color= str(request.form.get("color")),
            clarity= str(request.form.get("clarity"))
        )

        final_data = data.get_data_as_df()
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(final_data)
        result = round(prediction[0],2)

        return render_template("result.html", final_result = result)

if __name__ == "__main__":
    app.run()

