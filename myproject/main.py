import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, SessionLocal
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth
from fastapi.middleware.cors import CORSMiddleware


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
    "https://api-finalproject-michaelverv.cloud.okteto.net",
    "https://api-finalproject-michaelverv.cloud.okteto.net/bands"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET /bands/?limit=
@app.get("/bands", response_model=list[schemas.Band])
def read_bands(limit: int = 50, db: Session = Depends(get_db_session)):
    bands = crud.get_bands(db, limit=limit)
    return bands


# POST /bands
@app.post("/bands", response_model=schemas.Band)
def create_band(band: schemas.BandCreate, db: Session = Depends(get_db_session)):
    return crud.create_band(db, band=band)


# GET /bands/{band_id}
@app.get("/bands/{band_id}", response_model=schemas.Band)
def read_band(band_id: int, db: Session = Depends(get_db_session)):
    db_band = crud.get_band(db, band_id=band_id)
    if db_band is None:
        raise HTTPException(status_code=404, detail="Band is not found")
    return db_band


# GET /albums?limit=
@app.get("/albums", response_model=list[schemas.Album])
def read_albums(limit: int = 30, db: Session = Depends(get_db_session)):
    return crud.get_albums(db, limit=limit)


# POST /bands/{band_id}/albums
@app.post("/bands/{band_id}/albums", response_model=schemas.Album)
def create_album(band_id: int, album: schemas.AlbumCreate, db: Session = Depends(get_db_session)):
    return crud.create_album(db, album=album, band_id=band_id)


# GET /songs?limit=
@app.get("/songs", response_model=list[schemas.Song])
def read_songs(limit: int = 100, db: Session = Depends(get_db_session)):
    return crud.get_songs(db, limit=limit)


# POST /songs
@app.post("/songs", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db_session)):
    return crud.create_song(db, song=song)


# POST /songs
@app.post("/songs/{album_id}", response_model=schemas.Song)
def create_song_with_album(album_id: int, song: schemas.SongCreate, db: Session = Depends(get_db_session)):
    return crud.create_song(db, song=song, album_id=album_id)


# DELETE /bands/{band_id}/delete
@app.delete("/bands/{band_id}/delete")
def delete_band(band_id: int, db: Session = Depends(get_db_session)):
    crud.delete_band(db, band_id=band_id)


# DELETE /delete
@app.delete("/delete")
def delete_all(db: Session = Depends(get_db_session)):
    crud.delete_db(db)


# GET /users/?skip=&limit=
@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


# POST /users
@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    db_username = crud.get_user_by_username(db, username=user.username)
    db_email = crud.get_user_by_email(db, email=user.email)
    if db_username:
        raise HTTPException(status_code=400, detail="Username already exists")
    if db_email:
        raise HTTPException(status_code=400, detail="Email already in use")
    return crud.create_user(db, user=user)


# GET /users/{user_id}
@app.get("/users/{user_id}",  response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db_session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# GET /users/{user_id}/playlist
@app.get("/users/{user_id}/playlist",  response_model=list[schemas.Playlist])
def read_playlist(user_id: int, db: Session = Depends(get_db_session)):
    db_playlist = crud.get_playlists_of_user(db, user_id=user_id)
    return db_playlist


# POST /playlist
@app.post("/users/{user_id}/playlist", response_model=schemas.Playlist)
def create_playlist_for_user(
        user_id: int,
        playlist: schemas.PlaylistCreate,
        db: Session = Depends(get_db_session)
):
    return crud.create_playlist(db, playlist=playlist, user_id=user_id)


# POST /users/{user_id}/playlist/{playlist_id}/songs/{song_id}
# @app.post("/users/{user_id}/playlist/{playlist_id}/songs/{song_id}", response_model=schemas.Song)
# def add_song_to_playlist_of_user(
#         user_id: int,
#         playlist_id: int,
#         song_id: int,
#         db: Session = Depends(get_db_session)
# ):
#     song = crud.add_song_to_playlist_of_user(db, playlist_id, song_id)
#     if not song:
#        raise HTTPException(status_code=404, detail="Song or Playlist not found or already exists in another playlist")
#
#     return song


# PUT /users/{user_id}/playlist/{playlist_id}
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db_session),
    token: str = Depends(oauth2_scheme)
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, user=user)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
