import requests

endpoint='http://127.0.0.1:8000/todo_app/todo/'

response=requests.get(endpoint)
print(response.json())