import json
import facebook

from auth import ACCESS_TOKEN


def pp(o):
	print json.dumps(o, indent=1)

# create Graph API connection
g = facebook.GraphAPI(ACCESS_TOKEN)

# use ids to query for likes
mpower_id = '288644111340290'
ashoka_id = '66279444793'


# format integers with commas every 3 digits
def int_format(n):
	return "{:,}".format(n)

# query for likes
print "M-Power likes:", int_format(g.get_object(mpower_id)['likes'])
print "Ashoka likes:", int_format(g.get_object(ashoka_id)['likes'])

# query for feeds and links
pp(g.get_connections(mpower_id, 'feed'))
pp(g.get_connections(mpower_id, 'links'))
pp(g.get_connections(ashoka_id, 'feed'))
pp(g.get_connections(ashoka_id, 'links'))