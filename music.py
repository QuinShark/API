from urllib import request, urlopen

request = request('https://api.lyrics.ovh/v1/Coldplay/Adventure of a Lifetime')

response_body = urlopen(request).read()
print (response_body)