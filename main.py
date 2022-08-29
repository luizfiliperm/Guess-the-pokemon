from pokemon import *

randPokemon = returnPokemon(rand=True)

info = dict()
info['name'] = 'Unknown'
info['type'] = ['Unknown', 'Unknown']
info['gen'] = 'Unknown'

while info != randPokemon:

    print("=-=" * 15)

    while True:
        checkPokemon = input("Your guess: ").strip().lower()
        try:
            checkPokemon = returnPokemon(nameOrId=checkPokemon)
            break
        except:
            print("Invalid option!")
    
    if checkPokemon['name'] == randPokemon['name']:
        info['name'] = randPokemon['name']

    if checkPokemon['type'][0] == randPokemon['type'][0]:
        info['type'][0] = randPokemon['type'][0]
    if checkPokemon['type'][1] == randPokemon['type'][0]:
        info['type'][0] = randPokemon['type'][0]

    if checkPokemon['type'][0] == randPokemon['type'][1]:
        info['type'][1] = randPokemon['type'][1]
    if checkPokemon['type'][1] == randPokemon['type'][1]:
        info['type'][1] = randPokemon['type'][1]


    if info['gen'] == randPokemon['gen']:
        pass
    elif checkPokemon['gen'] == randPokemon['gen']:
        info['gen'] = randPokemon['gen']
    elif checkPokemon['gen'] < randPokemon['gen']:
        info['gen'] = f'>{checkPokemon["gen"]}'
    elif checkPokemon['gen'] > randPokemon['gen']:
        info['gen'] = f'<{checkPokemon["gen"]}'

    print("=-=" * 15)

    print(f"{checkPokemon['name']} - {checkPokemon['type'][0]}, {checkPokemon['type'][1]} - Gen {checkPokemon['gen']}")
    print(f"{info['name']} - {info['type'][0]}, {info['type'][1]} - Gen {info['gen']}")

print("=-=" * 15)
print("Congratulations, you got it!")
