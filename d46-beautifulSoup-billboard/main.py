from Scrape import Scrape
import dotenv
config = dotenv.dotenv_values()

SPOTIPY_CLIENT_ID= config['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = config['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = config['SPOTIPY_REDIRECT_URI']

scrape = Scrape()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = scrape.get_top_100(date)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    song = song['title']
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date}! Martine's Birthday Billboard", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)