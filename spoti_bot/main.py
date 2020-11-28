import spotify_func as sp
import youtube_func as yt

name = str(input("Enter Playlist Name: "))
sp_playlist = (sp.fetch_playlists(name))

for song in sp_playlist:
    print(yt.searchYT(song))


