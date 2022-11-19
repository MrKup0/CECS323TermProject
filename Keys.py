from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from Hooks import Hook
from Doors import Door


class Key(Base):
    __tablename__ = 'keys'
    # Instance Variables
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), nullable=False, primary_key=True)
    room_number = Column(Integer, ForeignKey('doors.door_number'), nullable=False, primary_key=True)
    door_name = Column(String, ForeignKey('doors.door_name'), nullable=False, primary_key=True)

    # Composite Key
    __table_args__ = (UniqueConstraint('hook_id', 'room_number', 'door_name'),)

    # Relationships
    door = relationship("Door", back_populates='keys_list')
    hook = relationship("Hook", back_populates='keys_list')
    issued_key = relationship("Issued_Key", back_populates="key")
    # Class methods
    def __init__(self, door, hook):
        self.door = door
        self.hook = hook

        self.hook_id = self.hook.hook_id
        self.room_number = self.door.room_number
        self.door_name = self.door.door_name

    #def add_key(self, opening_door: Door, hook: Hook):


    #def issue_key(self, request: Request):
