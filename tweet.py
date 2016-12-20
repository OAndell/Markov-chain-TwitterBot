from twitter import *
import time
import getAuth
import tweetGenerator

ACCESS_TOKEN = getAuth.getACCESS_TOKEN()
ACCESS_SECRET = getAuth.getACCESS_SECRET()
CONSUMER_KEY = getAuth.getCONSUMER_KEY()
CONSUMER_SECRET = getAuth.getCONSUMER_SECRET()
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


while True:
    new_status = tweetGenerator.generateMessage() + " #svpol"
    twitter = Twitter(auth = oauth)
    #results = twitter.statuses.update(status = new_status)
    print("updated status: %s" % new_status)
    time.sleep(24 * 60 * 60)