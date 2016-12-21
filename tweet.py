from twitter import *
import time
import settings
import tweetGenerator


# Removes half of saved tweets, while saving the newest.
def clearOldData():
    with open(settings.getDataFileName(), "r", encoding='utf-8') as file:
        data = file.readline()
    newData = data[len(data) // 2:]
    with open(settings.getDataFileName(), "w", encoding='utf-8') as file:
        file.writelines(newData)


# Check if the number lines in the saved data is larger than the specified number.Returns true or false.
def isDataLargerThan(lines):
    with open(settings.getDataFileName(), "r", encoding='utf-8') as file:
        data = file.readline()
    return len(data) > lines


# Sets up Authentication settings
ACCESS_TOKEN = settings.getACCESS_TOKEN()
ACCESS_SECRET = settings.getACCESS_SECRET()
CONSUMER_KEY = settings.getCONSUMER_KEY()
CONSUMER_SECRET = settings.getCONSUMER_SECRET()
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Start bot loop
while True:
    new_status = tweetGenerator.generateMessage()  + "#svpol" #create tweet
    twitter = Twitter(auth=oauth)
    results = twitter.statuses.update(status=new_status)
    print("Updated status: %s" % new_status)  # Update twitter status
    if isDataLargerThan(settings.getNumberOfLinesLimit()):  # Removes half of saved tweets, while saving the newest.
        clearOldData()
    time.sleep(18*60 * 60)# Sleep 18h
