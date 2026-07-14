from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


@app.route("/result", methods=["POST"])
def result():

    # mengambil data dari form
    gender = request.form.get("gender")
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    activity = request.form.get("activity")
    family = request.form.get("family")
    water = request.form.get("water")
    sleep = request.form.get("sleep")

    # sementara hasil dummy
    prediction = "Risiko Obesitas Sedang"
    probability = 87

    return render_template(
        "result.html",
        prediction=prediction,
        probability=probability,
        age=age,
        height=height,
        weight=weight,
        gender=gender
    )


if __name__ == "__main__":
    app.run(debug=True)