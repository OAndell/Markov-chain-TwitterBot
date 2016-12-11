
from twitter import *
import time

from tweetGenerator import generateMessage

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


while True:
    new_status = generateMessage() + "#svpol"
    twitter = Twitter(auth = oauth)
    results = twitter.statuses.update(status = new_status)
    open("twitterData.txt", 'w').close()
    print("updated status: %s" % new_status)
    time.sleep(24 * 60 * 60)
