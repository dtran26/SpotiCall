import requests

spotifyID = '57180e35ec194d22aa2cfd69053d6f42'
spotifyToken = '32c8e627c4e5456a83ea090c5454c34d'


def get_track_url(song_title):
    spotify_url = 'https://api.spotify.com/v1/search'
    params = {'q': song_title, 'type': 'track'}

    spotify_response = requests.get(spotify_url, params=params).json()
    track_url = spotify_response['tracks']['items'][0]['preview_url']
    return track_url