from sqlalchemy import select
from sqlalchemy.orm import Session

from core.utils.logger import cli_logger
from db import engine
from models import Course, Student


def get_students_by_course(session, course_name):
    course = _get_course_by_name(session, course_name=course_name)

    cli_logger.info(f"Students on course '{course_name}':")

    for student in course.students:
        cli_logger.info(student.name)


def get_courses_by_student(session, student_name):
    student = _get_student_by_name(session, student_name=student_name)

    cli_logger.info(f"Courses of student '{student_name}':")

    for course in student.courses:
        cli_logger.info(course.name)


def update_student_name(session, old_name, new_name):
    student = _get_student_by_name(session, student_name=old_name)

    student.name = new_name
    session.commit()

    cli_logger.info(f"Student renamed: '{old_name}' -> '{new_name}'")


def delete_student(session, student_name):
    student = _get_student_by_name(session, student_name=student_name)

    session.delete(student)
    session.commit()

    cli_logger.info(f"Student '{student_name}' deleted")


def add_student_to_course(session, student_name, course_name):
    course = _get_course_by_name(session, course_name=course_name)

    student = Student(name=student_name)

    student.courses.append(course)

    session.add(student)
    session.commit()

    cli_logger.info(
        f"Student '{student_name}' added to course '{course_name}'"
    )

def _get_student_by_name(session, student_name):
    student = session.scalar(
        select(Student).where(Student.name == student_name)
    )

    if student is None:
        cli_logger.warning(f"Student '{student_name}' not found")

    return student

def _get_course_by_name(session, course_name):
    course = session.scalar(
        select(Course).where(Course.name == course_name)
    )

    if course is None:
        cli_logger.warning(f"Course '{course_name}' not found")

    return course

with Session(engine) as session:
    # get_students_by_course(session, "Python")
    # get_courses_by_student(session, "Angie Henderson")
    # update_student_name(session,"Angie Henderson",
    #     "Angie Henderson123")

    # delete_student(session, "Angie Henderson123")
    add_student_to_course(session, "Angie Henderson123", "Python")
    get_courses_by_student(session, "Angie Henderson123")