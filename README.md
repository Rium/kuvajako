# Kuvajako

Sovelluksen käynnistäminen:\
Lataa tiedostot omalle koneelle.\
Sijoita tiedostoon jossa toimii flask.\
Suorita komento "sqlite3 database.db < schema.sql" (ilman heittomerkkejä) tietokannan luomiseksi.\
Käynnistä flask komennolla "flask run" ja avaa sivu http://127.0.0.1:5000 haluamallasi selaimella.

Tavoitteet:
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen kuvia kuvaavan tekstin kanssa. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kuvia. Käyttäjä voi halutessaan lisätä kuviin tagejä ennalta olevasta listasta.
* Käyttäjä näkee sovellukseen lisätyt kuvat. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kuvat.
* Käyttäjä pystyy lisäämään kommentteja omiin ja muiden lisäämiin kuviin.
* Käyttäjä pystyy etsimään kuvia luokittelulla, hakusanalla tai tageillä. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä kuvia.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät kuvat ja kommentit.
* Kuville on valittavissa useampia luokitteluja (valmiit projektit, kesken olevat, avuntarpeet). Valittavissa olevat luokittelut tulee määritellä tietokannassa. Käyttäjä voi valita jokaisen luokittelun kohdalla yhden vaihtoehdon.
* Sovelluksessa on pääasiallisen tietokohteen (kuvien) lisäksi toissijainen tietokohde (kommentit), joka täydentää pääasiallista tietokohdetta. Käyttäjä pystyy lisäämään toissijaisia tietokohteita omiin ja muiden käyttäjien tietokohteisiin liittyen.
* Sovellus on suunniteltu pienoismalliprojektien näyttämistä varten, mutta samaa pohjaa voi hieman muokkaamalla käyttää myös muuhun.
