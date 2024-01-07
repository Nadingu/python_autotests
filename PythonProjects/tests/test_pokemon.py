import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = "1bea14471c7374786dda71fa1a13f33e"

def test_status_code():
  response = requests.get(f'{host}/trainers', params = {'trainers_id': 4306})
  assert response.status_code == 200 
 
def test_part_of_body():
  response = requests.get(f'{host}/trainers', params = {'trainer_id': 4306})
  assert response.json()["trainer_name"] == "Core"