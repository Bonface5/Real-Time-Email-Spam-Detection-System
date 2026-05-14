import requests

url = "https://real-time-email-spam-detection-system-1.onrender.com/predict"

data = {
    "email": "Congratulations! You have won free money. Click now!"
}

response = requests.post(url, json=data)

print(response.json())