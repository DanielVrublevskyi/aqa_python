import random

from faker import Faker
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.utils.logger import cli_logger
from db import engine
from models import Course, Student


fake = Faker()

# Чтобы случайные данные были одинаковыми при каждом запуске
Faker.seed(42)
random.seed(42)

def add_courses(session):
    existing_courses = session.scalars(select(Course)).all()

    if existing_courses:
        cli_logger.info("'Courses' table already exist. Skip adding 'Courses' table.")
        return

    courses = [
        Course(name="Python"),
        Course(name="SQL"),
        Course(name="Java"),
        Course(name="API Testing"),
        Course(name="Automation QA"),
    ]

    session.add_all(courses)
    session.commit()

    cli_logger.info(f"Added {len(courses)} courses")


def delete_students(session):
    students = session.scalars(select(Student)).all()

    for student in students:
        session.delete(student)

    session.commit()

    cli_logger.info(f"Deleted {len(students)} students")


def add_students(session):
    courses = session.scalars(select(Course)).all()

    students = []

    for _ in range(20):
        student = Student(name=fake.name())

        # Выбираем для студента случайно от 1 до 3 разных курсов
        student.courses = random.sample(
            courses,
            k=random.randint(1, 3)
        )

        students.append(student)

    session.add_all(students)
    session.commit()

    cli_logger.info(f"Added {len(students)} students")


with Session(engine) as session:
    add_courses(session)
    delete_students(session)
    add_students(session)