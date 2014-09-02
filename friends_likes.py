import json
import facebook

from auth import ACCESS_TOKEN

# create Graph API connection
g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")["data"]

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']
			for friend in friends }

print likes			