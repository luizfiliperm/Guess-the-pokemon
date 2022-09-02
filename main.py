from pokemon import *

randPokemon = returnPokemon(rand=True)

info = {
    'name' : 'Unknown',
    'type' : ['Unknown', 'Unknown'],
    'weight': 'Unknown',
    'gen' : 'Unknown',
}

attempts = 0
uncheckedTypes = allTypes()
checkedTypes = list()

print("=-=" * 44)

while info != randPokemon:
    attempts += 1
    print(f'Checked types: {" ".join(checkedTypes)}\nUnchecked types: {" ".join(uncheckedTypes)}')
    print("=-=" * 44)

    while True:
        checkPokemon = input("Your guess: ").strip().lower()
        try:
            checkPokemon = returnPokemon(nameOrId=checkPokemon)
            break
        except:
            print("Invalid option!")
    
    # Name
    if checkPokemon['name'] == randPokemon['name']:
        info['name'] = randPokemon['name']

    # Type
    for checkType in checkPokemon['type']:
        for position,randType in enumerate(randPokemon['type']):
            if checkType == randType:
                info['type'][position] = randType

        if checkType not in checkedTypes:
            checkedTypes.append(checkType)
            uncheckedTypes.remove(f'{checkType}')

    # Weight
    if info['weight'] == randPokemon['weight']:
        pass
    elif randPokemon['weight'] == checkPokemon['weight']:
        info['weight'] = randPokemon['weight']
    elif checkPokemon['weight'] > randPokemon['weight'] :
        info['weight'] = f'< {checkPokemon["weight"]}'
    elif checkPokemon['weight'] < randPokemon['weight']:
        info['weight'] = f'> {checkPokemon["weight"]}'


    # Gen
    if info['gen'] == randPokemon['gen']:
        pass
    elif checkPokemon['gen'] == randPokemon['gen']:
        info['gen'] = randPokemon['gen']
    elif checkPokemon['gen'] < randPokemon['gen']:
        info['gen'] = f'> {checkPokemon["gen"]}'
    elif checkPokemon['gen'] > randPokemon['gen']:
        info['gen'] = f'< {checkPokemon["gen"]}'

    print("=-=" * 44)

    print(f"{checkPokemon['name']} - {checkPokemon['type'][0]}, {checkPokemon['type'][1]}, weight: {checkPokemon['weight']}kg - Gen {checkPokemon['gen']}")
    print(f"{info['name']} - {info['type'][0]}, {info['type'][1]}, weight: {info['weight']}kg - Gen {info['gen']}")

    print("=-=" * 44)

print(f"Congratulations! You got it! Attempts: {attempts}")
