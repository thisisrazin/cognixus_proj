Operating System: Mac OS Ventura

1. Instructions for building and running the app

Running in Local Environment

1) Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2) Install pipenv using Homebrew
brew install pipenv

3) Open the terminal and change the directory to the django project folder titled 'cognixus_proj'
(alternatively you can just open the project in VSCode and use the integrated terminal within the IDE)

4) Install the required packages in a newly created Python Virtual Environment
pipenv install -r requirements.txt

5) Activate the Python Virtual Environment
pipenv shell

Note: The terminal should now have (cognixus_proj) at the beginning the directory
to indicate that the Python Virtual Environment is activated

6) Migrate the Database
python manage.py makemigrations
python manage.py migrate

7) Run the 'cognixus_proj' django project
python manage.py runserver


Running in Docker Environment

1) Ensure Docker is installed

2) Start the Docker Image
docker compose up --build 


2. Instruction for testing the app

Run the python scripts in the todoClient folder. 
The scripts contain API requests that can be used to test the Django API Server

register.py - Register new account with email, username and password
login.py - Log in to a registered account to receive access token 
logout.py - Log out of a registered account to delete access token and generate a new token
list.py - List all TODO items
create.py - Add a TODO item
update.py - Mark a TODO item as completed
delete.py - Delete a TODO item

3) API Documentation

Description: Register new account with email, username and password
Request Method: POST
URL: http://127.0.0.1:8000/accounts/register/
Body: {
    "username": "testuser", "password": "testpassword", "email": "testing@testemail.com"
}
Response: {'username': 'testuser', 'email': 'testing@testemail.com'}

Description: Log in to a registered account to receive access token 
URL: http://127.0.0.1:8000/accounts/login/
Body: {"username": "testuser", "password": "testpassword"}
Response: {'token': {token}}

Description: Log out of a registered account to delete access token and generate a new token
Request Method: POST
URL: http://127.0.0.1:8000/accounts/logout/
Headers: {"Authorization": Token {token}}
Body: {"username": "testuser", "password": "testpassword"}
Response: {'message': 'Successfully logged out.'}

Description: Retrieve list of TODO items
Request Method: GET
URL: http://127.0.0.1:8000/todo_app/todo/
Response=[
    {'pk': 1, 'item': 'Test_Item', 'isComplete': False},
    ...
]

Description: Add a TODO item
Request Method: POST
URL: http://127.0.0.1:8000/todo_app/todo/
Headers: {"Authorization": Token {token}}
Body: {"item": "Test_Item"}
Response: {'pk': 1, 'msg': 'TODO item added successfully'}

Description: Mark a TODO item as completed
Request Method: PATCH
URL: http://127.0.0.1:8000/todo_app/todo/update/{primary_key}
Headers: {"Authorization": Token {token}}
Body: {"isComplete": True}
Response: {'pk': {primary_key}, 'patched_data': {'isCompleted': True}}

Description: Delete a TODO item
Request Method: DELETE
URL: http://127.0.0.1:8000/todo_app/todo/delete/{primary_key}
Headers: {"Authorization": Token {token}}
Response: {'pk': {primary_key}, 'msg': 'TODO item deleted successfully'}