from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

# Model representing a transaction linking a buyer, a product, quantity purchased and the record

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey("buyers.id"), nullable=False)
    
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    # Relationship to easily access product object
    product = relationship("Product", back_populates="transactions")

    
    payment_id = Column(Integer, ForeignKey("payments.id"), nullable=True)

    # Relationships
    buyer = relationship("Buyer", back_populates="transactions")
    product = relationship("Product", back_populates="transactions")
    payment = relationship("Payment", back_populates="transaction")

    def __repr__(self):
        return f"<Transaction {self.id}: Buyer {self.buyer_id}, Product {self.product_id}, Quantity {self.quantity}>"
