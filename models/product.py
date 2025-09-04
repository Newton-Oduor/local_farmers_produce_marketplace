from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False) # e.g maize, tomatoes
    price = Column(Float, nullable=False) # price per unit e.g per kg
    quantity = Column(Integer, nullable=False) # Stock available

    farmer_id = Column(Integer, ForeignKey("farmers.id"), nullable=False) # Links products to a farmer

    # Relationship back to farmer (string avoids circular import)
    farmer = relationship("Farmer", back_populates="products") # Product linked to the farmer model and vice versa

    transactions = relationship("Transaction", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name} (Farmer ID: {self.farmer_id})>"
