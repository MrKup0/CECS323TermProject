from sqlalchemy import Column, Integer, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import date

from Issued_Keys import IssuedKey


class Request(Base):
    __tablename__ = 'requests'
    # Define instance variables
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False, primary_key=True)
    room_number = Column(Integer, ForeignKey('rooms.room_number') ,nullable=False, primary_key=True)
    request_date = Column('request_date', Date, nullable=False, primary_key=True)
    approval_date = Column('approval_date', Date, nullable=True)

    __table_args__ = (UniqueConstraint('employee_id', 'room_number'),)

    # Relationship tracker
    employee = relationship("Employee", back_populates="active_requests", viewonly=False)
    room_requested = relationship("Room", back_populates="employee_requests", viewonly=False)
    issued_key: IssuedKey = relationship("IssuedKey", back_populates="request", viewonly=False)

    # Class methods
    def __init__(self, employee, room):
        # Relationship variables
        self.employee = employee
        self.room_requested = room

        # Table variables
        self.employee_id = self.employee.employee_id
        self.room_number = self.room.room_number
        self.request_date = date.today()
        self.approval_date = None
