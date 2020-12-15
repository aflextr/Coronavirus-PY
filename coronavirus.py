import requests
from bs4 import BeautifulSoup
import os


def main():
    print("**************CORONAVİRUS WORLD CASE****************")
    print("1-World")
    print("2-italy")
    print("3-USA")
    print("4-Turkey")
    print("5 Other Countries")
    print("**************CORONAVİRUS WORLD CASE****************")
    
    al = int(input("Select:"))

    if al == 1:
        r = requests.get("https://www.worldometers.info/coronavirus/")
        Soup = BeautifulSoup(r.content ,"html.parser")
        for link in Soup.find_all(id="maincounter-wrap"):
            print(link.text)
            pass
    elif al == 2:
        r = requests.get("https://www.worldometers.info/coronavirus/country/italy/")
        Soup = BeautifulSoup(r.content ,"html.parser")
        for link in Soup.find_all(id="maincounter-wrap"):
            print(link.text)
            pass
    elif al == 3:
        r = requests.get("https://www.worldometers.info/coronavirus/country/us/")
        Soup = BeautifulSoup(r.content ,"html.parser")
        for link in Soup.find_all(id="maincounter-wrap"):
            print(link.text)
            pass
    elif al == 4:
        r = requests.get("https://www.worldometers.info/coronavirus/country/turkey/")
        Soup = BeautifulSoup(r.content ,"html.parser")
        for link in Soup.find_all(id="maincounter-wrap"):
            print(link.text)
            pass
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
        r = requests.get("https://www.worldometers.info/coronavirus/country/samoa/")
        soup = BeautifulSoup(r.content,"html.parser")
        find = soup.find("div" , attrs={"class":"maincounter-number"})
        print("Coronavirus Cases", +find.text, end="")
        pass
        
        
        
main()

