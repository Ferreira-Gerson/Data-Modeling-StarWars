import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = (String(250))
    surface_water = (Integer)
    population = (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(100))
    gender = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))  
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = (Integer)
    lenght = (Integer)
    max_atmosphering_speed = (Integer)
    crew = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = (String(200))
    vehicles_class = (String(250))
    user_id = Column(Integer, ForeignKey('user.id'))

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    lenght = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passangers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    hyperdrive_rating = Column(Float)
    MGLT = Column(Integer)
    starship_class = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')