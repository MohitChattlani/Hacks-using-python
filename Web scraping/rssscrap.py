#scraping rss feeds of hindustan times

import requests

from bs4 import BeautifulSoup 


def main():
    
    url="http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

    resp=requests.get(url)

    soup=BeautifulSoup(resp.content,features="xml")

    items=soup.findAll('item')

    newsitems=[]

    for item in items:
        newsitem={}
        newsitem["title"]=item.title.text
        newsitem["description"]=item.description.text
        newsitem["link"]=item.link.text
        newsitem["date"]=item.pubDate.text
        newsitem["img_url"]=item.content["url"]
        newsitems.append(newsitem)
    
    print(newsitems[0])
    
main()
    
