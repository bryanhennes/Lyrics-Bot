import lyrics_api
import requests
import json

#method that searches for an artist's ID by searching their name
def search_artist_id(artist_name):
    url = requests.get(f'{lyrics_api.api_url}{lyrics_api.search_artist}{artist_name}{lyrics_api.api_key}')
    data = json.dumps(url.json(), indent=2)
    print(data)

#method that gets album names for specified artist ID
def get_albums(artist_id):
    url = requests.get(f'{lyrics_api.api_url}{lyrics_api.get_albums}{artist_id}&s_release_date=desc&g_album_name=1&page_size=100{lyrics_api.api_key}')
    #data = json.dumps(url.json(), indent=2)
    data = url.json()
    for entry in data['message']['body']['album_list']:
        print(entry['album']['album_name'])


#method to get track information by searching track name
def search_track(track_title):
    url = requests.get(f'{lyrics_api.api_url}{lyrics_api.search_tracks}{track_title}{lyrics_api.api_key}')
    data = json.dumps(url.json(), indent=2)
    print(data)

#method to get all album IDs from an artists albums by searching the artist's ID
def get_album_ids(artist_id):
    album_ids = []
    url = requests.get(f'{lyrics_api.api_url}{lyrics_api.get_albums}{artist_id}&s_release_date=desc&g_album_name=1&page_size=100{lyrics_api.api_key}')
    data = url.json()
    for entry in data['message']['body']['album_list']:
        album_ids.append(entry['album']['album_id'])
    return album_ids


#method to get track ids
def get_album_tracks(album_id):
    track_ids = []
    url = requests.get(f'{lyrics_api.api_url}{lyrics_api.get_album_tracks}{album_id}&page=1&page_size=100{lyrics_api.api_key}')
    data = url.json()
    for entry in data['message']['body']['track_list']:
        #print(entry['track']['track_name'])
        #print(entry['track']['track_id'])
        track_ids.append(entry['track']['track_id'])
    return track_ids

def get_lyrics(track_id):
    url = requests.get(f'{lyrics_api.api_url}{lyrics_api.get_track_lyrics}{track_id}{lyrics_api.api_key}')
    data = url.json()
    print(data['message']['body']['lyrics']['lyrics_body'])