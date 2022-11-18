from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import Base
from datetime import date

from Employees import Employees
from Doors import Doors
from Issued_Keys import IssuedKeys # For later :)

class Request(Base):
    # Define instance variables
    employee_id = Column('employee_id', Integer, ForeignKey('employees.employee_id') nullable=False, primary_key=True)
    room_number = Column('room_number', Integer, ForeignKey('rooms.room_number') nullable=False, primary_key=True)
    request_date = Column('request_date', Date, nullable=False, primary_key=True)
    approval_date = Column('approval_date', Date, nullable=True)

    # Relationship tracker
    employee = relationship("Employee", back_populates="active_requests")
    room_requested = relationship("Room", back_populates="employee_requests")
    issued_key = relationship("Issued_Key", back_populates="request")


    # Class methods
    def __init__(self, employee: Employee, room: Room):
        # Relationship variables
        self.employee = employee
        self.room_requested = room

        # Table variables
        self.employee_id = self.employee.employee_id
        self.room_number = self.room.room_number
        # Check the strftime() works w/ DDL
        self.request_date = date.today().strftime("%Y-%m-%d")
        self.approval_date = None
        # self.approval_date = NULL

    def approve_request(self):
        # Approval logic here!
