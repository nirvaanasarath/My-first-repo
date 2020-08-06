from bs4 import BeautifulSoup
import requests
import re


url = input("Enter the URL for your product : ")                                                                                       


def price_tracking(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content,"lxml")
    source = soup.find("div",class_=re.compile("1vC4OE _3qQ9m1"))
    # print(type(source))
    org_price = source.string[1:]
    if int(org_price) < 200:
        print("SEND SMS")
    else:
        print(f"{org_price} is the current price \n DO NOT SEND SMS")


price_tracking(url)  