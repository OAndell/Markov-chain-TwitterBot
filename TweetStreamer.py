import settings
import json


from twitter import OAuth, TwitterStream

# Sets up Authentication settings
ACCESS_TOKEN = settings.getACCESS_TOKEN()
ACCESS_SECRET = settings.getACCESS_SECRET()
CONSUMER_KEY = settings.getCONSUMER_KEY()
CONSUMER_SECRET = settings.getCONSUMER_SECRET()

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(track="#svpol" ,language="sv") #specifies what kind of tweets to stream.

for tweet in iterator: #Itrates over all incoming tweets
    jsonTweet = json.loads(json.dumps(tweet)) #Convert to Json
    if 'text' in jsonTweet:#Check if json contains text.
            with open(settings.getDataFileName(), "a", encoding='utf-8') as file: #Saves the current tweet tp txt file
                file.write(jsonTweet['text'] + "\n\n")
                file.close()