import os
import logging
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler

import requests
from io import BytesIO
from PIL import Image

def getSongInfo(username):
  scope = 'user-read-currently-playing'
  cache_handler = CacheFileHandler(username=username)
  client_id = os.getenv("SPOTIPY_CLIENT_ID")
  client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
  redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

  auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, 
      redirect_uri=redirect_uri, scope=scope, open_browser=False, 
      cache_handler=cache_handler)
  
  sp = spotipy.Spotify(auth_manager=auth_manager)
  track = sp.current_user_playing_track()

  if track is None:
      print("No song playing")
  else:  
    song = track["item"]["name"]
    imageURL = track["item"]["album"]["images"][0]["url"]
    print(song)
    return [song, imageURL]

  
