import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c7ae2ba775688a231679746493a27515'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '22980'

def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200 

def test_trainer_id():
    id =  requests.get(url = f'{URL}/trainers', params= {'trainer_id' : 22980})
    assert id.json()["data"][0]["trainer_name"] == 'Inna'