from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Hooks import Hook
from Doors import Door
from Issued_Keys import IssuedKey

class Key(Base):
    __tablename__ = 'keys'
    # Instance Variables
    hook_id = Column(Integer, ForeignKey("hooks.hooks"), nullable=False, primary_key=True)
    room_number = Column(Integer, ForeignKey("doors.room_number"), nullable=False, primary_key=True)
    door_name = Column(String, ForeignKey("doors.door_name"), nullable=False, primary_key=True)
    # Relationships
    door: Door = relationship("Door", back_populates='keys_list')
    hook: Hook = relationship("Hook", back_populates='keys_list')
    issued_key: IssuedKey = relationship("Issued_Key", back_popluates="key")
    # Class methods
    def __init__(self, door: Door, hook: Hook):
        self.door = door
        self.hook = hook

        self.hook_id = self.hook.hook_id
        self.room_number = self.door.room_number
        self.door_name = self.door.door_name

    def add_key(self, opening_door: Door, hook: Hook):
    # Try catch block to add Key to db

    def issue_key(self, request: Request):
