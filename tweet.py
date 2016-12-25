from twitter import *
import time
import settings
import tweetGenerator


# Removes half of saved tweets, while saving the newest.
def clearOldData():
    print("clearing")
    with open(settings.getDataFileName(), "w", encoding='utf-8') as file:
        file.writelines(" ")
        file.close()

# Sets up Authentication settings
ACCESS_TOKEN = settings.getACCESS_TOKEN()
ACCESS_SECRET = settings.getACCESS_SECRET()
CONSUMER_KEY = settings.getCONSUMER_KEY()
CONSUMER_SECRET = settings.getCONSUMER_SECRET()
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Start bot loop
while True:
    time.sleep(24 * 60 * 60)
    new_status = tweetGenerator.generateMessage()  + " #svpol" #create tweet
    twitter = Twitter(auth=oauth)
    results = twitter.statuses.update(status=new_status)
    print("Updated status: %s" % new_status)  # Update twitter status
