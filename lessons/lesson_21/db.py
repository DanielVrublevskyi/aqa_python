from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from models import Base

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="Aa123456",
    host="localhost",
    port=5432,
    database="student_management"
)

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)