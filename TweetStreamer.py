import getAuth

try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = getAuth.getACCESS_TOKEN()
ACCESS_SECRET = getAuth.getACCESS_SECRET()
CONSUMER_KEY = getAuth.getCONSUMER_KEY()
CONSUMER_SECRET = getAuth.getCONSUMER_SECRET()

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(track="#svpol" ,language="sv")

for tweet in iterator:
    jsonTweet = json.loads(json.dumps(tweet))
    if 'text' in jsonTweet:
            with open("twitterData.txt", "a", encoding='utf-8') as myfile:
                myfile.write(jsonTweet['text'] + "\n\n")
                myfile.close()