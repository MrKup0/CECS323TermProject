from sqlalchemy import \
    Column, Integer, String, Boolean, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from datetime import date

class IssuedKey(Base):
    __tablename__ = 'issued_keys'

    # Define instance Variables
    employee_id = Column(Integer, ForeignKey('requests.employee_id'), nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('keys.hook_id'), nullable=False, primary_key=True)
    approved_room = Column(Integer, ForeignKey('keys.room_number'), nullable=False, primary_key=True)

    requested_room = Column(Integer, ForeignKey('requests.room_number'), nullable=False)
    door_name = Column(String, ForeignKey('keys.door_name'), nullable=False)
    request_date = Column(Date, ForeignKey('requests.request_date'), nullable=False)

    issued_date = Column('issued_date', Date, nullable=False)
    return_date = Column('return_date', Date, nullable=False)
    date_returned = Column('date_returned', Date, nullable=True)
    is_valid = Column('is_valid', Boolean, nullable=False)

    __table_args__ = (UniqueConstraint('employee_id', 'hook_id', 'approved_room', 'requested_room', 'door_name', 'request_date'),)

    # Relationship tracker
    request = relationship("Request", primaryjoin="and_(IssuedKey.employee_id == foreign(Request.employee_id), "
                           "IssuedKey.requested_room == foreign(Request.room_number), "
                           "IssuedKey.request_date == foreign(Request.request_date))", back_populates="issued_key")
    key = relationship("Key", primaryjoin="and_(IssuedKey.hook_id == foreign(Key.hook_id), "
                       "IssuedKey.approved_room == foreign(Key.room_number), "
                       "IssuedKey.door_name == foreign(Key.door_name))", back_populates="issued_key")

    # Class Methods
    def __init__(self, request, key):
        self.request = request
        self.key = key

        # Primary Key Collection
        self.employee_id = self.request.employee_id
        self.hook_id = self.key.hook_id
        self.approved_room = self.key.room_number

        self.requested_room = self.request.room_number
        self.door_name = self.key.door_name
        today = date.today()
        self.issued_date = today.strftime("%Y-%m-%d")
        self.return_date = date(today.year + 1, today.month + 16, today.day)
        self.date_returned = None
        self.is_valid = True
        self.return_date = self.request.request_date



