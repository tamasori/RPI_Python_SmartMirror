from flask import Flask, render_template, request, redirect
import requests
import pymongo
import subprocess
from urllib.request import urlopen

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["tukor"]

app = Flask(__name__, static_url_path='/static')

@app.route('/tukor')
def tukor():
    return render_template('tukor.html')

@app.route('/')
def beallitas():
    return render_template('beallitas.html')

@app.route('/meresek')
def meresek():
    x = db['homeres'].find({})
    adatok = []
    for i in x:
        adatok.append(i)
    return render_template('meresek.html', adatok=adatok)

@app.route('/idojaras')
def idojaras():
    zip = db["zip"].find_one()['zip']
    if zip != None:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip+',hu&APPID=eb6da1b099c89e175bdbc1e60459f5bd&lang=hu&units=metric')
        return r.text
    return ""

@app.route('/hirek')
def hirek():
    r = requests.get('https://news.google.com/rss?hl=hu&gl=HU&ceid=HU:hu')
    return r.text

@app.route('/zip', methods=['POST'])
def zip_beallitas():
    db["zip"].delete_many({})
    db["zip"].insert_one({'zip':request.form['zip']})
    return redirect('/')

@app.route('/wifi', methods=['POST'])
def wifi_beallitas():
    if len(request.form['jelszo'])>=8 and len(request.form['jelszo'])<=30:
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as myfile:
            myfile.write('\nnetwork={\nssid="'+request.form['ssid']+'"\npsk="'+request.form['jelszo']+'"\n}\n')
            subprocess.call('sudo wpa_cli -i wlan0 reconfigure', shell=True)
    return redirect('/')

@app.route('/vannet')
def vannet():
    try:
        response = urlopen('https://www.google.com/', timeout=5)
        return "van"
    except:
        return "nincs"


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=80)

#https://raspberrypi.stackexchange.com/questions/69204/open-chromium-full-screen-on-start-up
