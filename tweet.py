
from twitter import *
import time

from tweetGenerator import generateMessage

ACCESS_TOKEN = '808029651062943750-DxmsQ86qmilsAapZZBGkCqujqyhOwKv'
ACCESS_SECRET = 'G5TIqTN7GlfMiJ0ZM0dAW7MVJkw5DZXzb90tq76IzCMY1'
CONSUMER_KEY = 'uBUbLlC1fzlrssBdmcoI4vnUY'
CONSUMER_SECRET = 'fFSuFmkHwXm1MGFvHT4GMsWQiTgp3L15wBgmXbY8i2QTOj3uM8'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


while True:
    new_status = generateMessage() + "#svpol"
    twitter = Twitter(auth = oauth)
    results = twitter.statuses.update(status = new_status)
    open("twitterData.txt", 'w').close()
    print("updated status: %s" % new_status)
    time.sleep(24 * 60 * 60)