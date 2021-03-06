from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class PostItem(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=False)
    text = Column(String(1024), unique=False)
    date = Column(DateTime())

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.date = datetime.utcnow()

    def __repr__(self):
        return '<Post (%s): %s>' % (self.title, self.text)
