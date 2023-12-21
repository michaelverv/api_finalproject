from sqlalchemy.orm import Session
import models
import schemas


def get_band(db: Session, band_id: int):
    return db.query(models.Band).filter(models.Band.id == band_id).first


def get_bands(db: Session, limit: int = 50):
    return db.query(models.Band).limit(limit).all()


def create_band(db: Session, band: schemas.BandCreate):
    db_band = models.Band(
        name=band.name,
        is_still_active=band.is_still_active,
        lead_singer=band.lead_singer,
        genre=band.genre
    )
    db.add(db_band)
    db.commit()
    db.refresh(db_band)
    return db_band


def get_albums(db: Session, limit: int = 30):
    return db.query(models.Album).limit(limit).all()


def create_album(db: Session, album: schemas.AlbumCreate, band_id: int):
    db_album = models.Album(
        **album.dict(),
        band_id=band_id
    )
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album


def get_songs(db: Session, limit: int = 100):
    return db.query(models.Song).limit(limit).all()


# def get_song_by_name(db: Session, name: str):
    # return db.query(models.Song).filter(models.Song.name == name).first


def create_song(db: Session, song: schemas.SongCreate, album_id: int):
    db_song = models.Song(
        **song.dict(),
        album_id=album_id,
    )
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def delete_band(db: Session, band_id: int):
    db.query(models.Band).filter(models.Band.id == band_id).delete()
    db.commit()


def delete_db(db: Session):
    db.query(models.Band).delete()
    db.query(models.Album).delete()
    db.query(models.Song).delete()
    db.commit()
