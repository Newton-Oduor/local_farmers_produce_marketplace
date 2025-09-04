from database.connection import Session, engine, Base

# 1️⃣ Import all models BEFORE creating tables
from models.farmer import Farmer
from models.product import Product

# 2️⃣ Create all tables
try:
    Base.metadata.create_all(engine)
    print("✅ Tables created successfully")
except Exception as e:
    print(f"❌ Error creating tables: {e}")

# 3️⃣ Open a session
session = Session()

try:
    # 4️⃣ Add a Farmer
    farmer = Farmer(name="George O", location="Kisumu", phone_number="0799999999")
    session.add(farmer)
    session.commit()
    print(f"✅ Added farmer: {farmer}")

    # 5️⃣ Add a Product linked to the Farmer
    product = Product(name="Tomatoes", price=50.0, quantity=100, farmer=farmer)
    session.add(product)
    session.commit()
    print(f"✅ Added product: {product}")

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
