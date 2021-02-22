import json
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
  print(video['title']['$t'])