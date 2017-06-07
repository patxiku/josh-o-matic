#Josh-omatic improved so results seem real
import requests
import random
from time import sleep
 
api = "http://www.matthewlush.com/VotingSystem/submitVote.php"
votecount = 0
count = 0
whovote = 7
name = "Josh"

def randomHttpProxy():
    lines = open('proxies.txt').read().splitlines()
    myline =random.choice(lines)
    return myline


def randomIp():
    return str(random.randint(90,180))+"."+str(random.randint(90,180))+"."+str(random.randint(90,180))+"."+str(random.randint(90,180))

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
    
    proxy = randomHttpProxy()

    if proxy:
        ip,port = proxy.split(":")
        print ( "Proxy with IP " + ip + " will be used")
        postvars = { "postperson":whovote,"postip":randomIp() }
        try:
            x = requests.post(api,params=postvars,proxies={'http' : proxy})
        except requests.exceptions.ProxyError:
            continue
    else: 
        ip = randomIp()
        print ( "Random IP " + ip + " will be used")
        postvars = { "postperson":whovote,"postip":randomIp() }
        x = requests.post(api,params=postvars)  

 
    if (x.text == "Thank you for voting!"):
        print (name +" got another vote, "+ str(votecount) + " times voted.")
    
    sleepytime = random.randint(0,5)

    print ("Waiting for " + str(sleepytime) + " seconds")

    sleep(sleepytime)
    
    count += 1
