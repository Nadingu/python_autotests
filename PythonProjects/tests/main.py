import requests

token = "1bea14471c7374786dda71fa1a13f33e"
host = 'https://api.pokemonbattle.me:9104'

'''response = requests.post('https://api.pokemonbattle.me:9104/pokemons',
                         json = { 
    "name": "generate",
    "photo": "generate"
}, headers = {"Content-Type":"application/json", "trainer_token": token})

print(response.json())'''

'''response = requests.put('https://api.pokemonbattle.me:9104/pokemons',
                         json = {
    "pokemon_id": "24973",
    "name": "Nadingu",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type":"application/json", "trainer_token": token})

print(response.json())'''

response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                         json = {
    "pokemon_id": "24973"
}, headers = {"Content-Type":"application/json", "trainer_token": token})

print(response.json())