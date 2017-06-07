#Josh-o-matic v0.1
#Contributors: Patxiku, Fat-animal

import requests
<<<<<<< HEAD
import csv
import random
from time import sleep
 
API = "http://www.matthewlush.com/VotingSystem/submitVote.php"
IPCSV = "resources/us.csv"
PROXIES = "resources/proxies.txt"
JOSHPERCENTAGE = 75
JOSHID = 7
#Doesn't always work since server has some proxies in its blacklist
USEPROXY = False

iterations = 0

class IPAdress:    
    def __init__ (self, ip):
        self.ip = self.__obtainLastDigit(ip)

    def obtainLastDigit(self, ip):
        m = ip.rsplit('.', 1)[-1]
        mMin = int(m.rpartition('/')[0])
        mMax = int(m.rsplit('/', 1)[-1])
        m = str(random.randint(mMin,mMax))
        ip = ip.rpartition('.')[0] + '.' + m
        return ip
    __obtainLastDigit = obtainLastDigit

def obtainRandomIP():
    with open(IPCSV, 'r') as csvfile:
      ips = list(csv.reader(csvfile))

    length = len(ips)
    pos = random.randint(0, length)
    ipAdress = IPAdress(*ips[pos])    
    return ipAdress.ip

def randomHttpProxy():
    lines = open(PROXIES).read().splitlines()
    myline = random.choice(lines)
    return myline


def whoToVote():
    voteID = 0
    percentage = random.randint(0,100)
    if percentage > JOSHPERCENTAGE:
        voteID = random.randint(1,6)
    else:
        voteID = JOSHID
    return voteID

while True:
    iterations += 1
    who = whoToVote()
    name = 'Faggot #'+str(who)
    if who == JOSHID:
        name = 'Glorious JOSH'
    proxy = randomHttpProxy()
    if USEPROXY and proxy:
        ip,port = proxy.split(":")
        print ( "Proxy with IP " + ip + " will be used.")
        postvars = { "postperson":who,"postip":obtainRandomIP() }
        try:
            x = requests.post(API,params=postvars,proxies={'http' : proxy})
        except requests.exceptions.ProxyError:
            continue
    else: 
        ip = obtainRandomIP()
        print ( "Random IP " + ip + " will be used.")
        postvars = { "postperson":who,"postip":ip }
        x = requests.post(API,params=postvars)

    if (x.text == "Thank you for voting!"):
        print ('You voted for '+name+'. This program has done '+str(iterations)+' iterations. Thank you for using josh-o-matic.')
        sleepytime = random.randint(7,12)
        print ("Waiting for " + str(sleepytime) + " seconds")
        sleep(sleepytime)
    else:
        print ('Server noticed about the proxy, trying again...')






=======
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
>>>>>>> origin/master
