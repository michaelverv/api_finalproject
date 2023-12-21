import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, SessionLocal

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


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
@app.get("/bands/{id}", response_model=schemas.Band)
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


# GET /songs/{name}
# @app.get("/songs/{name}", response_model=schemas.Song)
# def read_song_by_name(name: str, db: Session = Depends(get_db_session)):
# db_song_name = crud.get_song_by_name(db, name=name)
# if db_song_name is None:
# raise HTTPException(status_code=404, detail="Song not found")
# return


# POST /bands/{band_id}/albums/{album_id}/songs
@app.post("/songs", response_model=schemas.Song)
def create_song(album_id: int, song: schemas.SongCreate, db: Session = Depends(get_db_session)):
    return crud.create_song(db, song=song, album_id=album_id)


# DELETE /bands/{band_id}/delete
@app.delete("/bands/{band_id}/delete")
def delete_band(band_id: int, db: Session = Depends(get_db_session)):
    crud.delete_band(db, band_id=band_id)


# DELETE /delete
@app.delete("/delete")
def delete_all(db: Session = Depends(get_db_session)):
    crud.delete_db(db)
