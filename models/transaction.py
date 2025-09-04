from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.connection import Base

# Model representing a transaction linking a buyer, a product, quantity purchased and the record

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey("buyers.id"), nullable=False)5
    buyer = relationship("Buyer", back_populates="transactions")
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # Relationship to easily access product object
    product = relationship("Product", back_populates="transactions")

    quantity = Column(Integer, nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id"), nullable=True)

    # Relationship to payment object
    payment = relationship("Payment", back_populates="transaction", uselist=False)

    # Timestamp when the transaction occured
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Transaction {self.id}: Buyer {self.buyer_id} bought {self.quantity} of Product {self.product_id}>"
