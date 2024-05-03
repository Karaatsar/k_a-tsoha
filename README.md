# k_a-tsoha

Kuinka testata?

Kloonaa tämä repostorio ja luo .env tiedosto johon laitat nämä tiedot: 

- DATABASE_URL = >tietokannan-paikallinen-osoite<
- SECRET_KEY = >oma-salainen-avain<

tämän jälkeen tee seuraavat komennot: 
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install -r ./requirements.txt

määritä tietokannan skeema komennolla:
- $ psql < schema.sql

käynnistä komennolla: 
- $ flask run

projektin aihe on keskustelusovellus

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.


