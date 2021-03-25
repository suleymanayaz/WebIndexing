import requests
from bs4 import BeautifulSoup
import operator
import nltk
import math 
from nltk.corpus import stopwords




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
def sortWords2(kelimesayisi):
    sortedkelimeler = {}
    for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)):
            sortedkelimeler[anahtar] = deger
    return sortedkelimeler

def frekansbul(kelimesayisi):
    listeKelimeSayisi = list(kelimesayisi.items()) 
    liste = []
    count = -1
    counter = len(kelimesayisi)
    if counter >= 10:
        sa = -10
    else:
        sa = -counter
    if counter !=0:
        while(count>=-counter): # burda -10 ' u -counter olarak yazarsak ekrana tum kelimeleri basar
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


def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
def gereksizKelimeCikarma(kelimesayisi):
    stopsWord = []
    for anahtar,deger in kelimesayisi.items():        
        for stopWords in stopwords.words('turkish'):
            if(anahtar==stopWords):
                stopsWord.append(anahtar)
    for kelime in stopsWord:
        del kelimesayisi[kelime] ## nlkt deki stop kelimeler cıkarılıyor
    stopsWord.clear()
    for anahtar,deger in kelimesayisi.items():        
        for stopWords in stopwords.words('english'):
            if(anahtar==stopWords):
                stopsWord.append(anahtar)
    for kelime in stopsWord:
        del kelimesayisi[kelime] ## nlkt deki stop kelimeler cıkarılıyor
            
    ftest = open("static/a.txt",encoding="utf-8")
    ellestopwords =[]
    for words in ftest.readlines():
        ellestopwords.append(words.split())
    ftest.close()
    stopsWord.clear()
    for anahtar,deger in kelimesayisi.items():        
       for kelime in ellestopwords:
           kelime2 = listToString(kelime)
           if kelime2 == anahtar:
               stopsWord.append(anahtar)

    for kelime in stopsWord:
        if kelimesayisi.get(kelime) != None:
            del kelimesayisi[kelime]  ## bizim eklediğimiz stop kelimeler cıkarılıyor
    
    
    return kelimesayisi

def included(getSozluk,get2Sozluk):
    includedKelimeler = {}
    for anahtar,deger in getSozluk.items():
        if(checkKey(get2Sozluk,anahtar) == 0):
            includedKelimeler[anahtar]=returnValue(get2Sozluk,anahtar)
    return includedKelimeler   

def skorHesapla(get1Sozluk,get2Sozluk):
    numerator = dotProduct(get1Sozluk,get2Sozluk)
    
    denominator = math.sqrt(dotProduct(get1Sozluk,get1Sozluk)*dotProduct(get2Sozluk, get2Sozluk))  
    if(denominator != 0):
        deger = math.acos(numerator / denominator) 
        deger = deger*(180/math.pi)
    else:
        deger = 99
    #print("The distance between the documents is: % 0.6f (radians)"% deger) 
    return deger

def dotProduct(d1,d2):
    sum=0.0
    for key in d1:
        if key in d2:
            sum+=(d1[key]*d2[key])
            
    return sum    

def allSumValue(gel):
   print(sum(gel.values()))
   return sum(gel.values())
       
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return 0
    else: 
        return 1

def returnValue(dict,key):
    if key in dict.keys(): 
        return dict[key]    
    
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
    kelimesayisi = gereksizKelimeCikarma(kelimesayisi)
    
   
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
        tumkelimeler = sembolleritemizle(tumkelimeler)
        
    kelimesayisi = sozlukolustur(tumkelimeler)
    kelimesayisi = sortWords(kelimesayisi)
    kelimesayisi = gereksizKelimeCikarma(kelimesayisi)
        
    frekans = frekansbul(kelimesayisi)    
    
    return frekans

def func3(getUrl):
    alturller = []
    alturller1 = []
    alturller2 = []
    counter=0
    #index = 0
    anaUrl = ""
    for harf in getUrl:
        if(counter < 3 ):
            if(harf == '/'):
                counter = counter + 1
            anaUrl = anaUrl + harf
          
            
    print(anaUrl)      
    r = requests.get(getUrl)
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

  
       






 
    

       
    
    
    
    
    
        
    

        

