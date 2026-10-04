# Kuvajako

## Kuvaus:
Sovellus on tarkoitettu kuvien jakamiseen ja kommentoimiseen.
Tällä hetkellä sovelluksesta löytyy tilin tekeminen, sisään kirjautuminen, kuvien titteleiden luominen yhteen kolmesta aihealueesta, näitten muokkaaminen ja poisto, kommentointi ja näiden muokkaaminen ja poisto. Itse kuvien lisäys ja ulkoasun parantaminen olisi seuraavana. Myös hakutoiminto toimii.

## Sovelluksen käynnistäminen:
### Kloonaa repositorio
```
git clone git@github.com:Rium/kuvajako.git
```
```
Siirry komentorivillä kansioon /kuvajako
```
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
Sovellus löytyy nyt haluamallasi selaimella osoitteesta [http://127.0.0.1:5000]

## Testaus
Luo käyttäjätili tai kolme, kokeile lähettää "kuvia", kommentoida niitä, muokata ja poistaa.
Tällä hetkellä tiedettynä ongelmana on että jos yrittää luoda käyttäjätiliä jo olemassa olevalla nimellä uusien tilien tekeminen lukittuu kokonaan.
