from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from orm_base import Base

from Keys import Key

class Hook(Base):
    # Base settup
    __tablename__ = 'hooks'
    # Primary Key for the Hook Table
    hook_id = Column('hook_id', Integer, nullable=False, primary_key=True)

    # Relationships
    keys_list: [Key] = relationship("Keys", back_populates="hook", viewonly=False)

    # Object Init function
    def __init__(self, hook_id: Integer):
        self.hook_id = hook_id
        self.keys_list = []

    def add_key(self, key):
        for i in self.keys_list:
            if i == key:
                return

        self.keys_list.append(key)
