from urllib import request, urlopen

request = request('https://api.lyrics.ovh/v1/artist/title')

response_body = urlopen(request).read()
print (response_body)