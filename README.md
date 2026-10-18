# Kuvajako

## Kuvaus:
Sovellus on tarkoitettu kuvien jakamiseen ja kommentoimiseen.
Tämä nyt jäi vähän raakileeksi, täysin omasta ajankäytöstä johtuen.
Kaikki perusfunktiot toimivat, pitäis täyttää perusvaatimukset.
Käyttäjä pystyy rekisteröitymään, kirjautumaan sisään, näkemään kuvia kolmessa eri kategoriassa, lisäämään omia kuviaan tai kommentteja kuviin, muokkaamaan tai poistamaan omia lisäyksiään.

## Sovelluksen käynnistäminen:
### Kloonaa repositorio
```
git clone git@github.com:Rium/kuvajako.git
```
Siirry komentorivillä kansioon /kuvajako
### Käynnistä virtuaaliympäristö
```
python3 -m venv venv
```
```
source venv/bin/activate
```
### Alusta tietokannat
```
sqlite3 database.db < schema.sql
```
```
sqlite3 database.db < init.sql
```
### Käynnistä sovellus
```
flask run
```
Sovellus löytyy nyt haluamallasi selaimella osoitteesta http://127.0.0.1:5000

## Testaus
Luo käyttäjätili tai kolme, kokeile lähettää kuvia, kommentoida niitä, muokata ja poistaa.
Tällä hetkellä tiedettynä ongelmana on että jos yrittää luoda käyttäjätiliä jo olemassa olevalla nimellä uusien tilien tekeminen lukittuu kokonaan.

## Kehitysideoita
- CSS
- Käyttäjäystävällisyyden ja yleisen layoutin parannus
- Koodiin on todennäköisesti jäänyt hassuuksia vanhoista ideoista / yrityksistä jotka on sittenmin vaihdettu, näiden siistiminen.
