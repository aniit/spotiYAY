import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your credentials
client_id = 'Enter Client ID Here'
client_secret = 'Enter Client Secret Here'
redirect_uri = 'http://localhost:3000'
scope = 'user-top-read playlist-modify-public playlist-modify-private'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Fetch the top tracks for the current user
top_tracks = sp.current_user_top_tracks(limit=50)

track_ids = [track['id'] for track in top_tracks['items']]

# Create a new playlist
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user_id, 'My Top Tracks Playlist')

# Add top tracks to the newly created playlist
sp.playlist_add_items(playlist['id'], track_ids)

print("Playlist created successfully!")