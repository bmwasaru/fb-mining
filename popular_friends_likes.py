from collections import Counter
import json
import facebook

from auth import ACCESS_TOKEN
from prettytable import PrettyTable

# create Graph API connection
g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }

friends_likes = Counter([like['name']
					for friend in likes
						for like in likes[friend]
							if like.get('name')])

pt = PrettyTable(field_names=['Name', 'Freq'])
pt.align['Name'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(fl) for fl in friends_likes.most_common(10) ]

print 'Top 10 likes amongst friends'
print pt