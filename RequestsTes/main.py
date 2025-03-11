import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c7ae2ba775688a231679746493a27515'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Kuca",
    "photo_id": 8
}

body_catch = {
    "pokemon_id": '259526'
}

body_name = {
    "pokemon_id": '259564',
    "name": "Newkuca",
    "photo_id": 8

}

'''response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json= body_create )
print(response_create.text)'''


'''pokemon_id = response_create.json()[id]
print(pokemon_id)'''


'''response_catch = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_catch)
print(response_catch.text)'''

'''response_name = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= body_name)
print (response_name.text)'''

