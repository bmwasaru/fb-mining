import json

import requests
from auth import ACCESS_TOKEN

base_url = 'https://graph.facebook.com/me'

# get 10 likes for 10 friends
fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

url = '%s?fields=%s&access_token=%s' % (base_url, fields, ACCESS_TOKEN)

print url

content = requests.get(url).json()

print json.dumps(content, indent=1)