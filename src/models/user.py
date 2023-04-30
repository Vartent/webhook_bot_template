from db import Base
from sqlalchemy import Column, Integer, String


# basic User ORM model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)

