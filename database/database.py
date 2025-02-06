# database/database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///spiderpulse.db"  # Change to MySQL/PostgreSQL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(engine)

def save_to_db(data):
    session = SessionLocal()
    for item in data:
        session.add(Product(name=item["name"]))
    session.commit()
    session.close()