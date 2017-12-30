#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
import cryptocompare
import coin
import api
Api=api.Api
coin=coin.coin

import json
from urllib.request import Request, urlopen
GTotal=0

Size=len(coin)

def url(c):
    global i
    global Obj
    url="https://"+coin[c]+".miningpoolhub.com/index.php?page=api&action=getuserbalance&api_key="+Api
    
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        json.loads(webpage)
    except:
        
        print("<td><a href=\"" ,url,"\">",coin[c],"</a></td><td>indisponible</td><td>indisponible</td>")  
          
    else:
        print("<td><a href=\"" ,url,"\">",coin[c],"</a></td>")
        #print(repr(jsonToPython))
        
        Obj = json.loads(webpage)
        Obj=Obj['getuserbalance']
        Obj=Obj['data']
        print("<td>",Obj['confirmed'],"</td> <td>",Obj['unconfirmed'],"</td>")
        
        

html = """<!DOCTYPE html>
<head>
    <title>Balance miningpool</title>
    <style>
    table
{
    border-collapse: collapse;
}
td, th /* Mettre une bordure sur les td ET les th */
{
    border: 1px solid black;
}
th
{
    vertical-align: middle;
}
</style>  
</head>
<body>"""
Tableau = """
     <table>
        <tr>
        <th>Name</th>
        <th>Confirmed</th>
        <th>Unconfirmed</th>
        <th>usd confirmed</th>
        <th>usd unconfirmed</th>
        <th>Total</th>
        <th>price per coin</th>
        </tr>
        """
FinTableau= """</table>"""
htmlfin = """</body>
</html>
"""
print(html)
print(Tableau)
i = 0
while i <= Size-1:
    Total = 0
    print("<tr>")
    url(i)
    cryptocompare.url(i)
    if Obj['confirmed'] != 0:
        print("<td>",round(cryptocompare.usd*Obj['confirmed'],2),"$</td>")
    else:
        print("<td>0</td>")
        
    if Obj['unconfirmed'] != 0:
        print("<td> ",round(cryptocompare.usd*Obj['unconfirmed'],2),"$</td>")
    else:
        print("<td>0</td>")
        
    Total=Obj['unconfirmed']+Obj['confirmed']
    
    if Total != 0:
        print("<td> ",round(cryptocompare.usd*Total,2),"$</td>")
        GTotal =cryptocompare.usd*Total+GTotal
    else:
        print("<td>0</td>")
        
    print("<td>", cryptocompare.usd,"$</td>")
    
    cryptocompare.usd = 0
    Obj['unconfirmed'] = 0
    Obj['confirmed'] = 0
    i= i+1
    print("</tr>")
print("<tr><td></td><td></td><td></td><td></td><td>Total</td><td>",round(GTotal,2),"$</td><td></td>")
print(FinTableau)
#print("Total: ",round(GTotal,2),"$")
print(htmlfin)