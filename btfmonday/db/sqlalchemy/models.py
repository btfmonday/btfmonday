from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine

Base = declarative_base()


class Picture(Base):
    __tablename__ = 'picture'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    published = Column(Boolean(), default=False)
    hash = Column(String(16), nullable=False)

engine = create_engine('sqlite:///btfmonday.sqlite')
Base.metadata.create_all(engine)
