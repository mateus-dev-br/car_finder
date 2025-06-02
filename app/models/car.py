from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Car(Base):
    """
    Car model representing a vehicle in the database.
    """
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    engine = Column(String(50))
    fuel_type = Column(String(20))
    transmission = Column(String(20))
    doors = Column(Integer)
    color = Column(String(30))
    mileage = Column(Float)
    price = Column(Float)

    def __repr__(self):
        return (
            f"<Car({self.brand} {self.model} {self.year} - "
            f"{self.color} - {self.mileage}km - R${self.price:.2f})>"
        )
