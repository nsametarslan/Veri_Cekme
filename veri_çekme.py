import requests 
from bs4 import BeautifulSoup


url = requests.get("https://covid19.saglik.gov.tr/")
if url.status_code==200:
    print("Bu siteden veri çekilebilir")
else:
    print("Bu siteden veri çekilemez ")

soup = BeautifulSoup(url.content,"html.parser")

say = 1
while True:
    for i in soup.find("tbody").find_all("tr"):
        print("---------------------")
        print(i.text)
        say +=1
    devam = input("Devam edilsin mi (Evet/Hayır): ").lower()
    
    if devam != 'evet':
        print("Program sonlandırılıyor...")
        break
