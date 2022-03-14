import json
import colorama
from colorama import Fore
import time
import requests

logo = """
  ___      ___        __       
 |_ _|_ __|_ _|_ __  / _| ___  
  | || '_ \| || '_ \| |_ / _ \ 
  | || |_) | || | | |  _| (_) |
 |___| .__/___|_| |_|_|  \___/ 
     |_|                                             
      []Coded by @_Yyeu[]
"""

def ipinfo():
    print(Fore.RED + logo)
    q = input("Enter ip address: ")
    print(f'You are going to get info about {q}')
    w = input("Do you want to continue? (y/n): ")
    if w == 'y':
        time.sleep(1)
    elif w == 'n':
        print("Exiting ... in 3 seconds")
        time.sleep(1)
        print("Exiting ... in 2 seconds")
        time.sleep(1)
        print("Exiting ... in 1 seconds")
        time.sleep(1)
        print("Exiting ... in 0 seconds")
        exit()
    else:
        print("You did not enter y or n so exiting.")
        print("Exiting ... in 3 seconds")
        time.sleep(1)
        print("Exiting ... in 2 seconds")
        time.sleep(1)
        print("Exiting ... in 1 seconds")
        time.sleep(1)
        print("Exiting ... in 0 seconds")
        exit()

    r = requests.get(f'https://freeipapi.com/api/json/{q}')
    infolati = json.loads(r.text)["latitude"]
    infolongi = json.loads(r.text)["longitude"]
    infocname = json.loads(r.text)["countryName"]
    infoccode = json.loads(r.text)["countryCode"]
    infotimezone = json.loads(r.text)["timeZone"]
    infozip = json.loads(r.text)["zipCode"]
    infocity = json.loads(r.text)["cityName"]
    inforegion = json.loads(r.text)["regionName"]

    print(f'This is the info found about {q}')
    print(f'{infolati}: latitude')
    print(f'{infolongi}: longitude')
    print(f'{infocname}: countryName')
    print(f'{infoccode}: countryCode')
    print(f'{infotimezone}: timeZone')
    print(f'{infozip}: zipCode')
    print(f'{infocity}: cityName')
    print(f'{inforegion}: regionName')
    
    

ipinfo()
