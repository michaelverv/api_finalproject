from pydantic import BaseModel


# Song Base
class SongBase(BaseModel):
    duration: float
    name: str


# Song OUT
class Song(SongBase):
    id: int
    album_id: int | None = None

    class Config:
        orm_mode = True


# Song IN
class SongCreate(SongBase):
    pass


# Album Base
class AlbumBase(BaseModel):
    duration: float
    amount_of_songs: int
    release_date: int
    name: str


# Album OUT
class Album(AlbumBase):
    band_id: int
    id: int
    songs: list[Song] = []

    class Config:
        orm_mode = True


# Album IN
class AlbumCreate(AlbumBase):
    pass


# Band Base
class BandBase(BaseModel):
    name: str
    is_still_active: bool
    lead_singer: str
    genre: str


# Band OUT
class Band(BandBase):
    id: int
    albums: list[Album] = []

    class Config:
        orm_mode = True


# Band IN
class BandCreate(BandBase):
    pass


# Playlist Base
class PlaylistBase(BaseModel):
    name: str
    description: str
    user_id: int


# Playlist OUT
class Playlist(PlaylistBase):
    id: int
    songs: list[Song] = []

    class Config:
        orm_mode = True


# Playlist IN
class PlaylistCreate(PlaylistBase):
    pass


# User Base
class UserBase(BaseModel):
    username: str
    email: str


# User OUT
class User(UserBase):
    id: int
    playlists: list[Playlist] = []

    class Config:
        orm_mode = True


# User IN
class UserCreate(UserBase):
    password: str
