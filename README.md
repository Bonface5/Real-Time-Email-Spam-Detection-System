# 📧 Real-Time Email Spam Detection System

> A Machine Learning-based system that classifies emails as **Spam** or **Ham** using NLP and Logistic Regression, deployed as a real-time Flask API.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Objective](#-objective)
- [Dataset](#-dataset)
- [ML Pipeline](#-machine-learning-pipeline)
- [Model Performance](#-model-performance)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [How to Run Locally](#-how-to-run-locally)
- [API Usage](#-api-usage)
- [Deployment](#-deployment)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)

---

## 🚀 Overview

This project is an end-to-end **Email Spam Detection System** that:

- Classifies emails as **Spam** or **Not Spam (Ham)**
- Uses **word-frequency features** and a **Logistic Regression** model
- Is deployed as a **Flask REST API** for real-time predictions

---

## 🎯 Objective

- Build a binary classification model for spam detection
- Analyze email word-frequency patterns
- Train and evaluate a Logistic Regression model
- Deploy a real-time prediction API using Flask

---

## 📊 Dataset

| Property | Details |
|---|---|
| Source | Kaggle Email Spam Classification Dataset |
| Total Samples | 5,172 emails |
| Features | 3,000+ word frequency columns |
| Target `0` | Not Spam (Ham) |
| Target `1` | Spam |

---

## 🧠 Machine Learning Pipeline

```
1. Data Loading & Exploration
2. Feature Selection
3. Train-Test Split (80/20, stratified)
4. Feature Scaling (Standardization)
5. Model Training (Logistic Regression)
6. Model Evaluation
7. Model Serialization (Pickle)
8. Flask API Development
9. Real-Time Prediction System
```

---

## 🤖 Model Performance

| Split | Accuracy |
|---|---|
| Training | **99.98%** |
| Testing | **96.9%** |

**Key Metrics:**
- High precision and recall for both classes
- Very low false negative rate
- Strong generalization to unseen data

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| API Framework | Flask |
| Serialization | Pickle |
| Development | Jupyter Notebook, VS Code |

---

## 📁 Project Structure

```
spam-classifier/
│
├── app.py                        # Flask API
├── test.py                       # API testing script
├── spam_model.pkl                # Trained ML model
├── scaler.pkl                    # Feature scaler
├── feature_names.pkl             # Feature structure
├── emails.csv                    # Dataset
├── requirements.txt              # Dependencies
├── README.md                     # Documentation
│
└── notebook/
    └── spam_detection.ipynb      # Jupyter Notebook
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Real-Time-Email-Spam-Detection-System.git
cd Real-Time-Email-Spam-Detection-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask API

```bash
python app.py
```

The API will be available at: `http://127.0.0.1:5000`

### 4️⃣ Test the API

```bash
python test.py
```

---

## 📡 API Usage

### Endpoint

```
POST /predict
```

### Request Example

```json
{
  "the": 0,
  "to": 0,
  "and": 1,
  "free": 2,
  "win": 1
}
```

### Response Example

```json
{
  "prediction": "Spam",
  "spam_probability": 0.94
}
```

---

## 🌍 Deployment

This project can be deployed using:

| Platform | Notes |
|---|---|
| **Render** | Recommended |
| Railway | Easy setup |
| AWS Elastic Beanstalk | Scalable |
| Heroku | If supported |

---

## 🚀 Future Improvements

- [ ] Deploy live API on cloud (Render/AWS)
- [ ] Add frontend UI for email input
- [ ] Use TF-IDF or Word Embeddings for better NLP performance
- [ ] Allow raw email text input instead of feature vectors
- [ ] Experiment with advanced models (Naive Bayes, XGBoost, etc.)

---

## 👨‍💻 Author

**Bonface Kanyi**
- 🎓 BSc Applied Statistics with Computing
- 💡 Data Science & AI Enthusiast

---

## ⭐ Acknowledgements

- Kaggle dataset contributors
- Scikit-learn documentation
- Flask framework community

---

## 📌 Summary

This project demonstrates a complete **end-to-end ML pipeline** including data preprocessing, model training, evaluation, serialization, and real-time deployment using Flask. It showcases practical skills in **Machine Learning**, **NLP**, and **API development**.

---

> ⭐ **If you find this project helpful, feel free to star, fork, improve, and share it!**
