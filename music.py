from urllib.request import Request, urlopen

request = Request('https://api.lyrics.ovh/v1/artist/title')

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

