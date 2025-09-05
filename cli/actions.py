from database.connection import Session
from models.farmer import Farmer
from models.product import Product
from models.buyer import Buyer
from models.transaction import Transaction
from models.payment import Payment

# A database session to interact with SQLite
session = Session()

# -------------------------
# Farmer related functions
# -------------------------

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

# Deletes farmer along with all their products by ID
def delete_farmer():
    view_farmers()
    farmer_id = int(input("Enter the ID of the farmer to delete: "))
    farmer = session.query(Farmer).get(farmer_id)
    if not farmer:
        print("Farmer not found!")
        return
    session.delete(farmer)

    try:
        session.commit()
        print(f"farmer {farmer.name} deleted successfully")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

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

    print("Select a farmer by ID:")
    for f in farmers:
        print(f"{f.id}. {f.name}")
    farmer_id = int(input("> "))
    farmer = session.query(Farmer).get(farmer_id)
    if not farmer:
        print("Farmer not found!")
        return

    # Prevent adding the same product twice for this farmer
    existing = session.query(Product).filter_by(name=name, farmer_id=farmer_id).first()
    if existing:
        print(f"{farmer.name} already has a product called '{name}'.")
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
def view_products():
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
        print("Farmer not found!")
        return
    if not farmer.products:
        print(f"{farmer.name} has no products.")

    print(f"Products by {farmer.name}:")
    for p in farmer.products:
        print(f"- {p.name} (Price: {p.price}, qty: {p.quantity})")

# Delete a product by ID
def delete_product():
    view_products()
    product_id = int(input("Enter the ID of the product to delete: "))
    product = session.query(Product).get(product_id)
    if not product:
        print("Product not found!")
        return
    session.delete(product)

    try:
        session.commit()
        print(f"Product {product.name} deleted successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")


# -------------------------
# Buyer urelated functions
# -------------------------

# Register a new buyer
def add_buyer():
    name = input("Buyer name: ")
    phone = input("Phone number: ")

    # Check if buyer exists
    existing = session.query(Buyer).filter_by(name=name, phone_number=phone).first()
    if existing:
        print(f"Buyer already exists: {existing}")
        return
    
    buyer = Buyer(name=name, phone_number=phone)
    session.add(buyer)
    
    try:
        session.commit()
        print(f"Added buyer: {buyer}")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

# Soft delete a buyer
def delete_buyer():
    buyers = session.query(Buyer).all()
    if not buyers:
        print("No buyers found.")
        return
    
    print("Select a buyer by ID to delete:")
    for b in buyers:
        status = " (Deleted)" if not b.is_active else ""
        print(f"{b.id}. {b.name}{status} - Phone: {b.phone_number}")

    try:
        buyer_id = int(input("> "))
        buyer = session.query(Buyer).get(buyer_id)
        if not buyer:
            print("Buyer not found!")
            return

        # Delete associated transaction
        buyer.is_active = False
        session.commit()
        print(f"✅ Buyer {buyer_id} marked as deleted.")

    except Exception  as e:
        session.rollback()
        print(f"Error deleting buyer: {e}")


# -------------------------
# Search products functions
# -------------------------

def search_products():
    term = input("Enter product name to search (leave blank to view all): ").strip()

    if term:
        products = session.query(Product).filter(Product.name.ilike(f"%{term}%")).all()
    else:
        products = session.query(Product).all()

    if not products:
        print("No products found")
        return

    print("\nProducts:")  
    for p in products:
        print(f"{p.id}. {p.name} - Price: {p.price}, Qty: {p.quantity}, Farmer: {p.farmer.name}")    



# -------------------------
# payment related function
# -------------------------

# Purchase a product
def purchase_product():

    # List buyers
    buyers = session.query(Buyer).filter_by(is_active=True).all()
    if not buyers:
        print("No buyers found. Please register a buyer first.")
        return
    
    print("\nSelect Buyer:")
    for b in buyers:
        print(f"{b.id}. {b.name} - Phone: {b.phone_number}")
    buyer_id = int(input("> "))
    buyer = session.query(Buyer).get(buyer_id)
    if not buyer or not buyer.is_active:
        print("Invalid buyer selected.")
        return
    
    # List products
    products = session.query(Product).all()
    if not products:
        print("No products available.")
        return
    
    print("\nSelect Product:")
    for p in products:
        print(f"{p.id}. {p.name} - Price: {p.price}, Qty: {p.quantity}, Farmer: {p.farmer.name}")
    product_id = int(input("> "))
    product = session.query(Product).get(product_id)
    if not product or product.quantity <= 0:
        print("Invalid or out-of-stock product selected.")
        return
    

    # Ask for quantity
    qty = int(input("Enter quantity: "))
    if qty <= 0 or qty > product.quantity:
        print("Invalid quantity.")
        return
    
    total_price = product.price * qty


    # Reduce stock
    product.quantity -= qty

    # Create transaction
    transaction = Transaction(buyer=buyer, product=product, quantity=qty)
    session.add(transaction)
    session.commit()

    print(f"Transaction created: {buyer.name} bought {qty} {product.name}(s) for {total_price}")


    # Process payment
    process_payment(transaction, total_price)
    session.commit()



# Payment simulation function
def process_payment(transaction, amount):
    print(f"\nM-Pesa Payment Simulation for KES {amount}")
    code = input("Enter M-Pesa confirmation code (or leave blank to fail): ")

    status = "Completed" if code else "Failed"

    payment = Payment(amount=amount, status=status, transaction=transaction)
    session.add(payment)

    print(f"✅ Payment recorded: {status} (Transaction {transaction.id})")
