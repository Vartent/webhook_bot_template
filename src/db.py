# database initial properties

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URL
from contextlib import contextmanager

engine = create_engine(DB_URL)
Base = declarative_base()
metadata = MetaData()

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """
    ORM session context manager to interact with database
    usage:

    with session_scope() as session:
        user = User(username=username, email=email)
        session.add(user)

    """
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
