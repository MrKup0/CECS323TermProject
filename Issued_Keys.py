from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Requests import Request
from Keys import Key

class IssuedKey(Base):
    __tablename__ = 'issued_keys'

    # Define instance Variables
    employee_id = Column(Integer, ForeignKey('requests.employee_id'), nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('keys.hook_id'), nullable=False, primary_key=True )
    requested_room = Column(Integer, ForeignKey('requests.room_number'), nullable=False)
    approved_room = Column(Integer, ForeignKey('keys.room_number'), nullable=False, primary_key=True)
    door_name = Column(String, ForeignKey('keys.door_name'), nullable=False)
    issued_date = Column('issued_date', Date, nullable=False)
    return_date = Column('return_date', Date, nullable=False)
    date_returned = Column('date_returned', Date, nullable=True)
    is_valid = Column('is_valid', Boolean, nullable=False)
    request_date = Column(Date, ForeignKey('requests.request_date'), nullable=False)

    # Relationship tracker
    request: Request = relationship("Request", back_populates="issued_key")
    key: Key = relationship("Key", back_populates="")

    # Class Methods

