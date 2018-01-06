# to run webscraping on passiton.com using python bs4

import requests
from bs4 import BeautifulSoup


def main():
	
    url="https://www.passiton.com/inspirational-quotes"
    # making request on the following url and getting the html content
    resp=requests.get(url)
    # making Soup object
    soup=BeautifulSoup(resp.content,'html5lib')
    quotes=soup.findAll('article',attrs={'class':'portfolio-item'})
    myquotes=[]
    for quote in quotes:
        myquote={}
        myquote["theme"]=quote['class']
        myquote["lines"]=quote.img['alt']
        myquote["img_url"]=quote.img['src']
        myquotes.append(myquote)
    print(myquotes[0])

main()
