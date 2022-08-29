import requests
from random import randint

def pokeAPI(pokemon):
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    return res.json()


def pokeName(pokemon):
    pokemon = pokeAPI(pokemon)

    name = pokemon['name'].capitalize()
    return name


def pokeType(pokemon):
    pokemon = pokeAPI(pokemon)
    type = []
    
    for i in pokemon['types']:
        type.append((i['type']['name']).capitalize())

    if len(type) == 1:
        type.append(type[0])

    return type


def pokeGen(pokemon):
    pokemon = pokeAPI(pokemon)

    id = pokemon['id']

    if 151 >= id >= 1:
        gen = 1
    elif 251 >= id >= 152:
        gen = 2
    elif 386 >= id >= 252:
        gen = 3
    elif 493 >= id >= 387:
        gen = 4
    elif 649 >= id >= 494:
        gen = 5
    elif 721 >= id >= 650:
        gen = 6
    elif 809 >= id >= 722:
        gen = 7
    elif 905 >= id >= 810:
        gen = 8
    
    return gen


def returnPokemon(nameOrId = '', min=1, max=905, rand = False):
    pokemon = dict()

    if rand == True:
        nameOrId = randint(min, max)

    pokemon['name'] = pokeName(nameOrId)
    pokemon['type'] = pokeType(nameOrId)
    pokemon['gen'] = pokeGen(nameOrId)

    return pokemon
