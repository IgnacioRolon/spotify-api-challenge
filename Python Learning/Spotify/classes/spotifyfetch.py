import requests
from Spotify.classes.auth import Authorization

auth = Authorization()
authHeader = {'Authorization' : 'Bearer {}'.format(auth.get_spotify_token())}

def search_spotify_artist_id(artist: str):
    endpointUrl = "https://api.spotify.com/v1/search"
    queryParams = {'q' : 'artist:{}'.format(artist), 'type' : 'artist', 'limit' : 1}    

    result = requests.get(endpointUrl, params=queryParams, headers=authHeader)
    if len(result.json()["artists"]["items"]) > 0:
        return result.json()["artists"]["items"][0]["id"]    

def get_albums(id: str):  
    if id != None:
        endpointUrl = "https://api.spotify.com/v1/artists/{}/albums".format(id)
        queryParams = {'include_groups' : 'album'}
        result = requests.get(endpointUrl, params=queryParams, headers=authHeader)
        return result.json()["items"]