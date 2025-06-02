from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.car import Base

# Create the database engine (using SQLite for simplicity)
engine = create_engine('sqlite:///cars.db', echo=False) 

# Create database tables (execute once to set up the schema)
Base.metadata.create_all(engine)

# Create a session factory to interact with the database
SessionLocal = sessionmaker(bind=engine)
