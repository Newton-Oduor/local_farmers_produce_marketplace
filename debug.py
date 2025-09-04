from database.connection import Session, engine, Base

# 1️⃣ Import all models BEFORE creating tables
from models.farmer import Farmer
from models.product import Product
from models.buyer import Buyer
from models.transaction import Transaction
from models.payment import Payment

# 2️⃣ Create all tables (safe if already exist)
try:
    Base.metadata.create_all(engine)
    print("✅ Tables created successfully")
except Exception as e:
    print(f"❌ Error creating tables: {e}")

# 3️⃣ Open a session
session = Session()

try:
    # 4️⃣ Add a Farmer (only if not exists)
    existing_farmer = session.query(Farmer).filter_by(name="George O").first()
    if not existing_farmer:
        farmer = Farmer(name="George O", location="Kisumu", phone_number="0799999999")
        session.add(farmer)
        session.commit()
        print(f"✅ Added farmer: {farmer}")
    else:
        farmer = existing_farmer
        print(f"ℹ️ Farmer already exists: {farmer}")

    # 5️⃣ Add a Product linked to the Farmer
    existing_product = session.query(Product).filter_by(name="Tomatoes", farmer_id=farmer.id).first()
    if not existing_product:
        product = Product(name="Tomatoes", price=50.0, quantity=100, farmer=farmer)
        session.add(product)
        session.commit()
        print(f"✅ Added product: {product}")
    else:
        product = existing_product
        print(f"ℹ️ Product already exists: {product}")

    # 6️⃣ Query: get the product and its farmer
    fetched_product = session.query(Product).first()
    print(f"\n🔎 Product '{fetched_product.name}' belongs to Farmer: {fetched_product.farmer.name}")

    # 7️⃣ Query: get the farmer and all their products
    fetched_farmer = session.query(Farmer).first()
    print(f"\n📋 Farmer {fetched_farmer.name}'s products:")
    for p in fetched_farmer.products:
        print(f"- {p.name} (Price: {p.price}, Qty: {p.quantity})")

except Exception as e:
    session.rollback()
    print(f"❌ Error adding data: {e}")

finally:
    session.close()

