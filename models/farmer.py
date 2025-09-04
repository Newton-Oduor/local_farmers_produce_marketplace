from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base

# Farmer model to represent farmer in the system
class Farmer(Base):
    __tablename__ = "farmers" # Table name in the db

    # Columns = fields in the farmers table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    # Relationship to Product
    products = relationship("Product", back_populates="farmer", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"<Farmer {self.name} ({self.location} - Phone: {self.phone_number})>"
