from sqlalchemy import Column, String, Integer, Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

#Import relational classes
from Doors import Doors
from Requests import Requests

class Rooms(Base):
    __tablename__ = 'rooms'
    room_number = Column('room_number', Integer, nullable=False, primary_key=True)

    # Relationships
    doors_list: [Doors] = relationship("Doors", back_populates="room", viewonly=False)
    requests_for_room: [Requests] = relationship("Requests", back_populates="room", viewonly=False)

    def __init__(self, room_number):
        self.room_number = room_number
        self.doors_list = []
        self.requests_for_room = []

    def add_door(self, door: Door):
        #Check for dupes
        for test_door in self.doors_list:
            if test_door == door:
                return

        #Create new instance of child Door
        instance = Door(self)
        door.rooms
