import requests
from bs4 import BeautifulSoup
import operator
import nltk
import math 
from nltk.corpus import stopwords




def sozlukolustur(tumkelimeler):
    kelimesayisi = {} # sözlük
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
    counter = len(kelimesayisi)
    if counter >= 10:
        sa = -10
    else:
        sa = -counter
        
    if counter !=0:
        while(count>=-counter): # burda -10 ' u -counter olarak yazarsak ekrana tum kelimeleri basar #-1  >= -10 
            liste.append(listeKelimeSayisi[count]) ## kücükten büyüğe sıralamıştık  ## -2 >= -10 
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
    for kelime,kelime_tekrar_sayisi in kelimesayisi.items():     
        for stopWords in stopwords.words('turkish'):
            if(kelime==stopWords):
                stopsWord.append(kelime)
                
    for kelime in stopsWord:
        del kelimesayisi[kelime] ## nlkt deki stop kelimeler cıkarılıyor
        
    #----- silinebilir ---------------------------------------
    stopsWord.clear()
    for anahtar,deger in kelimesayisi.items():        
        for stopWords in stopwords.words('english'):
            if(anahtar==stopWords):
                stopsWord.append(anahtar)
    for kelime in stopsWord:
        del kelimesayisi[kelime] ## nlkt deki stop kelimeler cıkarılıyor
   #----- silinebilir ---------------------------------------     
   
    ftest = open("static/dahilistopword.txt",encoding="utf-8")
    haricistopwords =[]
    for words in ftest.readlines():
        haricistopwords.append(words.split())
    ftest.close()
    
    stopsWord.clear()
    for anahtar,deger in kelimesayisi.items():        
       for kelime in haricistopwords:
           hariciKelimeString = listToString(kelime)
           if hariciKelimeString == anahtar:
               stopsWord.append(anahtar)

    for kelime in stopsWord:  
        if kelimesayisi.get(kelime) != None:
            del kelimesayisi[kelime]  ## bizim eklediğimiz stop kelimeler cıkarılıyor
    
    
    return kelimesayisi

def esAnlamliKelimeCikarma(kelimesayisi):
    ftest = open("static/kelime-esanlamlisi.txt",encoding="utf-8")
    esAnlamliKelimeler =[]
    bulunanKelimelerEsAnlamlari = []
    bulunanKelimelerEsAnlamlari1 = []
    for words in ftest.readlines():
        esAnlamliKelimeler.append(words.split())
    ftest.close()
    
    for anahtar,deger in kelimesayisi.items():
        for satir in esAnlamliKelimeler:
            if satir[0] == anahtar :
                if len(satir) == 2:
                    bulunanKelimelerEsAnlamlari.append(satir)
                    
    for satir in bulunanKelimelerEsAnlamlari:
        for anahtar,deger in kelimesayisi.items():
            if satir[1] == anahtar:
                bulunanKelimelerEsAnlamlari1.append(satir)
                
    return bulunanKelimelerEsAnlamlari1
    

    
    
def included(getSozluk,get2Sozluk):
    includedKelimeler = {}
    for anahtar,deger in getSozluk.items():
        if(checkKey(get2Sozluk,anahtar) == 0):
            includedKelimeler[anahtar]=returnValue(get2Sozluk,anahtar)
    return includedKelimeler   

def skorHesapla(get1Sozluk,get2Sozluk):
    numerator = benzerlik_hesaplama(get1Sozluk,get2Sozluk)  
    denominator = math.sqrt(benzerlik_hesaplama(get1Sozluk,get1Sozluk)*benzerlik_hesaplama(get2Sozluk, get2Sozluk))  
    if(denominator != 0):
        deger = math.acos(numerator / denominator) 
        deger = deger*(180/math.pi)
    else:
        deger = 99
    #print("The distance between the documents is: % 0.6f (radians)"% deger) 
    return deger

def benzerlik_hesaplama(getsozluk,get1sozluk):
    sum=0.0
    for key in getsozluk:
        if key in get1sozluk:
            sum+=(getsozluk[key]*get1sozluk[key])
            
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
    
def kelime_sozluk_olusturma_div(getUrl):
    tumkelimeler = []
    r = requests.get(getUrl)
    soup = BeautifulSoup(r.content,"html.parser")
    for kelimegruplari in soup.find_all("div"):
        icerik = kelimegruplari.text
        kelimeler = icerik.lower().split()

        for kelime in kelimeler:
            tumkelimeler.append(kelime)
            # print(kelime)
        tumkelimeler = sembolleritemizle(tumkelimeler)
    kelimesayisi = sozlukolustur(tumkelimeler)
    
    return kelimesayisi


    
def kelime_sozluk_olusturma(getUrl):
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
    if(len(kelimesayisi) == 0):
        print("p tagında kelime yok")
        kelimesayisi = kelime_sozluk_olusturma_div(getUrl)
        
    kelimesayisi = sortWords(kelimesayisi)
    kelimesayisi = gereksizKelimeCikarma(kelimesayisi)
    
   
    return kelimesayisi

    
def kelime_frekans_siralama(getUrl):
    kelimesayisi = kelime_sozluk_olusturma(getUrl)
     
    frekans = frekansbul(kelimesayisi)    
    
    return frekans



def alt_url_bulma(getUrl):
    alturller = []
    alturller1 = []
    alturller2 = []
    alturller3 = []
    counter=0
    #index = 0
    anaUrl = ""
    for harf in getUrl:
        if(counter < 3 ):
            if(harf == '/'):
                counter = counter + 1
            anaUrl = anaUrl + harf
    
    anaUrl = anaUrl[:-1]         
    r = requests.get(getUrl)
    soup = BeautifulSoup(r.content,"html.parser")
    
    for link in soup.find_all('a',href=True):
        alturller1.append(link['href'])             
            
    for url in alturller1:
        if(len(url)>1): 
            if(url[0]=='/'):
                if url not in alturller2:
                    alturller2.append(url)
    
    
    for url in alturller1:
        if anaUrl in url:
            if url not in alturller3:
               alturller3.append(url)
              
        
    
    for url in alturller2: 
        alturller.append(anaUrl+url)     
        
    altUrllerr = alturller+alturller3
  
    return altUrllerr

def txt_okunan_urller():
    okunanUrllerListe = []
    okunanaUrller = []
    ftest = open("static/urllist.txt",encoding="utf-8")
    for words in ftest.readlines():
        okunanUrllerListe.append(words.split())
    ftest.close()
    
    for urller in okunanUrllerListe:
          print(type(urller[0]))
          okunanaUrller.append(urller[0])
          
    
    return okunanaUrller
    
    
    
    
    
    
  
       






 
    

       
    
    
    
    
    
        
    

        

