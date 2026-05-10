from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("spam_model_v2.pkl", "rb"))

@app.route("/")
def home():
    return "Spam Detection API v2 (NLP Demo) Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    email = data["email"]

    prediction = model.predict([email])[0]
    probability = model.predict_proba([email])[0][1]

    return jsonify({
        "prediction": "Spam" if prediction == 1 else "Not Spam",
        "spam_probability": float(probability)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)