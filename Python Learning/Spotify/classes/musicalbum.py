from Spotify.classes.musiccover import MusicCover
from dataclasses import dataclass

@dataclass
class MusicAlbum:
    name: str
    released: str
    tracks: int
    cover: MusicCover

    def __init__(self, name: str, released: str, tracks: int, cover: MusicCover):
        self.name = name
        self.released = released
        self.tracks = tracks
        self.cover = cover
    
    def __eq__(self, other):
        return self.name == other.name
    