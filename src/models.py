import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique = True)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique = True)

class Follower(db.Model):
    __tablename__ = 'Follower'
    
    user_from_id = db.Column(db.Integer, ForeignKey ("User.user_id"))
    user_to_id = db.Column(db.Integer, ForeignKey ("User.user_id"))
   
    rel_user = db.relationship('User')

class Media(db.Model):
    __tablename__ = 'Media'
   
    ID = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer,  nullable=False, unique = False)
    url = db.Column(db.String(250),  nullable=False, unique = True)
    post_id = db.Column(db.Integer, ForeignKey ("Post.ID"))  
   
    rel_user = db.relationship('Post')

class Post(db.Model):
    __tablename__ = 'Post'

    ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey ("User.user_id"))
      
    rel_user_post = db.relationship('User')


class Comment(db.Model):
    __tablename__ = 'Comment'
 
    ID = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(250),  nullable=False, unique = False)
    author_id = db.Column(db.Integer, ForeignKey ("User.user_id"))
    post_id = db.Column(db.Integer, ForeignKey ("Post.ID"))  
   
    rel_post = db.relationship('Post')
    rel_user = db.relationship('User')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e