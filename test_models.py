from database.connection import Session, Base, engine

# Import all models BEFORE creating tables
from models.farmer import Farmer
from models.product import Product
from models.buyer import Buyer
from models.transaction import Transaction
from models.payment import Payment

# Create all tables (safe if they already exist)
Base.metadata.create_all(engine)

# Open a session
session = Session()

try:
    print("\n--- TESTING MODELS ---\n")

    # 1️⃣ Test Farmer
    farmer = session.query(Farmer).filter_by(name="Alice Farmer").first()
    if not farmer:
        farmer = Farmer(name="Alice Farmer", location="Nairobi", phone_number="0711111111")
        session.add(farmer)
        session.commit()
        print(f"✅ Added Farmer: {farmer}")
    else:
        print(f"ℹ️ Farmer already exists: {farmer}")

    # 2️⃣ Test Product
    product = session.query(Product).filter_by(name="Onions", farmer_id=farmer.id).first()
    if not product:
        product = Product(name="Onions", price=30.0, quantity=50, farmer=farmer)
        session.add(product)
        session.commit()
        print(f"✅ Added Product: {product}")
    else:
        print(f"ℹ️ Product already exists: {product}")

    # 3️⃣ Test Buyer
    buyer = session.query(Buyer).filter_by(name="Bob Buyer").first()
    if not buyer:
        buyer = Buyer(name="Bob Buyer", phone_number="0722222222")
        session.add(buyer)
        session.commit()
        print(f"✅ Added Buyer: {buyer}")
    else:
        print(f"ℹ️ Buyer already exists: {buyer}")

    # 4️⃣ Test Payment
    payment = session.query(Payment).filter_by(amount=30.0, status="Pending").first()
    if not payment:
        payment = Payment(amount=30.0, status="Pending")
        session.add(payment)
        session.commit()
        print(f"✅ Added Payment: {payment}")
    else:
        print(f"ℹ️ Payment already exists: {payment}")

    # 5️⃣ Test Transaction
    transaction = session.query(Transaction).filter_by(buyer_id=buyer.id, product_id=product.id).first()
    if not transaction:
        transaction = Transaction(
            buyer=buyer,
            product=product,
            quantity=2,
            payment=payment
        )
        session.add(transaction)
        session.commit()
        print(f"✅ Added Transaction: {transaction}")
    else:
        print(f"ℹ️ Transaction already exists: {transaction}")

    # 6️⃣ Verify relationships
    print(f"\n🔎 Farmer {farmer.name} products:")
    for p in farmer.products:
        print(f"- {p.name} (Qty: {p.quantity})")

    print(f"\n🔎 Buyer {buyer.name} transactions:")
    for t in buyer.transactions:
        print(f"- Bought {t.quantity} of {t.product.name}, Payment Status: {t.payment.status}")

    print(f"\n🔎 Product {product.name} transactions:")
    for t in product.transactions:
        print(f"- Bought by {t.buyer.name}, Payment Status: {t.payment.status}")

except Exception as e:
    session.rollback()
    print(f"❌ Error during testing: {e}")

finally:
    session.close()
    print("\n--- TESTING COMPLETED ---")

