import json


if __name__ == "__main__":
    # Nuskaito json faila, sukuria data kintamaji kuriame failo turinys yra pitono objekte
    # dict() arba list() tipo kiek zinau
    with open("pets.json") as in_file:
        data = json.load(in_file)

    # print(data['pets'])
    all_pets = data['pets']

    # Uzduotis:
    # ishkirti all_pets kintamaji tipas list() i dvi dalis, irgi tipo dict(), vienoje tik sunys, kitoje tik kates,
    # ir irasyti i skirtingus json failus
    cats_dict = dict()  # dict() - {}, list() - [], tuple() - () dict(), list(), tuple(1, 2, )
    dogs_dict = dict()

    cats_dict['pets'] = []
    dogs_dict['pets'] = []

    for pet in all_pets:
        # print(pet)
        # print(type(pet))
        pet_species = pet.get('species')
        # print(pet_species)
        pet_name = pet.get('name')
        # print(pet_species, pet_name)
        if pet_species == 'Dog':
            # dogs_dict.update({pet_name: pet})  # .update(pet_name=pet)
            dogs_dict['pets'].append(pet)
        elif pet_species == 'Cat':
            # cats_dict[pet_name] = pet
            cats_dict['pets'].append(pet)
    print(dogs_dict)
    print(cats_dict)

    with open("dogs.json", 'w') as out_file:
        json.dump(dogs_dict, out_file, indent=4)

    with open("cats.json", 'w') as out_file:
        json.dump(cats_dict, out_file, indent=4)


