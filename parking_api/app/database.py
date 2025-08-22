#Isso vai conectar ao postgreSQL


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1324@localhost/parking_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL) #Ligacao com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() #Classe base para criar tabelas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db .close    