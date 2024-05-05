# k_a-tsoha

Kuinka testata?

Avaa kaksi terminalia, joista toiseen anna komento: 

- start-pg.sh

Kloonaa sitten tämä repostorio toiseen ja luo .env tiedosto johon laitat nämä tiedot: 

- DATABASE_URL = postgresql:///(tietokannan-paikallinen-osoite)
- SECRET_KEY = (oma salainen avain)

tämän jälkeen tee seuraavat komennot: 
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install -r ./requirements.txt

käynnistä komennolla: 
- $ flask run

projektin aihe on keskustelusovellus

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda ketjuun uuden viestin, antamalla sille otsikon ja viestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.


