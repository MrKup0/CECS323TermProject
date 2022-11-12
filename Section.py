from sqlalchemy import Column, String, Integer, Identity, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from Enrollment import Enrollment


class Section(Base):
    __tablename__ = 'sections'
    section_id = Column('section_id', Integer, Identity(start=1, cycle=True),
                           nullable=False, primary_key=True)
    department_name = Column('department_name', String(100), nullable=False)
    course_name = Column('course_name', String(50), nullable=False)
    section_number = Column('section_number', Integer, nullable=False, default=1)
    semester = Column('semester', String(50), nullable=False)
    year = Column('year', Integer, nullable=False)

    # Relationship
    students_list: [Enrollment] = relationship("Enrollment", back_populates="section", viewonly=False)

    # Alternate Key
    table_args = (UniqueConstraint(
        'department_name', 'course_name',
        'section_number', 'semester',
        'year', name='sections_uk_01'),)

    def __init__(self,
                 department_name: String, course_name: String,
                 section_number: Integer, semester: String,
                 year: Integer):
        self.department_name = department_name
        self.course_name = course_name
        self.section_number = section_number
        self.semester = semester
        self.year = year
        self.students_list = []

    def add_student(self, student):
        for test_student in self.students_list:
            if test_student == student:
                return

        instance = Enrollment(student, self)
        student.sections_list.append(instance)
        self.students_list.append(instance)
