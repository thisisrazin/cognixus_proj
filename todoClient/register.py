import requests

endpoint='http://127.0.0.1:8000/accounts/register/'

body={
    "username": "testuser", 
    "password": "testpassword", 
    "email": "test@example.com"
}

response=requests.post(endpoint, json=body)
print(response.json())