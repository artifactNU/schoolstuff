Här är den renskrivna versionen:

# Infrastruktur - Uppgift 4: Docker

## Skapa ett system med ett HTTP-baserat API

### Krav

- Systemet ska bestå av minst två Docker-containrar.
- En container ska heta `persistance`:
  - Ansvarar för lagring av data.
  - Data ska lagras på disk.
  - Lagringen bör vara konfigurerad så att containern kan raderas och återskapas utan att data går förlorat.
  - Det ska vara möjligt att anropa denna container från den andra containern via det interna nätverket för att lagra eller hämta data.
  - En `Dockerfile` för containern är valfri.
- En container ska heta `api`:
  - Ansvarar för att ta emot anrop från värddatorn.
  - Ska kunna hantera anrop för att lagra och läsa information.
  - Anropen ska vara av typen HTTP `GET` och `POST`.
  - `GET` ska returnera information som JSON.
  - `POST` ska ta emot information som JSON.
  - Anropen ska svara med lämpliga HTTP-statuskoder beroende på resultatet.
  - Testa och säkerställ följande scenarier:
    - Containern kan inte nå `persistance`.
    - Felaktiga anrop från värddatorn (exempelvis felaktig data).
  - Containern ska anropa `persistance` för att lagra och läsa information.
  - Containern måste ha en `Dockerfile` som bygger en färdig image.
  - Det ska vara möjligt att använda en bind mount för att enkelt uppdatera koden under utveckling.
  - Containern ska kunna nås från värddatorn via port 80.
- Skapa ett anpassat bridge-nätverk med namnet `infra`, som båda containrarna är anslutna till.
- Skapa ett enkelt Bash-skript, `start.sh`, som startar de två containrarna.

### Tips

Uppgiften är flexibel och syftet är att öva på att koppla samman containrar samt konfigurera nätverk och lagring.

Om du vill ha en startpunkt kan följande verktyg vara bra val:

- Programmeringsspråk: Python
- För att hantera HTTP-anrop: [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- För att interagera med en databas: [Peewee](https://peewee.readthedocs.io/en/latest/index.html)
- Databas: MySQL
- API-containern kan baseras på en Ubuntu-image
- Applikationsidé: En TODO-lista-applikation med stöd för att lägga till och visa alla TODO-poster.
- Gör inget stort och komplicerat.

## Inlämning

Följ dokumentet "Studentguide till GitHub Classroom", som finns länkat i materialet från den första lektionen på Studentportalen. Det är uppskattat om du ger feedback till utbildaren om dokumentet kan förbättras eller om något saknas.

### Filer

**Obligatoriska filer:**

| Filnamn              | Beskrivning                                                           |
| -------------------- | --------------------------------------------------------------------- |
| `Dockerfile.api`     | Fil för att sätta upp en image för `api`.                             |
| `start.sh`           | Skript som startar containrarna med nätverks- och volymkonfiguration. |
| `docker-compose.yml` | Docker Compose-fil som gör samma sak som `start.sh`.                  |

**Valfria filer:**

| Filnamn                  | Beskrivning                                             |
| ------------------------ | ------------------------------------------------------- |
| `Dockerfile.persistance` | Om du väljer att skapa en Dockerfile för `persistance`. |