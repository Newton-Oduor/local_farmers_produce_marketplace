from sqlalchemy import Column, Integer, String
from database.connection import Base

# Farmer model to represent farmer in the system
class Farmer(Base):
    __tablename__ = "farmers" # Table name in the db

    # Columns = fields in the farmers table
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    phone_number = Column(String, unique=True)

    def __repr__(self):
        return f"<Farmer id={self.id} name={self.name} location={self.location}>"
