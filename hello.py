from utils import parser
from utils import url
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
def a():
    if request.method == 'POST':
        url = request.form['url']
        returnValue = parser.func1(url)   
        return render_template('cevap_1.html', test=returnValue)

    return render_template('soru_1.html')

@app.route('/soru_2',methods=('GET', 'POST'))
def b():
    if request.method == 'POST':
        url = request.form['url']
        url2= request.form['url2']
        sozluk1Url= parser.func1(url)
        sozluk2Url= parser.func1(url2)
        frekans1Url = parser.func2(url)
        frekans2Url = parser.func2(url2) 
        sozluk1ve2UrlOrtak = parser.included(frekans1Url,frekans2Url)
        skor = parser.skorHesapla(frekans1Url,frekans2Url)
        return render_template('cevap_2.html',test=sozluk1Url,test2=sozluk2Url, test3=frekans1Url,test4=frekans2Url,test5 = sozluk1ve2UrlOrtak,test6=skor)
    return render_template('soru_2.html')

@app.route('/soru_3',methods=('GET', 'POST'))
def d():
    if request.method == 'POST':
        anaUrl = request.form['url']
        anaUrlSozluk = parser.func1(anaUrl)
        anaUrlFrekans = parser.func2(anaUrl)
        print(anaUrlFrekans)
        anaUrlObject = url.AnaUrl(anaUrl,anaUrlSozluk,anaUrlFrekans,0,1)
        anaUrlObject.altUrller.clear()
        anaUrlObject.altUrller_skor.clear()
        altUrller = parser.func3(anaUrl)   


        return render_template('cevap_3.html', anaUrlisim = anaUrl,test = altUrller)
    return render_template('soru_3.html')


@app.route('/soru_4',methods=('GET', 'POST'))
def c():
    if request.method == 'POST':
        anaUrl = request.form['url']
        anaUrlSozluk = parser.func1(anaUrl)
        anaUrlFrekans = parser.func2(anaUrl)
        print(anaUrlFrekans)
        anaUrlObject = url.AnaUrl(anaUrl,anaUrlSozluk,anaUrlFrekans,0,1)
        anaUrlObject.altUrller.clear()
        anaUrlObject.altUrller_skor.clear()
        altUrller = parser.func3(anaUrl)   
        for altUrl in altUrller:
            print("1.SEVİYE : "+altUrl)

            
            altUrlSozluk = parser.func1(altUrl)
            altUrlFrekans = parser.func2(altUrl) 
            skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)    
            altUrlObject = url.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,2)
            anaUrlObject.alturl_ekle(altUrlObject)
        
        for altUrlObject in anaUrlObject.altUrller:
            altinaltUrller = parser.func3(altUrlObject.anaUrl)
            for altUrl in altinaltUrller:
                 print("2.SEVİYE : "+altUrl)
                 altUrlSozluk = parser.func1(altUrl)
                 altUrlFrekans = parser.func2(altUrl)
                 skor = parser.skorHesapla(anaUrlFrekans,altUrlFrekans)   
                 altUrlObject1 = url.AnaUrl(altUrl,altUrlSozluk,altUrlFrekans,skor,3)
                 altUrlObject.alturl_ekle(altUrlObject1)
                 
        for altUrlObject in anaUrlObject.altUrller:
            #print(anaUrlObject.frekans)
            #print("---")
            anaUrlObject.altUrller_skor[altUrlObject.anaUrl] = altUrlObject.skor
            for altUrlObject1 in altUrlObject.altUrller:
                anaUrlObject.altUrller_skor[altUrlObject1.anaUrl] = altUrlObject1.skor
        
        anaUrlObject.sortSkor(parser.sortWords2(anaUrlObject.altUrller_skor))

        return render_template('cevap_4.html', anaUrlisim = anaUrl,test = altUrller,test1=anaUrlObject.altUrller_skor_reverse)
    return render_template('soru_4.html')

app.run(debug=False,host="localhost", port=int("999"))

