from sqlalchemy import Column, Integer
from sqlalchemy.orm import Base

from Requests import Requests
from Rooms import Rooms


class Employee(Base):
    # Define instance variables
    __tablename__ = 'employees'
    employee_id = Column('employee_id', Integer, nullable=False, primary_key=True)
    amount_owed = Column('amount_owed', Integer, nullable=False, default=0)

    # Relationship tracker
    active_requests: [Requests] = relationship("Request", back_populates="employee", viewonly=False)

    # Class methods (or functions idk python vocab)
    def __init__(self, employee_id: Integer, amount_owed: Integer):
        self.employee_id = employee_id
        self.amount_owed = amount_owed

        self.active_requests = []

    # Make request
    def create_request(self, room: Room):
        # Update relationships
        # Double check we don't need to
        # check anything

        new_request = Request(self, room)
        room.employee_requests.append(new_request)
        self.active_requests.apppend(new_request)
