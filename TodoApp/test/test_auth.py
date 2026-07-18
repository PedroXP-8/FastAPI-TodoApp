from .utils import *
from fastapi import status, HTTPException
from ..routers.auth import get_db, get_current_user,\
    authenticated_user, SECRET_KEY, ALGORITHM, create_access_token
from jose import jwt 
from datetime import timedelta
import pytest


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_authentication(test_user):

    db = TestingSessionLocal()

    authenticate_user = authenticated_user(test_user.username, 'pedro111', db)
    assert authenticate_user is not None
    assert authenticate_user.username == 'coqui'

    non_authenticated_user = authenticated_user('canjica', 'pedro111', db)
    assert non_authenticated_user is False

    wrong_password = authenticated_user(test_user.username, 'pedrobó', db)
    assert wrong_password is False

def test_create_access_token():
    username = 'nome'
    user_id = 1
    role = 'user'
    expires_time = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_time)

    decoded_token = jwt.decode(token,  SECRET_KEY, algorithms=[ALGORITHM],
                         options={'verify_signature':False})
    
    assert decoded_token.get('sub') == username
    assert decoded_token.get('id') == user_id
    assert decoded_token.get('role') == role

@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {'sub':'coqui', 'id':1, 'role':'admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    user = await get_current_user(token=token)
    assert user == {'username':'coqui', 'id':1, 'user_role':'admin'}

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role':'admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)

    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate users'