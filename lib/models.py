from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Asset(Base):
    __tablename__ = 'assets'
    
    id = Column(String, primary_key=True)
    name = Column(String)
    location = Column(String)
    date_taken = Column(Date, nullable=True)
    return_date = Column(Date, nullable=True)

class Staff(Base):
    __tablename__ = 'staff'
    
    id = Column(String, primary_key=True)
    name = Column(String)