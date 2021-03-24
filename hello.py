from utils import parser
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
def c():
    if request.method == 'POST':
        url = request.form['url']
        returnValue = parser.func3(url)   
        return render_template('cevap_3.html', test=returnValue)
    return render_template('soru_3.html')

app.run(debug=False,host="localhost", port=int("777"))

