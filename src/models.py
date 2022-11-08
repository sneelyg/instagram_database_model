import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique = True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique = True)

class Follower(Base):
    __tablename__ = 'Follower'
    
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey ("User.user_id"))
    user_to_id = Column(Integer, ForeignKey ("User.user_id"))
   
    rel_user = relationship('User')

class Media(Base):
    __tablename__ = 'Media'
   
    ID = Column(Integer, primary_key=True)
    type = Column(Integer,  nullable=False, unique = False)
    url = Column(String(250),  nullable=False, unique = True)
    post_id = Column(Integer, ForeignKey ("Post.ID"))  
   
    rel_user = relationship('Post')

class Post(Base):
    __tablename__ = 'Post'

    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey ("User.user_id"))
      
    rel_user_post = relationship('User')


class Comment(Base):
    __tablename__ = 'Comment'
 
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250),  nullable=False, unique = False)
    author_id = Column(Integer, ForeignKey ("User.user_id"))
    post_id = Column(Integer, ForeignKey ("Post.ID"))  
   
    rel_post = relationship('Post')
    rel_user = relationship('User')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e