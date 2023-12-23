from sqlalchemy.orm import Session

import auth
import models
import schemas


def get_band(db: Session, band_id: int):
    return db.query(models.Band).filter(models.Band.id == band_id).first()


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


def create_song(db: Session, song: schemas.SongCreate, album_id: int = None):
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


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        password=hashed_password,
        username=user.username
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_playlist(
        db: Session,
        playlist: schemas.PlaylistCreate,
        user_id: int,
        name: str,
        description: str
):
    db_playlist = models.Playlist(
        **playlist.dict(),
        user_id=user_id,
        description=description,
        name=name
    )
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist


def get_playlists_of_user(db: Session, user_id: int):
    return db.query(models.Playlist).filter(models.Playlist.user_id == user_id)


def update_playlist(
        db: Session,
        playlist_id: int,
        playlist: schemas.PlaylistCreate,
        user_id: int,
        description: str,
        name: str
):
    db.query(models.Playlist).filter(models.Playlist.id == playlist_id).delete()
    db_playlist = models.Playlist(
        **playlist.dict(),
        user_id=user_id,
        description=description,
        name=name
    )
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist
