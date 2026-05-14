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

## ⭐ Acknowledgements

- Kaggle dataset contributors
- Scikit-learn documentation
- Flask framework community

---


---

# 🔵 NLP Upgrade (v2)

A second version of the project was developed to demonstrate a production-style Natural Language Processing (NLP) workflow using TF-IDF vectorization, Flask API integration, and real-time cloud deployment.

Unlike the original structured-feature implementation, v2 accepts raw email text input and performs real-time spam prediction through a deployed REST API.

This repository therefore demonstrates the evolution of an email spam detection system from a traditional machine learning workflow into a deployment-oriented NLP application.

---

# 🔍 Project Evolution: v1 vs v2

## 🟢 Version 1 — Structured Feature Model

The original implementation used engineered word-frequency features from the dataset to train a Logistic Regression classifier with very high predictive performance.

### Characteristics

- Structured numerical feature input
- Feature scaling using StandardScaler
- Traditional supervised ML workflow
- Optimized for dataset performance
- High classification accuracy
- Statistical feature engineering approach

---

## 🔵 Version 2 — NLP Pipeline Demo

The second implementation explores a production-oriented NLP workflow using TF-IDF vectorization and real-time API deployment.

### Characteristics

- Raw email text input
- TF-IDF vectorization
- Logistic Regression NLP pipeline
- Real-time inference API
- Flask backend integration
- Render cloud deployment
- Git branch versioning workflow
- API-based prediction system

---

# 🧠 v2 Architecture

```text
User Email Text
        ↓
TF-IDF Vectorizer
        ↓
Logistic Regression
        ↓
Flask API
        ↓
Render Cloud Deployment
        ↓
Live Real-Time Inference
```

---

# ⚠️ Important Technical Note

The original dataset used in this project was structured as engineered word-frequency features rather than raw email text.

As a result:

- v1 achieves stronger predictive accuracy on the provided dataset
- v2 focuses on demonstrating NLP architecture and deployment workflow rather than maximizing benchmark accuracy

This distinction reflects a realistic machine learning engineering progression:

```text
Dataset-Based Modeling
            ↓
Production-Style NLP Systems
```

---

# ⚙️ Technologies Used in v2

- Python
- TF-IDF Vectorization
- Logistic Regression
- Scikit-learn
- Flask REST API
- Pickle Model Serialization
- Render Cloud Deployment
- Git & GitHub
- Jupyter Notebook
- VS Code

---

# 🌍 Live API Deployment

The NLP demo API is deployed on Render and can process real-time email text input through a publicly accessible endpoint.

## Endpoint

```text
https://real-time-email-spam-detection-system-1.onrender.com/predict
```

---

## Example Request

```json
{
  "email": "Congratulations! You won free money now!"
}
```

---

## Example Response

```json
{
  "prediction": "Spam",
  "spam_probability": 0.88
}
```

---

# 🧪 API Testing Methods

The deployed API can be tested using:

- Python `requests`
- Postman
- Frontend web interfaces
- External applications consuming the endpoint
- Local Flask testing environments

---

# 🌐 Deployment Workflow

The project follows a complete end-to-end deployment lifecycle:

```text
Train Model
    ↓
Evaluate Model
    ↓
Serialize Model (.pkl)
    ↓
Build Flask API
    ↓
Local API Testing
    ↓
GitHub Version Control
    ↓
Render Cloud Deployment
    ↓
Live Public Endpoint
    ↓
Real-Time Inference
```

---

# 📁 v2 Files

```text
app_v2.py
spam_model_v2.pkl
test_api_v2.py
Real-Time Email Spam Detection System v2.ipynb
```

---

# 🌿 Git Branches

| Branch | Description |
|--------|-------------|
| `main` | Original structured-feature spam classifier |
| `nlp-upgrade-v2` | NLP demo version with TF-IDF and deployed API |

---

# 🚀 Key Learning Outcomes

- Building end-to-end ML systems
- NLP pipeline design
- Real-time inference systems
- API development with Flask
- Cloud deployment using Render
- Model serialization with Pickle
- Git branching and version control
- Backend API integration
- Deployment workflow management
- Production-style ML architecture

---

# 💼 Skills Demonstrated

This project demonstrates practical skills in:

- Machine Learning
- Natural Language Processing (NLP)
- Logistic Regression Modeling
- TF-IDF Feature Engineering
- Flask API Development
- REST API Design
- Model Serialization
- Real-Time Inference Systems
- Git & GitHub Workflow
- Cloud Deployment
- Version Control with Branching
- End-to-End ML Engineering

---

## 👨‍💻 Author

**Bonface Kanyi**
- 🎓 BSc Applied Statistics with Computing
- 💡 Data Science & AI Enthusiast

---

## 📌 Summary

This project demonstrates a complete **end-to-end ML pipeline** including data preprocessing, model training, evaluation, serialization, and real-time deployment using Flask. It showcases practical skills in **Machine Learning**, **NLP**, and **API development**.

---
> ⭐ **If you find this project helpful, feel free to star, fork, improve, and share it!**
