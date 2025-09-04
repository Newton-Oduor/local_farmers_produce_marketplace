from database.connection import Session
from models.farmer import Farmer
from models.product import Product

# A database session to interact with SQLite
session = session()

# ------------------------
# Farmer related functions
# ------------------------

# Adds new farmer to db
def add_farmer():
    name = input("Farmer name: ")
    location = input("Location: ")
    phone = input("Phone number: ")

    farmer = Farmer(name=name, location=location, phone_number=phone)
    session.add(farmer)

    try:
        session.commit() # Save changes
        print(f"Added farmer: {farmer}")
    except Exception as e:
        session.rollback() # Undo if error occurs
        print(f"Error: {e}")

# Display all farmers
def view_farmers():
    farmers = session.query(Farmer).all()
    if not farmers:
        print("No farmers found.")
        return
    for f in farmers:
        print(f"{f.id}. {f.name} ({f.location}) - phone: {f.phone_number}")

# -------------------------
# Product related functions
# -------------------------

# Adds a new product and associates it with a farmer
def add_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    # Show list of farmers to associate
    farmers = session.query(Farmer).all()
    if not farmers:
        print("No farmers found. Add a farmer first!")
        return

    print("Selevt a farmer by ID:")
    for f in farmers:
        print(f"{f.id}. {f,name}")
    farmer_id = int(input("> "))
    farmer = session.query(Farmer).get(farmer_id)
    if not farmer:
        print("Farmer not found!")
        return

    product = Product(name=name, price=price, quantity=quantity, farmer=farmer)
    session.add(product)

    try:
        session.commit()
        print(f"Added product: {product}")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

# Displays all products
def view products():
    products = session.query(Product).all()
    if not products:
        print("No products found.")
        return
    for p in products:
        print(f"{p.id}. {p.name} - Price: {p.price}, Qty: {p.quantity}, Farmer: {p.farmer.name}")

# Display products belonging to a specific farmer
def view_products_by_farmer():
    farmers = session.query(Farmer).all()
    if not farmers:
        print("No farmers found.")
        return

    print("Select a farmer by ID:")
    for f in farmers:
        print(f"{f.id}. {f.name}")
    farmer_id = int(input("> "))
    farmer = session.query(Farmer).get(farmer_id)
    if not farmer:
        print(f"{farmer.name} has no products.")
        return

    print(f"Products by {farmer.name}:")
    for p in farmer.products:
        print(f"- {p.name} (Price: {p.price}, qty: {p.quantity})")

# ------------------------
# payment placeholder
# ------------------------

# Payment function
def process_payment():
    pass
