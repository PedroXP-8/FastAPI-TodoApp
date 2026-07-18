from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from fastapi.testclient import TestClient
from ..models import Todos, Users
import pytest
from ..main import app
from ..routers.auth import bcrypt_context


SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread':False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'user':'coqui', 'id':1, 'user_role':'admin'}

client = TestClient(app)

@pytest.fixture
def test_todo():
    db = TestingSessionLocal()
    todo = Todos(
        title= 'learn to code',
        description= 'because its cool',
        priority=5,
        complete=False,
        owner_id=1
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)

    yield todo

    db.query(Todos).delete()
    db.commit()
    db.close()

@pytest.fixture
def test_user():
    db = TestingSessionLocal()
    user = Users(
        email= 'coqui@email.com',
        username= 'coqui',
        first_name='pedro',
        last_name='dias',
        hashed_password=bcrypt_context.hash('pedro111'),
        is_active=True,
        role='admin',
        phone_number='11937777271'
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    yield user

    db.query(Users).delete()
    db.commit()
    db.close()