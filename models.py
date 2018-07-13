from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

# Write your classes below
class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    genres = relationship('Genre', secondary='songs')

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    artists = relationship(Artist, secondary='songs')

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    artist = relationship(Artist, backref=backref("songs", cascade="all, delete-orphan"))
    genre = relationship(Genre, backref=backref("songs", cascade="all, delete-orphan"))


engine = create_engine('sqlite:///music.db')
Base.metadata.create_all(engine)
