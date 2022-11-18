from sqlalchemy import Column, String, Integer, Identity
from sqlalchemy.orm import relationship
from orm_base import Base

from Hooks import Hooks
from Doors import Doors

class Keys(Base):
    # Instance Variables
    hook_id = Column(Integer, ForeignKey("hooks.hooks"), nullable=False, primary_key=True)
    room_number = Column(Integer, ForeignKey("doors.room_number"), nullable=False, primary_key=True)
    door_name = Column(String, ForeignKey("doors.door_name"), nullable=False, primary_key=True)
    # Relationships
    door = relationships("Door", back_populates='keys_list')
    hook = relationships("Hook", back_populates='keys_list')
    # Class methods
    def __init__(self, door: Door, hook: Hook):
        self.door = door
        self.hook = hook

        self.hook_id = self.hook.hook_id
        self.room_number = self.door.room_number
        self.door_name = self.door.door_name

    def add_key(self, opening_door: Doors, hook: Hooks):
        
