from sqlalchemy import Column, String, Integer, ARRAY
from database import Base

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, unique=True, nullable=False)
    alias = Column(ARRAY(String), default=[])
    subject_tags = Column(ARRAY(String), default=[])
    description = Column(String)
    prerequisites = Column(ARRAY(String), default=[])
    students_enrolled = Column(ARRAY(Integer), default=[])
    max_enrollment = Column(Integer)
    min_grade = Column(Integer)
    owner_id = Column(Integer)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    grade_level = Column(Integer)
    admin_level = Column(String)
    enrolled_classes = Column(ARRAY(String), default=[])
    published_classes = Column(ARRAY(String), default=[])