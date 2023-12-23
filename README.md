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
- - [x] Minstens 3 GET, 1 POST, 1 PUT en 1 DELETE endpoints
- - [x] Minstens 3 entiteiten in je API via een SQLite databank
- - [x] Minstens hashing en OAuth implementeren
- - [x] Beschrijving van het gekozen thema, je API(s) en je uitbreidingen + link naar de zaken die hosted zijn op GitHub README.md
- - [x] Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- - [x] Volledige OpenAPI docs screenshot(s) op GitHub README.md
- - [x] Logisch gebruik van path parameters, query parameters en body
- - [x] Docker container voor de API(s), welke automatisch door GitHub Actions opgebouwd wordt
- - [x] Deployment van de API container(s) op Okteto Cloud via Docker Compose
- - [x] Test alle GET endpoints van een van je APIs via de Requests en pytest library met een testfile in de root van je repository.

## OpenAPI docs
Dit zijn screenshots van alle endpoint die de API bevat.
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/1277d673-a175-4e71-8ee1-34d55dbbd67d)
![image](https://github.com/michaelverv/api_finalproject/assets/113921262/717809bd-1d76-43de-8cd4-7f4bf5564123)

## API werking met Postman
Via Postman wordt van elke endpoint van de API waargegeven hoe deze werkt.

## POST /bands
## GET /bands
## GET /bands/{band_id}
## POST /bands/{band_id}/albums
## GET /albums
## POST /songs
## POST /songs/{album_id}
## GET /songs
## DELETE /bands/{band_id}/delete
## DELETE /delete
## POST /users
## GET /users
## GET /users/{user_id}
## POST /users/{user_id}/playlist
## GET /users/{user_id}/playlist
## PUT /users/{user_id}/playlist/{playlist_id}
## POST /token
