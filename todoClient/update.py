import requests

def getToken(endpoint, user, password):
    body={"username": user, "password": password}
    auth_response=requests.post(endpoint, json=body)
    if auth_response.status_code==200:
        token=auth_response.json()['token']
        return token

token=getToken(
    'http://127.0.0.1:8000/todo_app/auth/', 
    'testuser', 
    'testpassword'
)

endpoint='http://127.0.0.1:8000/todo_app/todo/update/4'
headers={"Authorization": f"Token {token}"}
body={'isComplete': True}

response=requests.patch(endpoint, headers=headers, json=body)
print(response.json())