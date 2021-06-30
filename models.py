from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(f'postgresql+psycopg2://{os.getenv("sanusername")}:{os.getenv("sanpassword")}@{os.getenv("host")}:{os.getenv("port")}/School')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = MetaData()


class TeacherData(Base):
    
    __tablename__ = "teacher_data"
    teacher_id = Column(Integer, primary_key = True)
    teacher_name = Column(String(50))
    subject = Column(String(50))
    student = relationship("StudentData")
    def __repr__(self):
        return f"name:{self.teacher_name},Subject: {self.subject}"


class StudentData(Base):
    """[Here i have created a class "StudentData"]

    Args:
        Base
    -Here i have created a table with detailed columns.
    """
    __tablename__ = 'student_data'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teacher_data.teacher_id'))
    date_added_on = Column(DateTime, onupdate=datetime.now)
    def __repr__(self):
        return f"name:{self.name},age:{self.age},grade:{self.grade}, date: {self.added_on_date}, teacher_id: {self.teacher_id}"
