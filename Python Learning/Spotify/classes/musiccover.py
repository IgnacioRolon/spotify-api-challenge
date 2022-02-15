from dataclasses import dataclass

@dataclass
class MusicCover:
    height: int
    width: int
    url: str

    def __init__(self, height: int, width: int, url: str):
        self.height = height
        self.width = width
        self.url = url
    