import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- Spotify credentials ---
CLIENT_ID = "5394f8bbc8994f58944eedb935411b3a"
CLIENT_SECRET = "a371c917d4e24c77b20a2fce660444c0"
REDIRECT_URI = "http://127.0.0.1:8000/callback"
SCOPE = "playlist-modify-public"

# --- Spotify Auth ---
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# --- Get date and fetch Billboard JSON ---
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://raw.githubusercontent.com/mhollingshead/billboard-hot-100/main/date/{date}.json"

response = requests.get(url)
if response.status_code != 200:
    print("Invalid date or chart data not found.")
    exit()

chart = response.json()
songs = [entry['song'] for entry in chart['data']]
artists = [entry['artist'] for entry in chart['data']]

# --- Spotify: Create playlist ---
user_id = spotify.current_user()["id"]
playlist_name = f"Billboard HOT 100 - {date}"
playlist_description = f"Top 100 songs from Billboard on {date}"

# Check if playlist already exists
user_playlists = spotify.current_user_playlists()
existing_names = [playlist["name"] for playlist in user_playlists["items"]]

track_uris = []

# --- Search for songs on Spotify ---
for song, artist in zip(songs, artists):
    print(f"Searching: {song} by {artist}")
    result = spotify.search(q=f"track:{song} artist:{artist}", type='track', limit=1)
    items = result["tracks"]["items"]
    if items:
        track_uris.append(items[0]["uri"])
    else:
        print(f"NOT FOUND: {song} by {artist}")

# --- Create or skip playlist ---
if playlist_name in existing_names:
    print("Playlist already exists.")
else:
    playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description)
    if track_uris:
        spotify.playlist_add_items(playlist["id"], track_uris)
        print(f"Playlist '{playlist_name}' created with {len(track_uris)} tracks.")
    else:
        print("No tracks were added due to missing URIs.")