from sqlalchemy import Column, Integer, String
from database.connection import Base

# Buyers can purchase products and have transactions linked to them

class Buyer(Base):

    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)


    def __repr__(self):
        return f"<Buyer {self.name} (Phone: {self.phone_number})>"
