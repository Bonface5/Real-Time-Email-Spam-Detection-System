import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "email": "Congratulations you won free money click here"
}

response = requests.post(url, json=data)

print(response.json())
