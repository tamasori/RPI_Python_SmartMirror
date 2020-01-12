# Felhasználó dokumentáció - Smart Mirror

**Szerző**: Őri Tamás
**Neptun kód**: TKNM13
**Kurzus azonosító**: GKNB_INTM020
**Project megnevezés**: Okostükör

## Feladat

Okostükör telefonról elérhető kezelőfelülettel, távolságméréssel való automatikus kijelző kapcsolással, szoba hőmérséklet méréssel, Twitter, Google News és openweathermap API kapcsolattal.

## Környezet

- Raspberry Pi 3b+
- Raspbian operációs rendszer
- MongoDb
- Python3

**Szenzorok:**
- dht11 hőmérséklet szenzor
- ultrahang távolságmérő szenzor

## Felhasznált program és leíró nyelvek

 - Python3
 - CSS3
 - JavaScript
 - HTML
 - jSon
 - XML

## Felhasznált Python csomagok

**Alap csomagok:**

 - `requests`
 - `subprocess`
 - `urlopen`
 - `time`
 - `os`
 - `sys`

**Plusz csomagok:**

 - `RPi és RPi.GPIO`
 - `pymongo`
 - `Flask`
 - `Twython`

## Egyéb csomagok

- jQuery v3.4.1
- W3.CSS 4.13
- Chart.js v2.9.3

## Ötlet, tervezés

Az ötlet onnan jött, hogy már régóta akartam egy okos tükröt, több cikket olvastam róla, és így jó jött ki, hogy ezt ennek az órának a keretin belül tudtam elkészíteni. A tervekben szerepelt egy egyszerű kezelőfelület, hogy ne kelljen a mindig RDP vagy egér+billentyűzet segítségével csatlakozni a Pi-re, ha valamit változtatni akarok, vagy meg akarok nézni. Természetesen az elején mindig több tervvel indul az ember, és amiket tud megvalósít. Én is beszereztem egy hangerősség mérő szenzort, amivel azt volt a tervem, hogy tapsolásra is megjelennek az adatok, azonban ebből nem lett semmi végül, nem éreztem, hogy annyira fontos lenne. A távolságmérő és hőmérséklet mérőben biztos voltam, hogy alkalmazni akarom. A kijelző egy régi LCD TV nem a lebontott kijelzője a táppal és vezérlő elektronikával. Ennek a hátránya, hogy folyamatos háttér világítása van a kijelzőnek, és nagyon melegszik. A háttér világítás problémát a fényerő lejjebb vételével ki lehet küszöbölni, azonban a melegedés egy még most is fennálló gond lehet, ez a TV korának betudható. A megjelenítés kidolgozásában és a funkciókban sok ötletet merítettem a https://magicmirror.builders projektből, ami látszik is, azonban kódot nem használtam tőlük. A kijelző előtt egy 30%-os áteresztő üveglap található, ami fórumok szerint megfelelő, és a hely, ahol vettem, megerősítette ezt, azt mondták már másnak is adtak el okostükörhöz üveglapot, és ez a legjobb ár/érték arányban.

## Képek a kész projektről

![Raspberry Pi](https://lh3.googleusercontent.com/ApUY36n_5ZNQwPNcRGqjaG5XMcpt_iXTy5DZ58QxHMO9pGyiEq40z14eKuMGdXYchNGn073S0_SeeQMw5gGb6WsfluUkxyZCQf1c8877FsIFMK3s5lKQ5uXjv-zRKY8IhcOD3oEZdMF6TcAE28Rt8ESPc81ZHcgCPNCnMKjHZqbzTY33qRW4cF7Of9tJ_X0TV-bV13hT9m42c34YmmVNVeEINcpLHYHcJ9JUn1UZmAi4tzuYZYGijEkepbO2cHEdd6w0msY9tXsytmHXj-UoCmXAsmjhJZ7wcWWdhXJuL-ZWOhzctNrYJT0YJ577rjx_5DArrdrHk3aQdiuEeD5gO-QwLCdQYrzBLtNl030uhoBiY2frgMxQ_MYHHyk0MUMWxmy3Z4mPHoMyWGlZb1a-TvgNcodoya-dOwc3NWO9ncxX8XD9ru4hJBwGiQ6rx5bPWuV1L7gtl9tiVEJZlCnmfxdPYkzHm7wa8fdxWUFcJTIQ63H8L3emf1oLyMfTl7VAqg-PncZyziqqwQjTItFOznYJ6fo1fnQQG_p-CJUkfidH1spMlrcryuT_MyngiTkPseQk3YbQ9cGPXAvEYlMQ0rtXGz9x5u0XqPMC78H7QMamy5egoo81sT9TuBqvVbLGx-QN6ntk3ufxwQsoj3FLf8ZWCY9HagehoiOCaz3d7U3jrbS1nlrrBg=w1294-h970-no)

![Tükör 1](https://lh3.googleusercontent.com/fJWzTrdorpOUPEx9vRKs0l64Zee_QDDisTxw0M-Fia9VAEB4VWDXxrcZ9WOGRMjfPPSDU2TdjE-wHipOik37e_hKaUzJRj0A4BSOoL0JNhtFkyVVOvEmpp-u6YGbgIVJyy-3Ium716P2QKKrmT2Wn1qylbgPYbuujxxRS1li_FrdkF2b4MQjsNUwRVPhu5XyO-XPSD9fgE61r7pQaDg80fqbbsKclG-8F8ojeaITEQ4osg22CkslfqbjGjhGZTxMAgaM4ybevEppHhOmmYaLnt00Y-3YUHQ1UDXaB4Nm630rIvsBLSVGqZy9yDOuzD7jQrQU-ouzCNSRGrMaMZGUQ6RPslqWoH16ws8jMTqeslfaFxNiXV8Wv9VibqoR8L-gk3Ost5LACx7KMEaSVgKmRMdn57dGw947qX_z57K3vA9blxFMUw1L-HD8nRsWKszWduCq5jvzBcktbHunkfyCTPO5xI8g2LnalmlkNDpHo8yszkxs-7I64HS6AwGxWqHcbrldpByFF3H6JZA7Qaf3gfAdln4dWaIgaD8Afuj4GKMmjbOO1nXXc8Jvdj5-YW-SAYDN8l4KtuaDkhFvwm_l0IJsogHaeQ4rFI5G1NMVyIqnHlc8D77IjISs8T2iD4oPMaHU8Rzfj4EvEf9hZDvgG_xwKV6bxw8TvdUj6uY7ilqWaccnlhK8Bw=w1294-h970-no)

![Tükör 2](https://lh3.googleusercontent.com/kg1XiywBff4J9KIDx5qzrTP-O0OALYcgrhQ8hxBMsai6iIyT1K9JSJBSxFa2ffJlblujPo8WtVPiMfxQRdsiG9lVBt3OPhFBbyP7X978EuqM0QHqmNvjWjv9Z0h9ELmUS_dttDX6UE6p1lMtC5xF4_fxbisIMIsNXoq9UuDjMSIyONQWswQDMVbuS8P6mGwf3oMAKTVVdANSLr9vfaUzVGifUqqFxDz6EHSoTxz2xqcFjYFMgPV89MbzJo-QMcC5vwbdG0sDvqSNWf-Neg39KOWXtb11sBGDwnhaQuoh5KNG-4RPfCMeV3kRayYwe37WI40FmZ1PmzZS35YFpCm_hpeULPR6_lzrJRusNmVqC2NHVVDP3NcgrGAuntgXjSMW4hCChdoaFujBYR-dNP6C-UdMnlfe75HZQ1dTgvbYEddD0v-60DNSkFsgLSrT9Eag46NNIBdIiYcIkYeFJ_f_gA0GG-YhWAEuVgUGM17KnpQpdYyDxCQUjbs7ICcT5ER8vWGQ3dP8wUUiNv3NE6T4Dn8UWhgMzIeTntipYBz2YLHF5qgV4ISTamjx63oXGvBrO97IG0XjmOTB-WqKbwYfTNFh-vSuBC8HytDKepb-6pruKnXJfwK0fBxrhuMlpASFp3mv8lbimAGp18Sh_hYX3kR8o3c7JCcCFN7skalbB4wsyCy5cOGHTg=w1294-h970-no)
## Indítás

A rendszerben automatikus indításra lett beállítva:

- `app.py`
- chromium web böngésző teljes képernyős módban a `localhost/static` URL címmel

Ezek mellett még egy cronjob-ként van beállítva a `homeres_rogzites.py` , ami 15 percenként fut le és a szobahőmérséklet mérését és tárolását végzi.

## WiFi jeladás

Ezt a funkciót ki szeretném emelni. A Pi wifi egysége mint egy AP működik, azonban saját hálózattal. Saját privát címeket oszt, és ha csatlakozik egy másik WiFi-hez, internet elérésünk is van a Pi által közvetített WiFi-n. Ezt hosszú fórumozások után sikerült beállítani. A bejegyzés itt érhető el. https://www.raspberrypi.org/forums/viewtopic.php?t=206524

## Adatbázis

MongoDb adatbázis
A python program és az adatbázis között a `pymongo` csomag szolgáltatja a kapcsolatot.
Az adatbázis a `mongodb://localhost:27017/` címen érhető el

**Az adatbázis struktúrája:**

Adatbázis neve: `tukor`
Táblák:

- `homeres`: date, temperature
- `zip`: zip

## Kapcsolási rajz

![Kapcsolási rajz](https://lh3.googleusercontent.com/nB0s_xL2sSm92PswF71w0Zwcjjo_ZYTI4mWFflvwcG4cTBlzG2USH2IMVrjRmpu0OAy8QEPI8DSFYUDKEL596ibKiBPXETkXHFvj1SZxm3JbQuAvB9fOOxQvHw0tYB0MvF7y1PpSw-kNo4sfOzOnyhsa3IoI8ewPJq4UrxUNjQF8i7nPgTk62xJGnnhpJI_gZYOC1B4AiUQQbFKKWK6kTZXT6EIR6EoWa0dPJf8a9xQdrG5Ne0OOEC1kWnO8PBcIALhOEj4YamoanHOKNxz0SZy0drDpIO93Azt2Tv4DBuQ6DMIS4rfok7w3ITA6sM-lZSVfX7NDZGOsc-KLnXZ-cVN-sW6j6HzB-8nlH0jKXrpjpiOZXIdIKXtg3BjiyA-fGmgYW7WYGmgObqdcswqmSK4w35iyxliVqABkiAT6GockBm_kN5mP59ZJ-O78jJ6PJMtJEHGTzOu9kwYI15A_0iqOKLgrdcltCSIhVHVXop01hzZLtY7oxnUEqkYX9yBvP2ck6GCEpweed5T78WBlsrEYt819_LhR_g8mrz_IhBA8-gMxKtHWdege1SOra6f5XLZAgrUgM6LpAcEB-JazJI9DKgMt8y6lkx00mne2dFRc4QJdTOnuMwbsrVa4gNVmF_Z6j-p99NeWspGjLOnV_ulxliacoLxYFDxyziTgzbLS-UqvrMGp_w=w863-h970-no)

# Backend, frontend részek, modulok

## HDMI vezérlő:

A HDMI vezérlő, `hdmicontroller.py`, az ultrahangos távolságmérő mérései alapján, amennyiben a  távolság 1 méteren belül van, a hdmi jelet bekapcsolja, és ha 1 percig nem érzékel közelséget, akkor kikapcsolja a hdmi jelet.

A távolságot egy subprocess segítségével kéri le: 
`subprocess.check_output("python3 /home/pi/Okostukor/ultrasonic.py 100", shell=True)`

A hdmi jelkapcsolást pedig egy beépített Raspbian parancs vezérli: 
`subprocess.check_output("vcgencmd display_power", shell=True).decode('ascii')`

A méréseket 0.5 másodpercenként végzi el.

## Tweet modul

A Twitter kapcsolatot a `Twython` csomag végzi, és egy Twitter dev fiókkal van összekötve. Amennyiben a szoba hőmérséklete 18 celsius fok alá, vagy 28 celsius fok felé megy, akkor ez a Twitter dev fiók megemlít engem egy Tweetben, amiben értesít engem.

    val = subprocess.check_output("python3 /home/pi/Okostukor/homeres.py", shell=True)
    val = val.decode("ascii").strip()
    ...
    if  float(val) < 18.0:
	    subprocess.call('python3 /home/pi/Okostukor/tweet.py "@tams_ri Leesett a hőmérséklet a szobádban {0}°C fokra. Talán nyitvahagytad az ablakot?"'.format(val), shell=True)
    
    if  float(val) > 26.0:
	    subprocess.call('python3 /home/pi/Okostukor/tweet.py "@tams_ri Felszökött a hőmérséklet a szobádban {0}°C fokra. Talán elfelejtetted lekapcsolni a fűtést?"'.format(val), shell=True)

Ez a folyamat a `homeres_rogzites.py` fájl kerül futtatásra, ami a `homeres.py` segítségével és a `tweet.py` segítségével kerül végrehajtásra. A `homeres.py` végzi a mérést, a `tweet.py` pedig a kapcsolatot a Twitter és a program között.

## Szenzorok

**dht11:**
A dht11 egy hőmérséklet szenzor, amellyel a kommunikációt a `RPi.GPIO` csomag teremti meg. Van egy osztály `DHT11` névvel, ami a `dht11.py` fájlban található.  Ez a kapcsolatot teremtő fájl, egy hivatalos, kifejezetten a szenzorhoz írt letölthető osztály. A benne lévő kód nem az enyém, ezt csak felhasználom a többi fájlban, hogy kommunikációt tudjak létesíteni a szenzorral, és adatokat tudjak gyűjteni.

**ultrahangos távolságmérő szenzor:**
Az ultrahangos távolságmérő szenzorral a kommunikációt szintúgy a `RPi.GPIO` csomag teremti meg. Ehhez a szenzorhoz a kapcsolódó fájl az `ultrasonic.py`. Ebben a fájlban található `distance()` metódus, ami a jel visszaérkezésének ideje alapján számolja ki a távolságot a szenzor és a tükör előtti tárgy/személy között.

    def  distance():
	    GPIO.output(GPIO_TRIGGER, True)
	    time.sleep(0.00001)
	    GPIO.output(GPIO_TRIGGER, False)
	    StartTime = time.time()
	    StopTime = time.time()
	    while GPIO.input(GPIO_ECHO) == 0:
		    StartTime = time.time()
		    while GPIO.input(GPIO_ECHO) == 1:
			    StopTime = time.time()
			    TimeElapsed = StopTime - StartTime
			    distance = (TimeElapsed * 34300) / 2
	    return distance

## `app.py`

Az `app.py` egy összetettebb funkciójú fájl, ezért gondoltam, hogy erről külön írok.
Az `app.py` tartalmazza a program fő elemeit, a megjelenítés kezelését. Induláskor elindít egy Flask szerver/WSGI szolgáltatást a 80-as porton.
 `app.run(host='0.0.0.0',debug=True, port=80)`
8 útvonal van definiálva, amelyek mindegyike egy saját funkcióval bír.

    @app.route('/')
    def  beallitas():
	    return render_template('beallitas.html')
	    
Az első ilyen a *gyökérútvonal* amely a `templates/beallitas.html` fájlt küldi válaszként. Ebben található a felhasználó által elérhető oldal, amin keresztül az adatokat tudjuk frissíteni. Két form található benne, egy a tartózkodási hely beállításához, egy pedig a WiFi adatok beállításához.
A tartózkodási hely beállításához a `/zip` címre küld egy `POST` kérést, amiben a `zip` nevű bemeneti mező tartalmát küldi el.  Ezt a következő kód dolgozza fel.

    @app.route('/zip', methods=['POST'])
    def  zip_beallitas():
	    db["zip"].delete_many({})
	    db["zip"].insert_one({'zip':request.form['zip']})
	    return redirect('/')

Itt beillesztésre kerül az adatbázisba az új irányítószám.
A másik form a WiFi adatok frissítésével kapcsolatos, itt az SSID és a jelszó mezők kerülnek `POST` kéréssel a következő metódushoz.

    @app.route('/wifi', methods=['POST'])
    def  wifi_beallitas():
	    if  len(request.form['jelszo'])>=8  and  len(request.form['jelszo'])<=30:
		    with  open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as myfile:
			    myfile.write('\nnetwork={\nssid="'+request.form['ssid']+'"\npsk="'+request.form['jelszo']+'"\n}\n')
			    subprocess.call('sudo wpa_cli -i wlan0 reconfigure', shell=True)
	    return redirect('/')
Itt az látható, hogy a program átírja az adatok a Raspbian megfelelő fájlában, és egy beépített parancs segítségével frissíti a beállításokat.

    subprocess.call('sudo wpa_cli -i wlan0 reconfigure', shell=True)

Ezen az oldalon található egy link a `/meresek` oldalhoz, amely a dht11 szenzor által mért adatokat jeleníti meg egy grafikon segítségével időbélyegekkel ellátva.

    @app.route('/meresek')
    def  meresek():
	    x = db['homeres'].find({})
	    adatok = []
	    for i in x:
		    adatok.append(i)
	    return render_template('meresek.html', adatok=adatok)

Amint látható, ez az oldal az `adatok` változón keresztül kapja meg a méréseket, amiket pedig a chart.js dolgoz fel a következő kóddal.

    <script>
	    var  ctx = document.getElementById('chart').getContext('2d');
	    var  chart = new  Chart(ctx, {
		    type:  'line',
		    data: {
			    labels: [{% for adat in adatok %}'{{adat.date}}', {% endfor %}],
			    datasets: [{
				    label:  'Hőmérsékletek',
				    data: [{% for adat in adatok %}{{adat.temperature}}, {% endfor %}],
				    backgroundColor:  "rgba(255,0,0,0.5)",
				    pointBackgroundColor:  "rgba(0,0,0,0.8)",
				    pointBorderColor:  "rgba(0,0,0,0.8)",
		    }],
	    },
	    options: {
		    scales: {
			    yAxes: [{
				    ticks: {
					    beginAtZero:  true
				    }
			    }]
		    }
	    }
    });
    </script>

A tökrön közvetlenül a `/tukor` URL kerül megnyitásra, aminek a rendere pedig így néz ki. 

    @app.route('/tukor')
    def  tukor():
	    return render_template('tukor.html')

A `tukor.html` időnként kéréseket küld a következő címekre:

`/idojaras`: Az időjárást kéri le a openweathermap API segítségével.

    @app.route('/idojaras')
    def  idojaras():
        zip = db["zip"].find_one()['zip']
        if  zip != None:
	        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip+',hu&APPID=eb6da1b099c89e175bdbc1e60459f5bd&lang=hu&units=metric')
	        return r.text
        return  ""

Az adatokat jSon formátumban kapja meg a következő JavaScript metódus, ami 3 másodpercenként küld kérést.

    function  idojaras_lekeres(){
	    $.get("/idojaras", function(data, status){
		    data = JSON.parse(data);
		    $('#homerseklet').text(Math.floor(data.main.temp*10)/10 + " °C");
		    $('#hely').text(data.name);
		    $('#szel').text(data.wind.speed+" km/h");
		    icon_kod = data.weather[0].icon;
		    if(icon_kod != '01d' && icon_kod != '01n'){
			    icon_kod = icon_kod.substring(0, icon_kod.length - 1);
		    }
		    $('#icon').attr('src', "/static/kepek/"+ icon_kod+".png");
		    console.log(data);
	    });
    }

Az pontos dátum és idő pedig a következő kód frissíti másodpercenként.

    function  ido_lekeres(){
	    var  most = new  Date();
	    var  h = most.getHours();
	    var  m = nullak_hozzaadasa(most.getMinutes());
	    var  s = nullak_hozzaadasa(most.getSeconds());
	    $("#pontos_ido").text(h + ":" + m + ":" + s);
	    
	    var  y = most.getFullYear();
	    var  M = nullak_hozzaadasa(most.getUTCMonth()+1);
	    var  d = nullak_hozzaadasa(most.getDate());
	    $("#datum").text(y+"."+M+"."+d+".");
	    
	    var  napok = new  Array(7);
	    napok[0] = "Vasárnap";
	    napok[1] = "Hétfő";
	    napok[2] = "Kedd";
	    napok[3] = "Szerda";
	    napok[4] = "Csütörtök";
	    napok[5] = "Péntek";
	    napok[6] = "Szombat";
	    var  nap = napok[most.getDay()];
	    $("#nap").text(nap);
    }

A hírek a Google News segítségével kerülnek lekérésre. A lekéréseket a `/hirek` URL segítségével egy sima `GET` metódussal kerülnek átadásra XML formátumban. Ezt a lekérést 30 percenként futtatjuk le.

    @app.route('/hirek')
    def  hirek():
	    r = requests.get('https://news.google.com/rss?hl=hu&gl=HU&ceid=HU:hu')
	    return r.text

Az oldalon a TOP 5 hír jelenik meg, 8 másodpercenként váltogatva a híreket. 

    function  hirek_lekerese(){
	    $.get("/hirek", function(data, status){
		    xmlDoc = $.parseXML(data);
		    $xml = $(xmlDoc);
		    hirek = [];
		    $xml.find("item title").slice(0, 5).each(function(){
			    hirek.push($(this).text())
		    });
		    hirek_mutatasa();
	    });
    }
    
      
    function  hirek_mutatasa(){
	    $('#aktualis_hir').fadeOut(function(){
		    $(this).text(hirek[aktualis_hir_id]).fadeIn()
		});
	    aktualis_hir_id++;
	    if(aktualis_hir_id > 4){
		    aktualis_hir_id = 0;
	    }
    }

Ezeken kívül még másodpercenként ellenőrzi a program, hogy van-e éles, működő internetkapcsolata.  Ezt a google.com pingelésével deríti ki a program. Ha 5 másodpercen belül nem kap választ, a program azt feltételezi, hogy nincs éles internetkapcsolat.

    @app.route('/vannet')
    def  vannet():
	    try:
		    response = urlopen('https://www.google.com/', timeout=5)
		    return  "van"
	    except:
		    return  "nincs"
	//JS
    function  van_net(){
	    $.get("/vannet", function(data, status){
	    if(data=="van"){
		    $("#idojaras").show();
		    $("#hirek").show();
		    $("#nincsnet").hide();
	    }else{
		    $("#idojaras").hide();
		    $("#hirek").hide();
		    $("#nincsnet").show();
	    }
	    });
    }

