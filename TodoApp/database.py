from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

###SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/TodoApplicationDataBase'###
SQLALCHEMY_DATABASE_URL = 'postgresql://ph_production_postgresql_user:3nFlOX9OYAAm69wKbbXDhKYa5H8XX5uR@dpg-d9dv1pjrjlhs73bdo1k0-a/ph_production_postgresql'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()