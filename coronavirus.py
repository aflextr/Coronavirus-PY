import requests
from bs4 import BeautifulSoup
import os


def country(value):
    try:
        r = requests.get("https://www.worldometers.info/"+value+"/")
        Soup = BeautifulSoup(r.content ,"html.parser")
    except:
        print("Network Error.")
    print("--------------"+value+"----------------")
    for link in Soup.find_all(id="maincounter-wrap"):
        print(link.text)
    pass





def main():
    file = open("motd.txt", "r")
    print(file.read())
    
    al = int(input("Select:"))

    if al == 1:
        country("coronavirus")
    elif al == 2:
        country("coronavirus/country/italy")
    elif al == 3:
        country("coronavirus/country/us")
    elif al == 4:
        country("coronavirus/country/turkey")
    elif al == 5:
        r = requests.get("https://www.worldometers.info/coronavirus/")
        Soup = BeautifulSoup(r.content ,"html.parser")
        for link in Soup.find_all("a" , attrs={"class":"mt_a"}):
            print(link.text, end=": ")
            print("https://www.worldometers.info/coronavirus/", end="" )
            print(link.get("href"))
            print(" ")          
            pass
    elif al == 6:
        namecountry = str(input("Country Name : "))
        country("coronavirus/country/"+namecountry)
        pass
              
        
main()

