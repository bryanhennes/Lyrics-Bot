import requests
import lyrics_methods
import lyrics_api
import json
import random


#api = f'https://api.musixmatch.com/ws/1.1/chart.artists.get?page=1&page_size=3&country=it{lyrics_api.api_key}'


#lyrics_methods.search_artist_id('dance gavin dance')

#lyrics_methods.get_albums(lyrics_api.dgd_id)
#lyrics_methods.search_track("open your eyes and look north")

album_ids = lyrics_methods.get_album_ids(lyrics_api.dgd_id)
album_selection = random.choice(album_ids) #get random album id

track_ids = lyrics_methods.get_album_tracks(album_selection)
track_selection = random.choice(track_ids)

lyric_body = lyrics_methods.get_lyrics(track_selection)
print(lyric_body)

