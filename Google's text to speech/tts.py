import requests

url="https://translate.google.com/translate_tts"

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

text="How you doing?"

params={
    'ie':'UTF-8',
    'tl':'en',
    'client':'gtx',
    'q':text
}

r=requests.get(url,params=params,headers=headers)

with open("clip2.mp3",'wb') as f:
    f.write(r.content)

print(r.status_code)

