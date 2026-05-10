from flask import Flask, request, jsonify
import pickle
import pandas as pd
# Load trained model
model = pickle.load(open("spam_model.pkl", "rb"))

# Load scaler
scaler = pickle.load(open("scaler.pkl", "rb"))

# Load feature names (3000 words)
feature_names = pickle.load(open("feature_names.pkl", "rb"))
app = Flask(__name__)
def preprocess_email(text):
    # convert to lowercase
    words = text.lower().split()

    # create empty feature dictionary
    data = dict.fromkeys(feature_names, 0)

    # count word occurrences
    for word in words:
        if word in data:
            data[word] += 1

    # convert to dataframe
    df = pd.DataFrame([data])

    # scale input
    df_scaled = scaler.transform(df)

    return df_scaled
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # get JSON input
        data = request.json
        email_text = data["email"]

        # preprocess
        processed = preprocess_email(email_text)

        # prediction
        prediction = model.predict(processed)[0]

        # probability (spam confidence)
        probability = model.predict_proba(processed)[0][1]

        # return result
        return jsonify({
            "prediction": "Spam" if prediction == 1 else "Not Spam",
            "spam_probability": round(float(probability), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)})
@app.route("/")
def home():
    return "Spam Classifier API is running!"
if __name__ == "__main__":
    app.run(debug=True)