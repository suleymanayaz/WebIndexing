from utils import parser
from utils import ObjectUrl
from flask import Flask
from flask import render_template
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Web indexleme Deneme Surumu '

@app.route('/soru_1', methods=('GET', 'POST'))
def soru_1():
    if request.method == 'POST':
        gelenUrl = request.form['url']
        temiz_kelime_sozlugu = parser.kelime_sozluk_olusturma(gelenUrl)    ## func1 == kelime_sozluk_olusturma
        return render_template('cevap_1.html', temiz_kelime_sozlugu=temiz_kelime_sozlugu)

    return render_template('soru_1.html')

@app.route('/soru_2',methods=('GET', 'POST'))
def soru_2():
    if request.method == 'POST':
        gelenurl = request.form['url']
        gelenurl2= request.form['url2']
        temiz_kelime_sozlugu= parser.kelime_sozluk_olusturma(gelenurl)
        temiz_kelime_sozlugu_2= parser.kelime_sozluk_olusturma(gelenurl2)  
        frekans1Url = parser.kelime_frekans_siralama(gelenurl)
        frekans2Url = parser.kelime_frekans_siralama(gelenurl2) 
        ortak_sozluk = parser.included(frekans1Url,frekans2Url)
        skor = parser.skorHesapla(frekans1Url,frekans2Url)
        return render_template('cevap_2.html',temiz_kelime_sozlugu=temiz_kelime_sozlugu,temiz_kelime_sozlugu_2=temiz_kelime_sozlugu_2, frekans1Url=frekans1Url,frekans2Url=frekans2Url,ortak_sozluk = ortak_sozluk,skor=skor)
    return render_template('soru_2.html')

@app.route('/soru_3',methods=('GET', 'POST'))
def soru_3():
    if request.method == 'POST':
        anaUrl = request.form['url']
        anaUrlSozluk = parser.kelime_sozluk_olusturma(anaUrl)
        anaUrlFrekans = parser.kelime_frekans_siralama(anaUrl)
        #print(anaUrlFrekans)
        anaUrlObject = ObjectUrl.AnaUrl(anaUrl,anaUrlSozluk,anaUrlFrekans,0,1)
        anaUrlObject.altUrller.clear()
        anaUrlObject.altUrller_skor.clear()
        altUrller = parser.txt_okunan_urller()
      
        for altUrl in altUrller:
           
            print("1.SEVİYE : "+altUrl)            
            altUrlSozluk = parser.kelime_sozluk_olusturma(altUrl)
            altUrlFrekans = parser.kelime_frekans_siralama(altUrl) 
            skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)    
            altUrlObject = ObjectUrl.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,1)
            anaUrlObject.alturl_ekle(altUrlObject)
      
        for altUrlObject in anaUrlObject.altUrller:
            altinaltUrller = parser.alt_url_bulma(altUrlObject.anaUrl)
            for altUrl in altinaltUrller:
                 print("2.SEVİYE : "+altUrl)
                 altUrlSozluk = parser.kelime_sozluk_olusturma(altUrl)
                 altUrlFrekans = parser.kelime_frekans_siralama(altUrl)
                 skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)   
                 altUrlObject1 = ObjectUrl.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,2)
                 altUrlObject.alturl_ekle(altUrlObject1)
                 
                 for altUrlObject in altUrlObject.altUrller:
                     altinaltUrller = parser.alt_url_bulma(altUrlObject.anaUrl)
                     for altUrl in altinaltUrller:
                         print("3.SEVİYE : "+altUrl)
                         altUrlSozluk = parser.kelime_sozluk_olusturma(altUrl)
                         altUrlFrekans = parser.kelime_frekans_siralama(altUrl)
                         skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)   
                         altUrlObject1 = ObjectUrl.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,3)
                         altUrlObject.alturl_ekle(altUrlObject1)   
                 
                 
        for altUrlObject in anaUrlObject.altUrller:
            #print(anaUrlObject.frekans)
            #print("---")
            anaUrlObject.altUrller_skor[altUrlObject] = altUrlObject.skor
            for altUrlObject1 in altUrlObject.altUrller:
                anaUrlObject.altUrller_skor[altUrlObject1] = altUrlObject1.skor
                for altUrlObject2 in altUrlObject1.altUrller:
                    anaUrlObject.altUrller_skor[altUrlObject2] = altUrlObject2.skor
                    
        anaUrlObject.sortSkor(parser.sortWords(anaUrlObject.altUrller_skor))
      
       
        return render_template('cevap_3.html', anaUrlObject=anaUrlObject,anaUrlObject_Skor_Sozluk=anaUrlObject.altUrller_skor_reverse)
    return render_template('soru_3.html')


@app.route('/soru_4',methods=('GET', 'POST'))
def soru_4():
    if request.method == 'POST':
        anaUrl = request.form['url']
        anaUrlSozluk = parser.kelime_sozluk_olusturma(anaUrl)
        anaUrlFrekans = parser.kelime_frekans_siralama(anaUrl)
        esAnlamli = parser.esAnlamliKelimeCikarma(anaUrlSozluk)
        #print(anaUrlFrekans)
        anaUrlObject = ObjectUrl.AnaUrl(anaUrl,anaUrlSozluk,anaUrlFrekans,0,1)
        anaUrlObject.esAnlamli_ekle(esAnlamli)
        anaUrlObject.altUrller.clear()
        anaUrlObject.altUrller_skor.clear()
        altUrller = parser.txt_okunan_urller()
    
        for altUrl in altUrller:
           
            print("1.SEVİYE : "+altUrl)            
            altUrlSozluk = parser.kelime_sozluk_olusturma(altUrl)
            altUrlFrekans = parser.kelime_frekans_siralama(altUrl) 
            esAnlamli = parser.esAnlamliKelimeCikarma(altUrlSozluk)
            skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)    
            altUrlObject = ObjectUrl.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,1)
            altUrlObject.esAnlamli_ekle(esAnlamli)
            anaUrlObject.alturl_ekle(altUrlObject)
        
        for altUrlObject in anaUrlObject.altUrller:
            altinaltUrller = parser.alt_url_bulma(altUrlObject.anaUrl)
            for altUrl in altinaltUrller:
                 print("2.SEVİYE : "+altUrl)
                 altUrlSozluk = parser.kelime_sozluk_olusturma(altUrl)
                 altUrlFrekans = parser.kelime_frekans_siralama(altUrl)
                 esAnlamli = parser.esAnlamliKelimeCikarma(altUrlSozluk)
                 skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)   
                 altUrlObject1 = ObjectUrl.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,2)
                 altUrlObject1.esAnlamli_ekle(esAnlamli)
                 altUrlObject.alturl_ekle(altUrlObject1)
                 
                 for altUrlObject in altUrlObject.altUrller:
                     altinaltUrller = parser.alt_url_bulma(altUrlObject.anaUrl)
                     for altUrl in altinaltUrller:
                         print("3.SEVİYE : "+altUrl)
                         altUrlSozluk = parser.kelime_sozluk_olusturma(altUrl)
                         altUrlFrekans = parser.kelime_frekans_siralama(altUrl)
                         esAnlamli = parser.esAnlamliKelimeCikarma(altUrlSozluk)
                         skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)   
                         altUrlObject1 = ObjectUrl.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,3)
                         altUrlObject1.esAnlamli_ekle(esAnlamli)
                         altUrlObject.alturl_ekle(altUrlObject1)   
                 
                 
        for altUrlObject in anaUrlObject.altUrller:
            #print(anaUrlObject.frekans)
            #print("---")
            anaUrlObject.altUrller_skor[altUrlObject] = altUrlObject.skor
            for altUrlObject1 in altUrlObject.altUrller:
                anaUrlObject.altUrller_skor[altUrlObject1] = altUrlObject1.skor
                for altUrlObject2 in altUrlObject1.altUrller:
                    anaUrlObject.altUrller_skor[altUrlObject2] = altUrlObject2.skor
                    
        anaUrlObject.sortSkor(parser.sortWords(anaUrlObject.altUrller_skor))
       
       
        return render_template('cevap_4.html', anaUrlObject=anaUrlObject,anaUrlObject_Skor_Sozluk=anaUrlObject.altUrller_skor_reverse)
    return render_template('soru_4.html')




app.run(debug=False,host="localhost", port=int("999"))

