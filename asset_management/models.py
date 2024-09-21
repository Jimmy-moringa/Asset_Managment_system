# asset_management/models.py

from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Asset(Base):
    __tablename__ = 'assets'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    date_taken = Column(Date)
    return_date = Column(Date)

class Staff(Base):
    __tablename__ = 'staff'
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    assets = relationship("AssetAssignment", back_populates="staff")

class AssetAssignment(Base):
    __tablename__ = 'asset_assignments'
    
    id = Column(String, primary_key=True)
    staff_id = Column(String, ForeignKey('staff.id'))
    asset_id = Column(String, ForeignKey('assets.id'))
    date_taken = Column(Date)
    return_date = Column(Date)

    staff = relationship("Staff", back_populates="assets")
