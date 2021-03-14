from flask import Flask
from flask import render_template
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from utils import parser
import operator

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
        frekans1Url = parser.func2(url)
        frekans2Url = parser.func2(url2) # burası 2.urlde ilk 5'i döndoruyor bize 2.url tamamı lazım
        sozluk2Url= parser.func1(url2) # burası bize 2.urldeki tüm sözlüğü döndürür.
        sozluk1ve2UrlOrtak = parser.included(frekans1Url,sozluk2Url)
        skor = parser.skorHesapla(sozluk1ve2UrlOrtak,sozluk2Url)
        return render_template('cevap_2.html', test=frekans1Url,test2=frekans2Url,test3=sozluk1ve2UrlOrtak,test4=skor)
    return render_template('soru_2.html')


app.run(host="localhost", port=int("777"))