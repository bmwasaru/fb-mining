import json
import facebook

from auth import ACCESS_TOKEN


def pp(o):
	print json.dumps(o, indent=1)

# create Graph API connection
g = facebook.GraphAPI(ACCESS_TOKEN)

# queries

print '-------------'
print 'Me'
print '-------------'
pp(g.get_object('me'))
print
print '-------------'
print 'My Friends'
print '-------------'
pp(g.get_connections('me', 'friends'))
print
print '-------------'
pp(g.request("search", {'q': 'M-Power', 'type': 'page'}))