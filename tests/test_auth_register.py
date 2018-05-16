
import random, string, uuid
from werkzeug.security import generate_password_hash

from app.db import db
from app.db import User
from database_populator import DatabasePopulator

def test_register_returns_rtatus_code_201_with_msg_when_unique_username_and_password_is_passed(client):

    username = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    hashed_password = generate_password_hash("secret", method='sha256')

    response = client.post('/auth/register', json={
        'username': username, 
        'password': hashed_password
    })
    result = response.get_json()
    assert response.status_code == 201    
    assert result['message'] == "User successfully created." 


def test_register_returns_status_code_400_with_msg_when_only_username_is_passed(client):

    username = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])

    response = client.post('/auth/register', json={
        'username': username        
    })
    result = response.get_json()
    assert response.status_code == 400
    assert result['message'] == "Username or Password field not provided." 


def test_register_returns_status_code_400_with_msg_when_only_password_is_passed(client):

    hashed_password = generate_password_hash("secret", method='sha256')

    response = client.post('/auth/register', json={
        'password': hashed_password
    })
    result = response.get_json()
    assert response.status_code == 400
    assert result['message'] == "Username or Password field not provided."     


def test_register_returns_status_code_400_with_msg_when_username_and_password_is_not_passed(client):

    response = client.post('/auth/register', json={})
    result = response.get_json()
    assert response.status_code == 400
    assert result['message'] == "Username or Password field not provided."     
    

def test_register_returns_status_code_400_with_msg_when_only_username_is_passed_with_empty_string(client):    

    response = client.post('/auth/register', json={'username': ''})
    result = response.get_json()
    assert response.status_code == 400
    assert result['message'] == "Username or Password field not provided."         


def test_register_returns_status_code_400_with_msg_when_only_password_is_passed_with_empty_string(client):    

    response = client.post('/auth/register', json={'password': ''})
    result = response.get_json()
    assert response.status_code == 400
    assert result['message'] == "Username or Password field not provided."             


def test_register_returns_status_code_400_with_msg_when_username_and_password_is_passed_with_empty_strings(client):    

    response = client.post('/auth/register', json={'username': '', 'password': ''})
    result = response.get_json()
    assert response.status_code == 400
    assert result['message'] == "Username or Password field not provided."                 


def test_register_returns_status_code_409_with_msg_when_already_existing_username_with_password_is_passed(client):    

    DatabasePopulator.populate()

    response = client.post('/auth/register', json={'username': 'tester1', 'password': 'secret'})
    result = response.get_json()
    assert response.status_code == 409
    assert result['message'] == "Username already exist."