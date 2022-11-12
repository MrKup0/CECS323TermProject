from sqlalchemy import Column, String, Integer, Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from Enrollment import Enrollment


class Student(Base):
    __tablename__ = 'students'
    # There was an issue with uniqueness constraints when
    # using no surrogate for students, hence there is a surrogate included
    student_id = Column('student_id', Integer, Identity(start=1, cycle=True),
                           nullable=False, primary_key=True)
    first_name = Column('first_name', String(100), primary_key=False, nullable=False)
    last_name = Column('last_name', String(100), primary_key=False, nullable=False)

    # Relationship
    sections_list: [Enrollment] = relationship("Enrollment", back_populates="student", viewonly=False)

    # Alternate Key, original PK
    student_args = (UniqueConstraint('first_name', 'last_name', name='students_uk_01'),)

    def __init__(self, first_name: String, last_name: String):
        self.first_name = first_name
        self.last_name = last_name
        self.sections_list = []

    def add_section(self, section):
        for next_section in self.sections_list:
            if next_section == section:
                return

        instance = Enrollment(self, section)
        section.students_list.append(instance)
        self.sections_list.append(instance)
