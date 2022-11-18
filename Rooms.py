from sqlalchemy import Column, String, Integer, Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

# Import relational classes
from Doors import Door
from Requests import Request

class Room(Base):
    __tablename__ = 'rooms'
    room_number = Column('room_number', Integer, nullable=False, primary_key=True)

    # Relationships
    doors_list: [Door] = relationship("Doors", back_populates="room", viewonly=False)
    employee_requests: [Request] = relationship("Requests", back_populates="room_requested", viewonly=False)

    def __init__(self, room_number: Integer):
        self.room_number = room_number
        self.doors_list = []
        self.employee_requests = []

    def add_door_str(self, door_name):
        # Check for dupe doors
        for i in self.doors_list:
            if i.door_name == door_name:
                print("Failed to add door: " + door_name + "\nDoor " + i.door_name + " already exists for room "+ self.room_number)
                return

        # Create door
        new_door = Door(self, door_name)
        self.doors_list.append(new_door)

    def add_request(self, request: Request):
        # Each room can have several requests
        # no need to check for dupes
        self.employee_requests.append(request)
