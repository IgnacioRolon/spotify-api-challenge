from Spotify.classes.musicalbum import MusicAlbum
from Spotify.classes.musiccover import MusicCover
from Spotify.classes.aws import get_album_image_s3
from Spotify.model.dbartist import DbArtist
from typing import List
import Spotify.classes.spotifyfetch as spfetch
from fastapi import Depends, FastAPI, Header, Response
from sqlalchemy.orm import Session
from Spotify.db.session import get_db
from Spotify.schema.input import InputValidation
from Spotify.schema.output import OutputValidation

# Starting the API
app = FastAPI()


@app.get("/api/v1/albums", response_model=OutputValidation)
def return_albums(
    response: Response,
    artist: InputValidation = Depends(), 
    session: Session = Depends(get_db),
    ):    
    artistAlbums: List[MusicAlbum] = list()
    for instance in session.query(DbArtist).filter_by(artistName=artist.artist):
        cover = MusicCover(instance.coverHeight, instance.coverWidth, instance.coverUrl)
        album = MusicAlbum(instance.name, instance.released, instance.tracks, cover)
        coverimage = get_album_image_s3(artist.artist, album.name)
        if coverimage:
            cover.url = coverimage[2:]
            cover.url = cover.url[:-1]
        if album not in artistAlbums:
            artistAlbums.append(album)
    # If the DB didn't have the album for the artist, fetch it from Spotify
    if len(artistAlbums) == 0:
        artistId = spfetch.search_spotify_artist_id(artist.artist)
        albums = spfetch.get_albums(artistId)
        if albums:
            for item in albums:
                cover = MusicCover(item["images"][0]["height"], item["images"][0]["width"], item["images"][0]["url"])
                album = MusicAlbum(item["name"], item["release_date"], item["total_tracks"], cover)
                coverimage = get_album_image_s3(artist.artist, album.name)
                if coverimage:
                    cover.url = coverimage[2:]
                    cover.url = cover.url[:-1]
                if album not in artistAlbums:
                    artistAlbums.append(album)

    response.headers["Access-Control-Allow-Origin"] = "*"
    if len(artistAlbums) == 0:
        response.status_code = 404
        return {"Discography": artistAlbums}
    else:
        return {"Discography": artistAlbums}

