# -*- coding: utf-8 -*
from urllib.request import Request, urlopen
import json

Coin=("adzcoin", "auroracoin-qubit", "bitcoin", "bitcoin-cash", "bitcoin-gold", "dash", "digibyte-groestl",
    "digibyte-qubit", "digibyte-skein", "electroneum", "ethereum", "ethereum-classic", "expanse", "feathercoin",
    "gamecredits", "geocoin", "globalboosty", "groestlcoin", "litecoin","maxcoin", "monacoin","monero","musicoin",
    "myriadcoin-groestl","myriadcoin-skein", "myriadcoin-yescrypt", "sexcoin", "siacoin", "startcoin", "verge-scrypt",
    "vertcoin", "zcash", "zclassic", "zcoin", "zencash")


ApiData= ""
Api= "&api_key="+ApiData

Action=("getminingandprofitsstatistics", "getautoswitchingandprofitsstatistics", "getuserallbalances", "getblockcount","getblocksfound",
        "getblockstats", "getcurrentworkers","getdashboarddata","getdifficulty", "getestimatedtime", "gethourlyhashrates","getnavbardata", 
        "getpoolhashrate", "getpoolinfo", "getpoolsharerate", "getpoolstatus", "gettimesincelastblock" ,"gettopcontributors", "getuserbalance", 
        "getuserhashrate", "getusersharerate", "getuserstatus", "getusertransactions", "getuserworkers", "public")


def menu_coin():
    global c
    try:
        c
    except NameError:
        for index, group in enumerate(Coin):
            print("%s: %s" % (index, group))
        c = int(input("coin to choose: "))
        print("selected: ", Coin[c])
    else:
        print("default coin: ", Coin[c])

def menu_action():
    global a
    try:
        a
    except NameError:
        for index, group in enumerate(Action):
            print("%s: %s" % (index, group))
        a = int(input("action: "))
        print("selected:",Action[a])
    else:
        print("default Action: ", Action[a])
    
def fonction(c):
    Url="https://"+Coin[c]+".miningpoolhub.com/index.php?page=api&action="+Action[a]+Api
    print("url:", Url)
    Req = Request(Url, headers={'User-Agent': 'Mozilla/5.0'})
    Webpage = urlopen(Req).read()
    jsonToPython = json.loads(Webpage)
    print(jsonToPython)


    
c=33 #comment to enable coin menu selection

a=18 #comment to enable action menu selection

menu_coin()
menu_action()
print()
fonction(c)