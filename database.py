from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db', connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlush=False)

Base = declarative_base()
