from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import date

from Requests import Request
from Keys import Key

class IssuedKey(Base):
    __tablename__ = 'issued_keys'

    # Define instance Variables
    employee_id = Column(Integer, nullable=False, primary_key=True)
    hook_id = Column(Integer, nullable=False, primary_key=True)
    approved_room = Column(Integer, nullable=False, primary_key=True)

    requested_room = Column(Integer, nullable=False)
    door_name = Column(String, nullable=False)
    request_date = Column(Date, nullable=False)

    issued_date = Column('issued_date', Date, nullable=False)
    return_date = Column('return_date', Date, nullable=False)
    date_returned = Column('date_returned', Date, nullable=True)
    is_valid = Column('is_valid', Boolean, nullable=False)

    __table_args__ = ForeignKeyConstraint([employee_id, hook_id, approved_room, requested_room, door_name, request_date],
                                          [Request.employee_id, Key.hook_id, Key.room_number, Request.room_number, Key.door_name, Request.request_date])

    # Relationship tracker
    request: Request = relationship("Request", back_populates="issued_key")
    key: Key = relationship("Key", back_populates="issued_key")

    # Class Methods
    def __init__(self, request: Request, key: Key):
        self.request = request
        self.key = key

        # Primary Key Collection
        self.employee_id = self.request.employee_id
        self.hook_id = self.key.hook_id
        self.approved_room = self.key.room_number

        self.requested_room = self.request.room_number
        self.door_name = self.key.door_name
        today = date.today()
        self.issued_date = today.strftime("%Y-%m-%d")
        self.return_date = date(today.year + 1, today.month + 16, today.day)
        self.date_returned = None
        self.is_valid = True
        self.return_date = self.request.request_date



