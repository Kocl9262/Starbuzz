import urllib2
import time

cena = 99.99
while cena > 4.74:
    time.sleep(900)
    page = urllib2.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    tekst = page.read().decode("utf8")
    kje = tekst.find(">$")
    zacetek = kje + 2
    konec = zacetek + 4
    cena = float(tekst[zacetek:konec])
print("Buy!")

