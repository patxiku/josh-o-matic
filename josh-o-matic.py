#Josh-omatic improved so results seem real
import requests
from random import randint
from time import sleep
 
api = "http://www.matthewlush.com/VotingSystem/submitVote.php"
votecount = 0
count = 0
whovote = 7
name = "Josh"
while True:
    if count <= 3:
        whovote = 7
        name = "Josh"
    elif count <= 5:
        whovote = 3
        name = "Gaylord with id 3"
    else:
        whovote = 5
        name = "Gaylord with id 5"
        count = 0
        
    votecount+= 1
    fakeip = str(randint(90,180))+"."+str(randint(90,180))+"."+str(randint(90,180))+"."+str(randint(90,180))
    postvars = { "postperson":whovote,"postip":fakeip }
 
    x = requests.post(api,params=postvars)
 
    if (x.text == "Thank you for voting!"):
        print (name +" got another vote, "+ str(votecount) + " times voted.")
    sleepytime = randint(5,10)
    print ("Waiting for " + str(sleepytime) + " seconds")
    sleep(sleepytime)
    count += 1
