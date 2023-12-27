import requests
import json


def test_get_bands():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/bands')
    assert response.status_code == 200
    bands = response.json()
    assert isinstance(bands, list)
    for band in bands:
        assert "id" in band
        assert band["id"] >= 1


def test_get_band_with_id():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/bands/2')
    assert response.status_code == 200
    band = response.json()
    assert "id" in band
    assert band["id"] == 2
    assert band["name"] == "Radiohead"


def test_get_albums():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/albums')
    assert response.status_code == 200
    albums = response.json()
    for album in albums:
        assert "release_date" in album
        assert album["release_date"] > 1900
        assert album["amount_of_songs"] >= 1


def test_get_songs():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/songs')
    assert response.status_code == 200
    songs = response.json()
    assert isinstance(songs, list)
    for song in songs:
        assert "album_id" in song
        assert "id" in song
        assert "duration" in song


def test_get_users():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/users')
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    for user in users:
        assert "username" in user
        assert "email" in user


def test_get_user_with_id():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/users/1')
    assert response.status_code == 200
    user = response.json()
    assert isinstance(user, dict)
    assert "id" in user
    assert "username" in user
    assert "email" in user


def test_get_playlist_of_user():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/users/1/playlist')
    assert response.status_code == 200
    playlist = response.json()
    assert isinstance(playlist, list)
    for item in playlist:
        assert "id" in item
        assert "name" in item
        assert "user_id" in item
        assert "description" in item
        assert "songs" in item
