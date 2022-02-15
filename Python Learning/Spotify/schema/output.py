from pydantic import BaseModel, Field
from typing import List, Any


class MusicCover(BaseModel):
    height: int
    width: int
    url: str


class MusicAlbum(BaseModel):
    name: str
    released: str
    tracks: int
    cover: MusicCover


class OutputValidation(BaseModel):
    Discography: List[MusicAlbum]
