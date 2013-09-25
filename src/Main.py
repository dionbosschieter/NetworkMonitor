#!/usr/bin/env python3
#

# Auteurs: {dionbosschieter,timodekker}
#  
# Requirements:
# 
# Client<->server 
# Moet een modulaire user interface hebben 
# dit kunnen we doen met ncurses, in python heet het curses
# We kunnen de data over het netwerk versturen/ophalen met een database
# Bijv: mongoDB, javascript array's
# Meerdere connecties mogelijk, zowel aan agent kant als de administrator's kant
# Moet zo min mogelijk negatieve invloeden hebben op de verbindingskwaliteit. 
# Moet realtime data laten zien
# Data opslaan in database
# Data analyseren van gebruikers:
# Scapy is een library waar dit in kan hiermee kan je pakketten realtime binnen halen en de gegevens van het pakket analyseren/doorlezen.
# IP
# TCP
# DNS
# Modulaire protocol analyse
# dus voor elk protocol analyse een appart bestandje maken en deze in een modules map gooien, zodat elk bestand die in die map zit ge•mporteerd kan worden.


version = 0.1

class Main():
    
    nummer = 0

    def printnr(self):
        print(self.nummer)
        
        
print('Network Monitor version', version)
_main = Main()
_main.printnr()
_main.nummer = 2
_main.printnr()
