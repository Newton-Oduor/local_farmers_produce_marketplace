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
