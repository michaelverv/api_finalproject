import requests
import json


def test_get_bands():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/bands')
    assert response.status_code == 200


def test_get_band_with_id():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/bands/1')
    assert response.status_code == 200


def test_get_albums():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/albums')
    assert response.status_code == 200


def test_get_songs():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/songs')
    assert response.status_code == 200


def test_get_users():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/users')
    assert response.status_code == 200


def test_get_user_with_id():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/users/1')
    assert response.status_code == 200


def test_get_playlist_of_user():
    response = requests.get('https://api-finalproject-michaelverv.cloud.okteto.net/users/1/playlist')
    assert response.status_code == 200
