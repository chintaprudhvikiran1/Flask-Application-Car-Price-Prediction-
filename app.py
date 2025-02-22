from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import json

app = Flask(__name__)

model_path = "model/cpp_model.pkl"
with open(model_path,"rb") as file:
    model=pickle.load(file)

ranges_path = "model/feature_ranges.json"
with open(ranges_path,"r") as file:
    feature_ranges = json.load(file)

@app.route("/")
def root():
    return render_template("form.html", ranges = feature_ranges)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        inputs = [
            int(request.form.get("Year")),
            float(request.form.get("EngineV"))
        ]

        input_array = np.array([inputs]).reshape(1,-1)

        predicted_price = model.predict(input_array)[0]

        return jsonify({
            "input": {
                "Year": inputs[0],
                "EngineV": inputs[1],
            },
            "predicted_price": round(predicted_price, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}),400
    
if __name__=="__main__":
    app.run(debug=True)


