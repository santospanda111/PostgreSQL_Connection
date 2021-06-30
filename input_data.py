from models import *
from sqlalchemy.engine.reflection import Inspector
import logging
logger = logging.getLogger()
insp = Inspector(engine)

class Classroom:

    def create_table(self):
        """
        Creating tables provided in models.py
        :return: dictionary of table names and its fields
        """
        try:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            return insp.get_table_names()
        except Exception as e:
            logger.exception(e)
    
    def insert_student_data(self,name, age, grade):
        """
        Args:
            name ([String])
            age ([Integer])
            grade ([String])

        Returns:
            [count data size]
        """
        studnt = StudentData(name=name,age=age,grade=grade)
        session.add(studnt)
        session.commit()
        return session.query(StudentData).count()

    def update_row_student(self, value):
            """
            :param value: value to be inserted to update
            :return: count of rows after update
            """
            try:
                session.query(StudentData).filter(StudentData.id < 10).update(
                    {StudentData.name: value})
                session.commit()
                return session.query(StudentData.name).one()
            except Exception as e:
                logger.exception(e)

    def delete_row_student(self):
        """
        :return: count of rows after delete
        """
        try:
            session.query(StudentData).filter(StudentData.id < 10).delete()
            session.commit()
            return session.query(StudentData).count()
        except Exception as e:
            logger.exception(e)

    def insert_teacher_data(self,name,subject):
        """"
        Args:
            name ([String])
        Returns:
            [Count the data size]
        """
        teacher = TeacherData(teacher_name=name, subject=subject)
        session.add(teacher)
        session.commit()
        return session.query(TeacherData).count()

    def update_row_teacher(self, value):
            """
            :param value: value to be inserted to update
            :return: count of rows after update
            """
            try:
                session.query(TeacherData).filter(TeacherData.teacher_id < 10).update(
                    {TeacherData.teacher_name: value})
                session.commit()
                return session.query(TeacherData.teacher_name).one()
            except Exception as e:
                logger.exception(e)

    def delete_row_teacher(self):
        """
        :return: count of rows after delete
        """
        try:
            session.query(TeacherData).filter(TeacherData.teacher_id < 10).delete()
            session.commit()
            return session.query(TeacherData).count()
        except Exception as e:
            logger.exception(e)