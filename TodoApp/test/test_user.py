from .utils import *
from fastapi import status
from ..models import Users
from ..routers.user import get_db, get_current_user


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_user(test_user):
    response = client.get('/user/user')

    assert response.status_code == status.HTTP_200_OK

    assert response.json()['username'] == 'coqui'

def test_change_password_success(test_user):
    change_password_request = {
        'old_password':'pedro111',
        'new_password':'pedro222'
    }

    response = client.put('/user/update_user_password', json=change_password_request)
    
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid(test_user):
    change_password_request = {
        'old_password':'pedro000',
        'new_password':'pedro222'
    }

    response = client.put('/user/update_user_password', json=change_password_request)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password change'}
    
def test_change_phone_number_success(test_user):
    change_phone_number_request = {
        'password':'pedro111',
        'new_phone_number':'11969186090'
    }

    response = client.put('/user/update_user_phone_number', json=change_phone_number_request)
    
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_phone_number_invalid(test_user):
    change_phone_number_request = {
        'password':'pedro000',
        'new_phone_number':'11969186090'
    }

    response = client.put('/user/update_user_phone_number', json=change_phone_number_request)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail':'Error on password'}