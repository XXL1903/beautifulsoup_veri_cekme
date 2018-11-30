import requests
from bs4 import BeautifulSoup
# * olan kısımlara kendi user-agent yazılmalı
headers_param={"User-Agent": "********"}
url = requests.get("https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-spor-toto-s%C3%BCper-lig/2018-2019/482ofyysbdbeoxauk19yg7tdt",headers_param)
soup = BeautifulSoup(url.content,"lxml")
yil=[]
sirali_yillar=[]
i=0
kelime=[]
yeni_sirali_yillar=[]
yeni_kelime=[]
l=""
yillar= soup.find("div",attrs={"data-instance-id":"page-season-picker"}).find("select",attrs={"class":"component-dropdown__native"}).find_all("option")
for c in yillar:
    sirali_yillar.append(c.text.strip())
for k in sirali_yillar:
    if len(k)>4:
        kelime=k
        lst=list(kelime)
        lst[4]="-"
        for t in lst:
            l=l+t
        yeni_sirali_yillar.append(l)
        l=""
for z in yeni_sirali_yillar:
    degisen_url = requests.get("https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-spor-toto-s%C3%BCper-lig/"+str(z)+"/482ofyysbdbeoxauk19yg7tdt",headers_param)
    soup1 = BeautifulSoup(degisen_url.content,"lxml")
    takim= soup1.find("table",attrs={"class":"p0c-competition-tables__table p0c-competition-tables__table--total"}).tbody.find_all("tr")
    print("-" * 60)
    print("*" * 60)
    print("{}".format(z))
    print("*" * 60)
    for i in takim:
        takimlar=i.select("td:nth-of-type(3)")[0].a.span.text.strip()
        oynadigi=i.select("td:nth-of-type(4)")[0].text.strip()
        galibiyet = i.select("td:nth-of-type(6)")[0].text.strip()
        beraberlik = i.select("td:nth-of-type(7)")[0].text.strip()
        maglubiyet = i.select("td:nth-of-type(8)")[0].text.strip()
        attigi = i.select("td:nth-of-type(9)")[0].text.strip()
        yedigi = i.select("td:nth-of-type(10)")[0].text.strip()
        averaj = i.select("td:nth-of-type(11)")[0].text.strip()
        puan = i.select("td:nth-of-type(12)")[0].text.strip()

        print(" {} {} {} {} {} {} {} {} {} ".format(takimlar,oynadigi,galibiyet,beraberlik,maglubiyet,attigi,yedigi,averaj,puan))
