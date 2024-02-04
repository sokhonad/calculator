from sqlalchemy import create_engine, Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String(255), index=True) 
    result = Column(Float)

def create_database():
    engine = create_engine("mysql+mysqlconnector://root:sokh@db:3306/calculator_bd")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionLocal = create_database()
