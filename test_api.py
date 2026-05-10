import requests

url = "https://real-time-email-spam-detection-system.onrender.com/predict"

data = {
    "email": "Congratulations! You have won a free prize. Click here now!"
}

response = requests.post(url, json=data)

print(response.json())