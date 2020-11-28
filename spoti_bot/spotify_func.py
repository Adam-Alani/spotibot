import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "e31b1a401de04f70ae0e8b00c14425ca"  # Need to create developer profile
client_secret = "9af22fa28aec4e018c8829fdf8aa658a"
username = "21tqxjahbydtkdwzchxyhuvhy"
scope = 'user-library-read playlist-read-private playlist-read-collaborative'
redirect_uri = "http://localhost:8888/callback/"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
sp = spotipy.Spotify(auth=token)

def fetch_playlists(name):
    results = sp.search(name, type='playlist')
    items = results['playlists']['items']
    playlists = []
    if len(items) > 0:
        playlist = items[0]
        playlists.append(playlist['uri'])
    track_names = []
    for j in range(len(playlists)):
        pl_id = str(playlists[j])
        plist = sp.playlist(pl_id)
        tracks = plist["tracks"]
        songs = tracks["items"]
        for i in range(0, len(songs)):
            if songs[i]['track']['id'] is not None:  # Removes  local tracks, if any
                track_names.append( (songs[i]['track']['artists'][0]['name']) + " " + songs[i]['track']['name'])
    return(track_names)


