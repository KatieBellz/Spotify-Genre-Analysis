import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# set up Spotify API client
client_id = 'your_client_id'
client_secret = 'your_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# search for a track
results = sp.search(q='track:Smells Like Teen Spirit artist:Nirvana', type='track')

# get audio features for a track
track_id = results['tracks']['items'][0]['id']
audio_features = sp.audio_features(track_id)

# get user's top tracks
top_tracks = sp.current_user_top_tracks(limit=10)

# get user's top artists
top_artists = sp.current_user_top_artists(limit=10)
