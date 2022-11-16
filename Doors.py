from sqlalchemy import Column, String, Integer, Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Rooms import Rooms

class Doors(Base):
    __tablename__ = 'Doors'
    # Define Variables
    
