import requests

from bs4 import BeautifulSoup, SoupStrainer
url="https://www.seohocasi.com/kopya-icerik-seo-iliskisi/"
import operator
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords



    alturller = []
    alturller1 = []
    alturller2 = []
    counter=0
    #index = 0
    anaUrl = ""
    for harf in url:
        if(counter < 3 ):
            if(harf == '/'):
                counter = counter + 1
            anaUrl = anaUrl + harf
             
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    
    for link in soup.find_all('a',href=True):
        alturller1.append(link['href'])             
            
    for url in alturller1:
        if(len(url)>1): 
            if(url[0]=='/'):
                if url not in alturller2:
                    alturller2.append(url)
    ##if(len(alturller2)==0):
     ##   for url in alturller:
       ##     index = 0
         ##   index = url.find(anaUrl)
           ## print(url.find(anaUrl)) 
            ##if(index !=0):
              ##  alturller2.append(url)
    #for alturl in alturller2:
        #print(anaUrl+alturl)  
    
    for url in alturller2: 
        alturller.append(anaUrl+url)     
          
    return alturller

for alturl in alt_url_bulma(url):
    print(alturl)
    



    
    
    

#for url in alturller:
   
            #print(url)
    # url deki string  3üncü /'a gelene kadarını alır o bizim ana sayfamız olur sonra bu alturller buna eklenir.!!

#print(soup.find_all("p")) 
def sozlukolustur(tumkelimeler):
        kelimesayisi = {}

        for kelime in tumkelimeler:
            if kelime in kelimesayisi:
                kelimesayisi[kelime] += 1
            else:
                kelimesayisi[kelime] = 1
        return kelimesayisi

def sortWords(kelimesayisi):
    sortedkelimeler = {}
    for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
            sortedkelimeler[anahtar] = deger
    return 

def frekansbul(kelimesayisi):
    listeKelimeSayisi = list(kelimesayisi.items()) 
    liste = []
    count = -1
    while(count>=-6):
        liste.append(listeKelimeSayisi[count])
        count-=1
    return ConvertToDic(liste)

def ConvertToDic(liste):
    liste2 = []
    for i in range(0,len(liste)-1):
        liste2.append(liste[i][0])
        liste2.append(liste[i][1])
    it = iter(liste2)
    res_dct = dict(zip(it, it))
    return res_dct


       
def sembolleritemizle(tumkelimeler):
    sembolsuzkelimeler = []
    semboller = "!@$#^*()_+{}\"<>?,./:;[]''-=" + chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")

        if(len(kelime) > 0):
            sembolsuzkelimeler.append(kelime)
    return  sembolsuzkelimeler

    
    



