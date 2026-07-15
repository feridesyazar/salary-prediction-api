import os
import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

with open("maas.pkl", "rb") as model_file:
    model = pickle.load(model_file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        tecrube = float(request.form["tecrube"])
        yazili = float(request.form["yazili"])
        mulakat = float(request.form["mulakat"])

        prediction = model.predict([[tecrube, yazili, mulakat]])
        predicted_salary = round(float(prediction[0]), 2)

        return render_template(
            "index.html",
            prediction=predicted_salary
        )

    except (KeyError, ValueError):
        return render_template(
            "index.html",
            error="Lütfen bütün alanlara geçerli sayılar girin."
        ), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
