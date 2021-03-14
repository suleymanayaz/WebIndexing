import requests
from bs4 import BeautifulSoup
import operator


def sozlukolustur(tumkelimeler):
    kelimesayisi = {}
    for kelime in tumkelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] +=1
        else:
            kelimesayisi[kelime] = 1
    return kelimesayisi     
                   
       
        
def sembolleritemizle(tumkelimeler):
        sembolsuzkelimeler = []
        semboller = "!@$#^*()_+{}\"<>?,./:;[]''-=" + chr(775)
        for kelime in tumkelimeler:
            for sembol in semboller:
                if sembol in kelime:
                    kelime = kelime.replace(sembol,"")
                    
            if(len(kelime)>0):
                sembolsuzkelimeler.append(kelime)
        return sembolsuzkelimeler
    
def sortWords(kelimesayisi):
    sortedkelimeler = {}
    for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
            sortedkelimeler[anahtar] = deger
    return sortedkelimeler

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

def func1(getUrl):
    tumkelimeler= []
    r = requests.get(getUrl)
    soup = BeautifulSoup(r.content,"html.parser")
    for kelimegruplari in soup.find_all("p"):
        icerik = kelimegruplari.text
        kelimeler = icerik.lower().split()

        for kelime in kelimeler:
            tumkelimeler.append(kelime)
            # print(kelime)
        tumkelimeler = sembolleritemizle(tumkelimeler)

        kelimesayisi = sozlukolustur(tumkelimeler)
        kelimesayisi = sortWords(kelimesayisi)
       
        
    return kelimesayisi


def func2(getUrl):
    tumkelimeler= []
    r = requests.get(getUrl)
    soup = BeautifulSoup(r.content,"html.parser")
    for kelimegruplari in soup.find_all("p"):
        icerik = kelimegruplari.text
        kelimeler = icerik.lower().split()

        for kelime in kelimeler:
            tumkelimeler.append(kelime)
            # print(kelime)
        tumkelimeler = sembolleritemizle(tumkelimeler)

        kelimesayisi = sozlukolustur(tumkelimeler)
        kelimesayisi = sortWords(kelimesayisi)
       
    frekans = frekansbul(kelimesayisi)    
    return frekans


def included(getSozluk,get2Sozluk):
    includedKelimeler = {}
    for anahtar,deger in getSozluk.items():
        if(checkKey(get2Sozluk,anahtar) == 0):
            includedKelimeler[anahtar]=returnValue(get2Sozluk,anahtar)
    return includedKelimeler         
       
def skorHesapla(includedKelimeler,get1Sozluk,get2Sozluk):
    temp = 1
    tumkelimeFrekans1 = allSumValue(get2Sozluk)
    tumkelimeFrekans2 = allSumValue(get1Sozluk)
    for anahtar,deger in includedKelimeler.items():
        print(deger)
        temp +=deger
    skor =  2*temp / (tumkelimeFrekans1+tumkelimeFrekans2)
    
    return skor*100


def allSumValue(gel):
   print(sum(gel.values()))
   return sum(gel.values())
       
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        #print("Present, ", end =" ") 
        #print("value =", dict[key]) 
        return 0
    else: 
        #print("Not present") 
        return 1

def returnValue(dict,key):
    if key in dict.keys(): 
        return dict[key]
 

        
    

        

