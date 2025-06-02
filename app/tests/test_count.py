from app.db.database import SessionLocal
from app.models.car import Car

def test_database_count():
    session = SessionLocal()
    count = session.query(Car).count()
    session.close()
    
    assert count >= 100
