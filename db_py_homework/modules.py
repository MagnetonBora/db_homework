from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence, String, Column, Integer, Date

Base = declarative_base()


class Course(Base):

    __tablename__ = 'course'
    course_id = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    title = Column(String(50))
    ects = Column(Integer)
    price = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)

    def __repr__(self):
        return f"Course({self.title}, {self.ects}, {self.price}, {self.start_date}, {self.end_date})"


class OnlineCourse(Base):

    __tablename__ = 'online_course'
    course_id = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    url = Column(String(150))

    def __repr__(self):
        return f"Online-course({self.url})"


class OnsiteCourse(Base):

    __tablename__ = 'onsite_course'
    course_id = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    address = Column(String(150))
    duration = Column(Integer)

    def __repr__(self):
        return f"Onsite-course({self.address}, {self.duration})"


class Departament(Base):

    __tablename__ = 'departement'
    departement_id = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    departement_name = Column(String(150))
    address = Column(String(150))
    manager = Column(String(150))
    budget = Column(Integer)

    def __repr__(self):
        return f"Departement({self.departement_name}, {self.address}, {self.manager}, {self.budget})"


class Employees(Base):

    __tablename__ = 'employees'
    employee_id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    start_date = Column(Date)
    end_date = Column(Date)
    pesel = Column(Integer)
    telephone = Column(Integer)
    address = Column(String(100))

    def __repr__(self):
        return f"Employees({self.first_name}, {self.last_name}, \n" \
               f"{self.start_date}, {self.end_date}, {self.pesel},\n" \
               f" {self.telephone}, {self.address})"


class StudentGrades(Base):

    __tablename__ = 'student_grades'
    student_id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    course_id = Column(Integer)
    ects = Column(Integer)
    grade = Column(Integer)

    def __repr__(self):
        return f"StudentGrades({self.course_id}, {self.ects}, {self.grade})"


class Students(Base):

    __tablename__ = 'students'
    student_id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    address = Column(String(100))
    pesel = Column(Integer)
    telephone = Column(Integer)

    def __repr__(self):
        return f"Students({self.first_name}, {self.last_name}, {self.address}, {self.pesel}, {self.telephone})"


if __name__ == '__main__':
    pass
