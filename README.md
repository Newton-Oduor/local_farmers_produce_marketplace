# Local Farmers Produce Marketplace (LFPM)

## Project Overview

LFPM is a Python-based command-line interface (CLI) application that simulates a local farmers’ marketplace. Farmers can list produce, buyers can browse and purchase items, and the system records transactions and payments. This project demonstrates CRUD operations, relational database management using SQLAlchemy, and basic reporting.

It also simulates an M-Pesa-style payment confirmation for purchases, allowing for testing transaction flows in a realistic way.

---

## Problem Statement

In many African countries, small-scale farmers are the backbone of food production. However, they face serious challenges in accessing markets, including:

1. Reliance on middlemen who buy at low prices and sell at high margins.
2. Limited access to digital platforms where they can showcase their produce.
3. Lack of structured systems to connect directly with local buyers (shops, households, restaurants).

This results in reduced income for farmers and higher food costs for buyers.

---

## Solution Statement

The proposed solution is a Python-based CLI Marketplace Application that connects farmers and buyers directly:

1. **Farmers** can register and list produce (name, price, and quantity).
2. **Buyers** can search, compare, and purchase directly from farmers.
3. The system records transactions, manages stock updates, and provides a fair-trade platform. This ensures fair pricing for farmers, affordable produce for buyers, and a transparent local marketplace.

---

## Project Features

### 1. Farmer Registration & Produce Listing
- Farmers create profiles and list available produce with details such as name, quantity, and unit price.
- Each produce entry is linked to the farmer for traceability.
- Farmers can view sales and stock reports, giving insight into product performance.

### 2. Buyer Registration & Produce Search
- Buyers can register in the system and maintain a profile.
- Buyers can search available produce by type (e.g., maize, beans, tomatoes) and filter by price or availability.
- Buyers can view detailed information about each product including price, quantity, and seller details.

### 3. Transaction Management (Purchases & Stock Update)
- The system automatically updates stock levels after each purchase.
- Transactions are recorded, linking buyers, products, and quantity purchased.
- Transaction history is available for both buyers and farmers.

### 4. Price Transparency & Fair Trade
- Farmers set their own prices, avoiding exploitative middlemen.
- Buyers see exact prices, quantities, and seller details.
- Promotes transparency and trust in the local food supply chain.

### 5. Payment Simulation
- M-Pesa-style payment simulation allows entering a confirmation code to mark a transaction as completed.
- Failed transactions are also recorded for accuracy in reporting.

### 6. Reporting
- Buyers can view all past purchases, including product details, total price, and purchase date.
- Farmers can view sales reports showing sold quantities, remaining stock, and total revenue.

---

## Folder Structure

```pgsql

local_farmers_produce_marketplace/
│
├── cli/
│   ├── __init__.py
│   ├── actions.py       # All CLI actions (add/view/delete, purchase, reports)
│   └── menu.py          # Menu interface and input handling
│
├── database/
│   ├── __init__.py
│   └── connection.py    # SQLAlchemy engine, session, and Base
│
├── models/
│   ├── __init__.py
│   ├── buyer.py
│   ├── farmer.py
│   ├── payment.py
│   ├── product.py
│   └── transaction.py
│
├── app.py               # Main entry point for running the CLI
├── farmers_market.db    # SQLite database file
├── README.md
├── Pipfile
└── Pipfile.lock
```

---

## Project Setup

1. Clone the repository:

```bash
git clone https://github.com/Newton-Oduor/local_farmers_produce_marketplace
cd local_farmers_produce_marketplace
```

2. Install dependencies:

```bash
pipenv install
pipenv shell
```

3. Run the CLI app:
```bash
python app.py
```

## Database
- SQLite database farmers_market.db is used.
- Tables: farmers, buyers, products, transactions, payments.
- SQLAlchemy ORM manages models and relationships.
- Tabulate is used for clean CLI table displays.

## Technologies Used
Python, SQLite, SQLAlchemy & CLI interface.

---

## Future Improvements
- Buyers place orders through the CLI.
- Web Interface
- Real payment intergration 
- Reporting dashboards

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- Special thanks to Moringa School Instructors & Flatiron School for the project guidelines.

Author [Newton Oduor](https://github.com/Newton-Oduor/local_farmers_produce_marketplace)



