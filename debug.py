from database.connection import session
from sqlalchemy import text

def test_connection():
    try:
        # Just run a raw SQL query to test if DB is alive
        result = session.execute(text("SELECT 1")).fetchone()
        print("✅ Database connected successfully:", result)
    except Exception as e:
        print("❌ Database connection failed:", e)

if __name__ == "__main__":
    test_connection()

from database.connection import engine, Base
from models.farmer import Farmer

def create_tables():
    Base.metadata.create_all(engine)
    print("✅ Tables created succesfully")

if __name__ == "__main__":
    create_tables()

from database.connection import Session
from models.farmer import Farmer

# Create a session (like opening a notebook for DB work)
session = Session()

try:
    # Create a new farmer object
    new_farmer = Farmer(
        name="Mary",
        location="Nairobi",
        phone_number="0712345678"
    )

    # Add farmer to the session
    session.add(new_farmer)

    # Commit (save) to the database
    session.commit()

    print(f"✅ Farmer added with ID: {new_farmer.id}")

except Exception as e:
    session.rollback()  # undo if something fails
    print(f"❌ Error adding farmer: {e}")

finally:
    session.close()
