import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    Firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    pass 

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
    pass 

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(String(250), nullable=False)
    post_id = Column(String(250), nullable=False)
    pass 

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(String(250), nullable=False)
    
    pass 

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    follower_id = Column(Integer, ForeignKey('follower.id'))
    follower = relationship(Follower)

    comment_id = Column(Integer, ForeignKey('comment.id'))
    vehicle = relationship(Comment)

    media_id = Column(Integer, ForeignKey('media.id'))
    vehicle = relationship(Media)
    
    pass 
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
