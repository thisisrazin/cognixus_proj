import requests

endpoint='http://127.0.0.1:8000/accounts/login/'

body={
    "username": "testuser", 
    "password": "testpassword", 
}

response=requests.post(endpoint, json=body)
print(response.json())