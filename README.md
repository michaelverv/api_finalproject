# API Development final project Michael Vervoort 1CCS01

## Gekozen thema
Voor het project heb ik als thema `muziek`. Mijn database bestaat uit `5` entiteiten: users, playlists, bands, albums en songs.
Een band kan meerdere albums hebben en een album kan meerdere songs bevatten. Een song kan ook gemaakt worden zonder een album. Een user kan playlists maken die meerdere songs kunnen bevatten, deze lijsten zijn onafhankelijk van de bands en albums.

## API
### Link API: https://api-finalproject-michaelverv.cloud.okteto.net/

### Uitleg API
Met deze API is het mogelijk om een collectie bij te houden van je favoriete bands, albums en songs. Door gebruik te maken van alle endpoints hieronder, is dit gebruiksvriendelijk en gemakkelijk te doen. In tegenstelling tot de oudere API is het nu ook mogelijk om verschillende playlists te maken. Deze playlists zijn gelinkt aan een account van een user, deze is beveiligt volgens de eisen van de opdracht. In de playlist zelf is het mogelijk om verschillende songs te zetten, de favoriete bands, albums en songs zijn ook nog beschikbaar.

De API wordt toegangelijk gesteld via Okteto doormiddel van github met een workflow en docker compose enz --> `meer uitleg`

### Functies van de API
- 7 GET endpoints
- 7 POST endpoints
- 2 DELETE endpoints
- 1 PUT endpoint
- Hashing van wachtwoorden
- OAuth op GET /users endpoint
- Token

## Uitgewerkte nummers
### 1. ALGEMENE EISEN & DOCUMENTATIE (alles samen +50%)
- :heavy_check_mark: Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
- :heavy_check_mark: Minstens 3 entiteiten in je API via een SQLite databank
- :heavy_check_mark: Minstens hashing en OAuth implementeren
- :heavy_check_mark: Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md
- [ ] Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- :heavy_check_mark: Volledige OpenAPI docs screenshot(s) op GitHub README.md
- :heavy_check_mark: Logisch gebruik van path parameters, query parameters en body
- :heavy_check_mark: Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
- :heavy_check_mark: Deployment van de API container(s) op Okteto Cloud via Docker Compose
- [ ] Test alle GET endpoints van een van je APIs via de Requests en pytest library met een testfile in de root van je repository.

## OpenAPI docs
Dit zijn screenshots van alle endpoint die de API bevat.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/1277d673-a175-4e71-8ee1-34d55dbbd67d)
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/717809bd-1d76-43de-8cd4-7f4bf5564123)

## API werking met Postman
Via Postman wordt van elke endpoint van de API waargegeven hoe deze werkt.

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
### POST /songs/{album_id}
### GET /songs
### DELETE /bands/{band_id}/delete
### DELETE /delete
### POST /users
### GET /users
### GET /users/{user_id}
### POST /users/{user_id}/playlist
### GET /users/{user_id}/playlist
### PUT /users/{user_id}/playlist/{playlist_id}
### POST /token
