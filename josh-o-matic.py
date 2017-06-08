#Josh-o-matic v0.11
#Contributors: Patxiku, Fat-animal
#---------------------------------
import requests
import csv
import random
from time import sleep
 
API = "http://www.matthewlush.com/VotingSystem/submitVote.php"
IPCSV = "resources/us.csv"
PROXIES = "resources/proxies.txt"
JOSHPERCENTAGE = 57
JOSHID = 7
USEPROXY = True

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


print("------------------------------------------")
print("#            JOSH-O-MATIC                #")
print("------------------------------------------")
print(" ")
print(".....................................v0.11")
print(" ")
print("Do you want to use proxies? y/n \n*some proxies might not work and/or be slow.")
ans = input();
if ans == 'y':
    USEPROXY = True
else:
    USEPROXY = False

while True:
    iterations += 1
    print("------------------------------------------------")
    print("                 Iteration #"+str(iterations))
    print("------------------------------------------------")
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
            print ("Error")
            continue
    else: 
        ip = obtainRandomIP()
        print ( "Random IP " + ip + " will be used.")
        postvars = { "postperson":who,"postip":ip }
        x = requests.post(API,params=postvars)

    if (x.text == "Thank you for voting!"):
        print ('You voted for '+name+'.\nThank you for using josh-o-matic!')
        sleepytime = random.randint(15,30)
        print ("Waiting for " + str(sleepytime) + " seconds",end="")
        for counter in range(sleepytime):
            print(".",end="")
            sleep(1)
    else:
        print ('Server noticed about the proxy, trying again...')

    print("")




