from sqlalchemy import Column, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from Hooks import Hook
from Doors import Door


class Key(Base):
    __tablename__ = 'keys'
    # Instance Variables
    hook_id = Column(Integer, nullable=False, primary_key=True)
    room_number = Column(Integer, nullable=False, primary_key=True)
    door_name = Column(String, nullable=False, primary_key=True)

    # Composite Key
    __table_args__ = (ForeignKeyConstraint([room_number, door_name, hook_id],
                                           [Door.room_number, Door.door_name, Hook.hook_id]),{})

    # Relationships
    door = relationship("Door", back_populates='keys_list')
    hook = relationship("Hook", back_populates='keys_list')
    issued_key = relationship("Issued_Key", back_popluates="key")
    # Class methods
    def __init__(self, door, hook):
        self.door = door
        self.hook = hook

        self.hook_id = self.hook.hook_id
        self.room_number = self.door.room_number
        self.door_name = self.door.door_name

    #def add_key(self, opening_door: Door, hook: Hook):


    #def issue_key(self, request: Request):
