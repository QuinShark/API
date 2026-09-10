import requests
# from requests.utils import quote

artist = input("Give me an Artist:")
song = input("now give me a song: ")
lyrics = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')

lyrics = lyrics.json()
# lyric = Request.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')
if 'lyrics' not in lyrics:
    print("Can't find those lyrics.")
else:
    print(f"Here are the lyrics for {song}:")
    print(lyrics["lyrics"])
# print(request)
# Ask for artist and then print all their songs for the 
# NO WHERE CLOSE TO DONE. 


# # parameters. still so very confused. 
# # artist:Name of the artist
# # title:Title of the song
# {
#     'lyrics':"Here the Lyrics of the song"
# }
# {
#     "error": "No lyrics found"
#         }
# response_body = urlopen(request).read()
# print (response_body)

