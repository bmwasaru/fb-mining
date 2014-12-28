import requests

username = raw_input()

username_request = requests.get('https://graph.facebook.com/{0}/'.format(username))

if username_request.status_code == 200:
    print "username taken"
else:
    print "username available"


