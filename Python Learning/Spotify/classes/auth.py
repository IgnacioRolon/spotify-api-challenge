import requests
import os
from dotenv import load_dotenv
load_dotenv()


class Authorization:
    clientId = os.getenv('CLIENT_ID')
    clientSecret = os.getenv('CLIENT_SECRET')
    spotifyUrl = "https://accounts.spotify.com/api/token"

    # Add logic to save and regenerate every hour
    def get_spotify_token(self):
        response = requests.post(
            self.spotifyUrl,
            data={"grant_type": "client_credentials"},
            auth=(self.clientId, self.clientSecret),
        )
        return response.json()["access_token"]
