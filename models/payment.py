from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.connection import Base

# Model representing a payment linked to a transaction

class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False) # Payment amount
    status = Column(String, default="Pending") # Payment status
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship to the transaction
    transaction = relationship("Transaction", back_populates="payment", uselist=False)

    def __repr__(self):
         return f"<Payment {self.id}: {self.status} - Amount: {self.amount}>" 