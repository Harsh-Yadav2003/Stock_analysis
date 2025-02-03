#--------------------------Necessary imports--------------------#

from sqlalchemy import create_engine, Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import SYMBOL
import os

# -------------------------------yha database ka connection h-------------------#

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current directory
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'stocks.db')}" 
DATABASE_URL = "sqlite:///./stocks.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()

class StockData(Base):
    __tablename__ = "stock_data"
    
    date = Column(Date, primary_key=True)
    symbol = Column(String, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db  # Return Database Session
    finally:
        db.close()
