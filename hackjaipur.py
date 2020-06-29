 

import tweepy,speedtest,os, subprocess,urllib.request
from apscheduler.schedulers.blocking import BlockingScheduler

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# mentions = api.mentions_timeline()

st = speedtest.Speedtest()


def tweet():

    f= open("config.txt", "r")
    message = f.readline()
    cla = os.popen('speedtest-cli --simple --share')
    output = cla.read()
    x = (output.find('http'))
    bloody_url = (output[x:]).strip()
    x = (output.find('Download'))
    y = (output.find('Upload'))
    actualDSpeed=float((output[x+10:y-1].replace(' Mbit/s', ''))) #print download
    x = (output.find('Upload'))
    y= (output.find('Share'))
    actualUSpeed=float((output[x+8:y].replace(' Mbit/s', ''))) #print upload
    print(bloody_url)
    dSpeed=float(f.readline()[3:])
    uSpeed=float(f.readline()[3:])
    print(dSpeed)
    print(uSpeed)
    print(len(bloody_url))  
    
    if (actualDSpeed<0.8*dSpeed or actualUSpeed<0.8*uSpeed):
        print("Let's tweet")
        urllib.request.urlretrieve(bloody_url, 'image.png')
        api.update_with_media('image.png',message)
    else:
        print("Everything is good")	    
    

#The loop prints out text from all the mentions in your twitter account

# for mention in mentions:
# 	print(str(mention.id)+'-' + mention.text)
tweet()
scheduler = BlockingScheduler()
scheduler.add_job(tweet, 'interval', hours=2)
scheduler.start()
