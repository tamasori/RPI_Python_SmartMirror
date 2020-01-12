# Felhasználó dokumentáció - Smart Mirror 

## Kezdeti lépések

 1. A tükröt helyezze a kívánt helyre **álló** helyzetben, úgy, hogy a kábel az egység **alján** legyen található.
 2. A tükröt csatlakoztassa az elektromos hálózatához az egység alján található kábellel. 
 3. Kapcsolja be az egységet a bal oldalfalon található, megjelölt gombbal.
 4. Várjon, ameddig az egységen a "Nincs internetkapcsolat" felirat megjelenik. Amikor ez megtörténik egy WiFi képes eszközzel keresse meg az **Okostükör** nevü WiFi-t.
 5. Csatlakozzon eszközével az **Okostükör WiFi**-re, a **tukor1234** jelszó segítségével.
 6. A csatlakoztatott eszközén egy böngészőbe írja be a következő címet: **192.168.4.1** és nyissa meg.
 7. A megjelenő oldalon először töltse ki a WiFi beállítás részt, a házában található WiFi adataival. "SSID": a WiFi **pontos** neve, "Jelszó": a WiFi pontos jelszava, majd nyomjon a "Küldés" gombra.
 8. Egy kis idő után, körülbelül 2-3 perc, a tükörről el fog tűnni a "Nincs internetkapcsolat" felirat, ez azt jelenti, hogy a WiFi-re kapcsolódás sikeres volt. Amennyiben a felirat nem tűnik el, írja be újra az adatokat.
 9. Miután sikeresen kapcsolódott az eszköz az internetre, az "Irányítószám" mezőbe írja be irányítószámát, majd nyomjon a "Küldés" gombra. A tükrön a településnek 3 másodpercen belül át kell állítódnia.
 10. Ha minden működött, akkor a kezdeti beállításokkal készen is van. A részletes használati és működési utasításokat a továbbiakban olvashatja.

## Használati információk

Amennyiben még nem végezte el, nézze végig a **Kezdeti lépések** részt!

**Szobahőmérséklet mérés**
Az eszköz méri a szoba hőmérsékletét is. Ezt a mérést 15 percenként végzi el és tárolja el. A méréseket akkor tudja megtekinteni, ha csatlakozik a tükörhöz a **Kezdeti lépések** résznek megfelelően, és a **192.168.4.1** címen a menüben a mérések menüpontot megnyitja. Itt egy diagram található a mért adatokkal. 

Ezen kívül az eszköz a [szemirror](https://twitter.com/szemirror) Twitter fiokról küld egy tweetet, ha a szoba hőmérséklete 18 fok alá, vagy 28 fok felé megy. 

**Hírek**
Az eszközön megjelennek hír címek is. Ezeket a Google News szolgáltatja, Magyarország top 5 felkapott híre cserélődnek, amennyiben a hírlista frissül a Google News-on, az eszköz is frissíti azokat. 

**Időjárás**
 Az eszköz az időjárást a beállított irányítószám alapján kéri le. Az időjárás mellett megjeleníti a szél sebességet, és egy ikont a várható/jelenlegi időjárási viszonyokról: napsütés, felhő, eső, vihar, stb...
Az irányítószámot a úgy tudja beállítani, ha csatlakozik a tükörhöz a **Kezdeti lépések** résznek megfelelően, és a **192.168.4.1** címen kitölti a megfelelő mezőt, majd elküldi az adatot. Maximum 3 másodperc alatt át kell állnia a városnak az eszközön.

**Dátum és idő**
Az eszközön megjelenítésre kerül a mindenkori dátum és idő, amely automatikusan követi az óra átállításokat.
> Written with [StackEdit](https://stackedit.io/).
