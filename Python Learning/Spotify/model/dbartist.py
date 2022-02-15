from sqlalchemy import Column, Integer, String, true
from sqlalchemy.orm import declarative_base

base = declarative_base()


class DbArtist(base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=true)
    artistName = Column(String)
    name = Column(String)
    released = Column(String)
    tracks = Column(Integer)
    coverHeight = Column(Integer)
    coverWidth = Column(Integer)
    coverUrl = Column(String)

