import json

import facebook
import requests
import networkx as nx
from auth import ACCESS_TOKEN

# create Graph API connection
g = facebook.GraphAPI(ACCESS_TOKEN)

friends = [ (friend['id'], friend['name'],)
			for friend in g.get_connections('me', 'friends')['data']
			 ]

url = 'https://graph.facebook.com/me/mutualfriends/%s?access_token=%s'			 

mutual_friends = {}

for friend_id, friend_name in friends:
	r = requests.get(url % (friend_id, ACCESS_TOKEN,))
	response_data = json.loads(r.content)['data']
	mutual_friends[friend_name] = [ data['name']
	 								for data in response_data ]

nxg = nx.Graph()

[ nxg.add_edge('me', mf) for mf in mutual_friends ]

[ nxg.add_edge(f1, f2)
	for f1 in mutual_friends
		for f2 in mutual_friends[f1]]

print nxg

