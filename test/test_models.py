# test_models.py
from database.connection import Session, Base, engine

from models.farmer import Farmer
from models.product import Product
from models.buyer import Buyer
from models.transaction import Transaction
from models.payment import Payment

# -------------------------
# Setup: create tables
# -------------------------
Base.metadata.create_all(engine)
session = Session

# -------------------------
# Simple test data
# -------------------------
def test_seed_data():
    # Clear existing data
    session.query(Payment).delete()
    session.query(Transaction).delete()
    session.query(Product).delete()
    session.query(Farmer).delete()
    session.query(Buyer).delete()
    session.commit()

    # Add farmers
    f1 = Farmer(name="John Doe", location="Nairobi", phone_number="0712345678")
    f2 = Farmer(name="Jane Smith", location="Mombasa", phone_number="0723456789")
    session.add_all([f1, f2])
    session.commit()

    # Add products
    p1 = Product(name="Tomatoes", price=50, quantity=100, farmer=f1)
    p2 = Product(name="Onions", price=80, quantity=50, farmer=f2)
    session.add_all([p1, p2])
    session.commit()

    # Add buyers
    b1 = Buyer(name="Alice", phone_number="0734567890")
    b2 = Buyer(name="Bob", phone_number="0745678901")
    session.add_all([b1, b2])
    session.commit()

    print("✅ Seed data added successfully.")

# -------------------------
# Quick verification
# -------------------------
def verify_data():
    print("\nFarmers:")
    for f in session.query(Farmer).all():
        print(f"{f.id}. {f.name} - {f.location}")

    print("\nProducts:")
    for p in session.query(Product).all():
        print(f"{p.id}. {p.name} - {p.price} KES - Qty: {p.quantity} - Farmer: {p.farmer.name}")

    print("\nBuyers:")
    for b in session.query(Buyer).all():
        print(f"{b.id}. {b.name} - {b.phone_number}")

if __name__ == "__main__":
    test_seed_data()
    verify_data()


