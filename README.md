# API Development final project Michael Vervoort 1CCS01

## Gekozen thema
Voor het project heb ik als thema `muziek`. Mijn database bestaat uit `5` entiteiten: users, playlists, bands, albums en songs.
Een band kan meerdere albums hebben en een album kan meerdere songs bevatten. Een song kan ook gemaakt worden zonder een album. Een user kan playlists maken die meerdere songs kunnen bevatten, deze lijsten zijn onafhankelijk van de bands en albums.

Het doel van mijn API is om de app `Spotify` als inspiratie te gebruiken voor een functionele API. Uiteraard is het niet op hetzelfde niveau en zijn niet alle functionaliteiten volledig gelukt, meer uitleg hierover onderaan bij de "playlist" endpoints.

## API
### Link API: https://api-finalproject-michaelverv.cloud.okteto.net/
### Link Frontend API: https://api-michaelv.netlify.app/api

### Uitleg API
Met deze API is het mogelijk om een collectie bij te houden van je favoriete bands, albums en songs. Door gebruik te maken van alle endpoints hieronder, is dit gebruiksvriendelijk en gemakkelijk te doen. In tegenstelling tot de oudere API is het nu ook mogelijk om verschillende playlists te maken. Deze playlists zijn gelinkt aan een account van een user, deze is beveiligt volgens de eisen van de opdracht. In de playlist zelf is het mogelijk om verschillende songs te zetten, de favoriete bands, albums en songs zijn ook nog beschikbaar.

De API wordt toegangelijk gesteld via Okteto, doormiddel van github met een workflow die de dockerimage van de website dockerhub haalt. Met behulp van docker-compose en workflow wordt dit geautomatiseerd en is het makkelijk om via Okteto de github repo aan te duiden en deze op te starten.

### Functies van de API
- 7 GET endpoints
- 7 POST endpoints
- 2 DELETE endpoints
- 1 PUT endpoint
- Hashing van wachtwoorden
- OAuth op GET /users endpoint
- Token
- Frontend

## Uitgewerkte nummers
### 1. ALGEMENE EISEN & DOCUMENTATIE (alles samen +50%)
- :heavy_check_mark: Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
- :heavy_check_mark: Minstens 3 entiteiten in je API via een SQLite databank
- :heavy_check_mark: Minstens hashing en OAuth implementeren
- :heavy_check_mark: Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md
- :heavy_check_mark: Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- :heavy_check_mark: Volledige OpenAPI docs screenshot(s) op GitHub README.md
- :heavy_check_mark: Logisch gebruik van path parameters, query parameters en body
- :heavy_check_mark: Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
- :heavy_check_mark: Deployment van de API container(s) op Okteto Cloud via Docker Compose
- :heavy_check_mark: Test alle GET endpoints van een van je APIs via de Requests en pytest library met een testfile in de root van je repository.

### 3.  AANVULLINGEN: FRONT-END
- :heavy_check_mark: 3.1 (+15%) Maak een front-end voor je applicatie die al je GET endpoints en POST endpoints bevat.
- :heavy_check_mark: 3.1.1 (+10%) Host de front-end op Netlify. 
- :heavy_check_mark: 3.1.2 (+10%) Geef de front-end een leuke stijlgeving.

Hoewel ik niet alle GET en POST endpoints op de frontend heb heeft dit zijn redenen. Omdat ik meer GET/POST requests heb dan werd gevraagd voor de basis opdracht heb ik de request op de pagina ook wat beperkter gehouden. Nog een reden hiervoor is dat ik de code voor de playlists niet volledig in orde heb gekregen, waardoor ik het meer gepast vond om enkel de bands, albums en songs op de frontend te zetten.

## OpenAPI docs
Dit zijn screenshots van alle endpoint die de API bevat.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/28d96103-61e5-4fbe-8653-303b7c1c194f)
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/7adf1549-a1bb-42df-9140-485f56965c49)

## API werking met Postman
Via Postman wordt van elke endpoint van de API weergegeven hoe deze werkt.

### POST /bands
Gaat een band aanmaken om naar de database sturen.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/e641d019-4edb-4e02-a5d9-c910f0e1993a)

### GET /bands
Laat alle bands zien.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/ac4d9c43-1126-41f8-acdb-a003d1338a15)

### GET /bands/{band_id}
Laat een specifieke band zien door de id van een band mee te geven.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/8a6cf2df-7c19-44a7-8e1c-80ce4bac1f3d)

### POST /bands/{band_id}/albums
Gaat een album toevoegen bij een specifieke band door de id van deze band mee te geven.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/7ec755b0-e599-4504-9ca5-9a803cc5d2c8)

### GET /albums
Laat alle albums zien.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/2cc9dd01-6532-4caa-9347-043cad26ffe2)

### POST /songs
Maak een nummer aan dat **niet** gelinkt is aan een album.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/4cd927ca-2b45-4eda-8d87-25a2d1dec8ba)

### POST /songs/{album_id}
Maakt een nummer aan dat gelinkt wordt aan een bepaald albums doordat er een album id wordt meegegeven.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/91125feb-4516-44cb-9e3a-ff1b797969ff)

### GET /songs
Laat alle songs zien.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/920a8139-6d1f-4a81-91ab-0eb7273e68e6)

### DELETE /bands/{band_id}/delete
Verwijdert een specifieke band door de band id mee te geven in de URI.

Bij een GET /bands zijn de volgende bands te zien:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/6dfebfcd-57ca-412d-b31a-98456a5cda75)

Bij het uitvoeren van een /bands/2/delete gaat de band "Slipknot" uit de database worden gehaald. Na het uitvoeren wordt er een null waarde teruggegeven.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/5809a516-41b8-485f-bbb7-27aea2f2202e)

Bij het opnieuw uitvoeren van een GET /bands request is het te zien dat de band is verwijderd.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/1c4c197d-e394-4796-99c3-facdd32aba38)

### DELETE /delete
Verwijdert alle data in de database, dit houd in: alle bands, albums, songs, playlists en users.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/954449e1-7c1f-4377-b620-6d702fd2d269)

Na het uitvoeren van deze endpoint gaat deze een null waarde terug geven als bevestiging dat alles is verwijderd. Bij het maken van een GET request zijn er lege vierkante haakjes als response omdat er geen data is.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/bbec3862-7d14-47ce-aa64-f86ec7a9b4cc)

### POST /users
Maakt een user aan en checkt of de username/email al niet bestaat in de database.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/18a14d3e-182d-44f1-9744-e81aad4cc51b)

Bij het opnieuw doorsturen van dezelfde data, is er een melding zichtbaar dat de username al bestaat.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/85b86af3-9224-4267-a642-99ac04b6bab4)

Hetzelfde voor de email, ondanks dat de username nu anders is.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/2d23fce5-0c46-401f-a17c-dcf400f31ed2)

### GET /users
Laat alle users zien.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/765d82a9-1ec0-4ff2-9b85-acdd54a75571)

### GET /users/{user_id}
Laat een specifieke user zien door de user id mee te geven in de URL.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/bfee2bce-2f36-4458-9956-2c77132efe7e)

### POST /users/{user_id}/playlist
Hiermee kan er een playlist aangemaakt worden voor een gebruiker. Mijn originele bedoeling was om er makkelijk nummers in te kunnen zetten, dit is me echter niet gelukt. De code die ik hiervoor had geschreven heb ik in commentaar laten staan. Ondanks dat het niet mogelijk is om nummers toe te voegen aan een playlist, heb ik de lijst met songs leeg laten staan.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/eb9d232d-71fa-4bf8-8e0f-42d913bca64b)

### GET /users/{user_id}/playlist
Laat alle playlists zien van een gebruiker.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/addd6dc8-59df-41ff-a24c-68565707d709)

### PUT /users
Via deze endpoint is het mogelijk om de gegevens van een gebruiker aan te passen. Voor security redenen is het aanpassen van gebruikers enkel mogelijk door geauthorizeerd te zijn via OAuth, indien dit niet nog niet is gedaan krijg je de volgende melding:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/34ddb904-8f76-4c4d-bfdf-8feb0a76dfc1)

Dus om deze endpoint te kunnen gebruiken moet er eerst worden geauthoriseerd, dit kan via de `/token` in te geven maar eigenlijk wordt deze automatisch gebruikt in de OpenAPI docs, hier kan dit gemakkelijk met de `Authorize` knop. Dus voor deze endpoint ga ik werken via de knop, deze maakt automatisch gebruik van de /token endpoint om de gegevens daar naar door te sturen. De knop ziet er als volgende uit:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/943c8243-3388-4725-822d-3cd14b487ade)

Door op de knop te drukken verschijnt dit scherm:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/d10fe516-9521-47fa-b5f3-7b7095c7f41f)

Als we hier de gegevens invullen en op de knop drukken komt dit scherm tevoorschijn:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/9cb1d661-0396-471a-94ea-12163b2b826d)

Dit wilt zeggen dat het inloggen gelukt is en dat het nu mogelijk is om de PUT endpoint te gebruiken.

Voor we de gebruiker aanpassen doen we een GET request voor de data van de gebruiker te zien:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/79210b8c-d71b-4591-9be8-649423d4639f)

Hierna voeren we een PUT request uit op dezelfde gebuiker om de gegevens aan te passen, de id wordt meegegeven in de URL:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/d8db7ef6-a064-425e-bd46-2446de78c1b6)

Als we dan opnieuw een GET request uitvoeren is het te zien dat de gegevens zijn aangepast:
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/ea519719-38e5-47af-9f28-5c070a0737fd)

### POST /token
Deze endpoint dient voor OAuth te kunnen gebruiken. OpenAPI docs gebruikt dit om een gebruiker te authorizeren met een token. Via Postman is dit niet mogelijk om zomaar te doen.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/a921fbcb-9b27-4fc6-a92c-ed900ab9489e)
