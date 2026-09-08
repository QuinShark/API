from urllib.request import Request, urlopen

request = Request('https://api.lyrics.ovh/v1/artist/title')

response_body = urlopen(request).read()
print (response_body)

