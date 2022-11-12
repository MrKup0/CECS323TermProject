from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base


class Enrollment(Base):
    __tablename__ = 'enrollments'

    # Foreign Keys
    section_id = Column(Integer, ForeignKey('sections.section_id'), primary_key=True, nullable=False)
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True, nullable=False)
    # student_first_name = Column(String(100), ForeignKey('students.first_name'), primary_key=True, nullable=False)
    # student_last_name = Column(String(100), ForeignKey('students.last_name'), primary_key=True, nullable=False)

    # Exclusive Vars
    grade = Column('grade', String(2), nullable=False, default='C')

    # Relationships
    student = relationship("Student", back_populates='sections_list')
    section = relationship("Section", back_populates='students_list')

    def __init__(self, student, section):
        self.section_id = section.section_id
        self.student_id = student.student_id
        # self.student_first_name = student.first_name
        # self.student_last_name = student.last_name

        self.student = student
        self.section = section
