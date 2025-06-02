import logging
from random import choice, randint, uniform
from faker import Faker
from app.db.database import SessionLocal
from app.models.car import Car
from constants import brands_models, fuel_types, transmissions, colors

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

fake = Faker()

def create_fake_car() -> Car:
    """Generate a fake Car instance with realistic attributes."""
    brand = choice(list(brands_models.keys()))
    model = choice(brands_models[brand])
    return Car(
        brand=brand,
        model=model,
        year=randint(2000, 2023),
        engine=f"{uniform(1.0, 3.5):.1f}L",
        fuel_type=choice(fuel_types),
        color=choice(colors),
        mileage=round(uniform(0, 200000), 1),
        doors=choice([2, 4]),
        transmission=choice(transmissions),
        price=round(uniform(20000, 200000), 2)
    )

def seed_database(n: int = 100) -> None:
    """Populate the database with n fake cars."""
    session = SessionLocal()
    try:
        session.query(Car).delete()
        session.commit()

        logger.info(f"Inserting {n} vehicles into the database...")
        for _ in range(n):
            session.add(create_fake_car())
        session.commit()
        logger.info("Done! Vehicles successfully inserted.")
    except Exception as e:
        session.rollback()
        logger.error("Failed to seed the database.", exc_info=True)
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()
