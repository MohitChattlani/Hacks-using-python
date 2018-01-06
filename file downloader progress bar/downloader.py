#Using tqdm library

def main():
    from tqdm import tqdm
    import time
    import requests

    chunk_size=1024

    url="http://www.pdf995.com/samples/pdf.pdf"

    r=requests.get(url,stream=True)

    total_size=int(r.headers['content-length'])

    f=open("random.pdf",'wb');

    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size),total=total_size/chunk_size,unit='kb'):
    	f.write(data)

main()
