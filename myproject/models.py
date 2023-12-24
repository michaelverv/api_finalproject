# link naar db engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base


class Band(Base):
    __tablename__ = "bands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    genre = Column(String)
    lead_singer = Column(String)
    is_still_active = Column(Boolean, default=True)

    albums = relationship("Album", back_populates="band")


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    duration = Column(Float)
    amount_of_songs = Column(Integer)
    release_date = Column(Integer)

    band_id = Column(Integer, ForeignKey("bands.id"))
    band = relationship("Band", back_populates="albums")
    songs = relationship("Song", back_populates="album")


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    duration = Column(Float)

    album_id = Column(Integer, ForeignKey("albums.id"))
    # playlist_id = Column(Integer, ForeignKey("playlists.id"))
    album = relationship("Album", back_populates="songs")
    # playlist = relationship("Playlist", back_populates="song")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True, index=True)

    playlists = relationship("Playlist", back_populates="user")


class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="playlists")
    # song = relationship("Song", back_populates="playlist")
