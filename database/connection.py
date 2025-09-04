# import tools from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create db engine (Bridge to the sqlite db file)
engine = create_engine('sqlite:///farmers_market.db')

# Create a base class (superclass) for our models to inherit from (farmers, product, customer)
Base = declarative_base()

# Create a session maker (what we will use to talk to the db like add, query, delete)
Session = sessionmaker(bind=engine)
session = Session()
