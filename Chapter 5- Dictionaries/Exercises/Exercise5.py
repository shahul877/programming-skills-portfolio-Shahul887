pets = []

pet = {
    'animal type': 'cat',
    'name': 'tom',
    'owner': 'shahul',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'andrew',
    'owner': 'abdu',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'tommy',
    'owner': 'jahfar',
}
pets.append(pet)

for pet in pets:
    print(f"\n what I know about {pet['name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
