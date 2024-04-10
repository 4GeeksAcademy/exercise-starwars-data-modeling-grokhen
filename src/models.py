import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Favorite_planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    favorite_planet = Column(String(250), ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Favorite_character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    favorite_character = Column(String(250), ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), )
    planet_population = Column(String(250))
    planet_rotation = Column(String(125))
    user = relationship(Favorite_planet)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(125))
    character_age = Column(String(100))
    character_weight = Column(String(10))
    user = relationship(Favorite_character)

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')
