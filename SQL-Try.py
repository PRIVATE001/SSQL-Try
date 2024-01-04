import os
R='\33[1;31m'
G='\33[1;32m'
O='\33[1;33m'
B='\33[1;34m'
P='\33[1;35m'
C='\33[1;36m'
try:
 import pyfiglet
except:
 os.system("pip install pyfiglet")
import pyfiglet
try:
 import requests
except:
 os.system("pip install requests")
import requests
try:
 from googlesearch import search 
except:
 os.system("pip install google")
from googlesearch import search
try:
 import webbrowser
except:
 os.system("pip install webbrowser")
import webbrowser
bnrx = pyfiglet.figlet_format("SQL INJ")
print(C+bnrx)
kay = "php?id=1"
kay1="'"
for i in search(kay,stop=100):
 try:
  req = requests.get(i+kay1)
  msg="your SQL"
  if msg in req.text:
   print(G+"[✓] website SQL !")
   print("[✓] "+i)
   webbrowser.open(i)
   xx = input(O+"[*] Do you compliet? y/n: ")
   if xx == "n" or xx == "N":
    break
  else:
   print(R+"[*] website NO SQL !")
 except:
  print(B+"INTERNET!!!!!!")