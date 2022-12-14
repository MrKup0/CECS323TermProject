from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Keys import Key

class Door(Base):
    __tablename__ = 'doors'
    # Define Variables
    room_number = Column(Integer, ForeignKey('rooms.room_number'), nullable=False, primary_key=True)
    door_name = Column('door_name', String, nullable=False, primary_key=True)
    # Relationships
    room = relationship("Room", back_populates='doors_list', viewonly=False)
    keys_list: [Key] = relationship("Key", back_populates='door', viewonly=False)
    # Instance Methods
    def __init__(self, room, door_name: String):
        self.room = room
        self.room_number = self.room.room_number
        # room doesn't look like a real word anymore
        self.door_name = door_name
        self.keys_list = []

    def add_key(self, key):
        for i in self.keys_list:
            if i == key:
                return
        self.keys_list.append(key)