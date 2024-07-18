from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = "sqlite:///./sqllite.db"
engine = create_engine(sqlalchemy_database_url, connect_args={'check_same_thread': False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
