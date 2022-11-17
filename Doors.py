from sqlalchemy import Column, String, Integer, Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Rooms import Rooms

class Doors(Base):
    __tablename__ = 'Doors'
    # Define Variables
    # Relationships
    # Instance Methods
    def __init__(self, room: Room, door_name: String):
        self.room = room
        self.room_number = self.room.room_number
        # room doesn't look like a real word anymore
        self.door_name = door_name
