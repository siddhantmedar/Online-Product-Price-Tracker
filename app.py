#Importing libraries

from tracker import track
import time

#Run always
while(True):
    #call track function from tracker.py
    track()
    #provide delay, like 60*60*24(To run the script daily)
    time.sleep(60*60*24)
    
