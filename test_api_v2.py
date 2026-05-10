import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "email": "Congratulations! You have won free money. Click now!"
}

response = requests.post(url, json=data)

print(response.json())