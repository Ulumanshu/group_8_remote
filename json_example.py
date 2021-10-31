import json


if __name__ == "__main__":
    # Nuskaito json faila, sukuria data kintamaji kuriame failo turinys yra pitono objekte
    # dict() arba list() tipo kiek zinau
    with open("pets.json") as in_file:
        data = json.load(in_file)

    print(data['pets'])
    all_pets = data['pets']

    # Uzduotis:
    # ishkirti all_pets kintamaji tipas list() i dvi dalis, irgi tipo dict(), vienoje tik sunys, kitoje tik kates,
    # ir irasyti i skirtingus json failus
    cats_dict = dict()  # dict() - {}, list() - [], tuple() - () dict(), list(), tuple(1, 2, )
    dogs_dict = dict()
    split_keys = [('Cat', cats_dict), ('Dog', dogs_dict)]
    for split_key in split_keys:
        species_name = split_key[0]
        species_dictionary = split_key[1]
        print(split_key, species_name, species_dictionary)
        for pet in all_pets:
            pet_species = pet.get('species', '') or ''
            pet_name = pet.get('name', '') or ''
            if pet_species == species_name:
                species_dictionary[pet_name] = pet
        print(split_key, species_name, species_dictionary)


        # Iraso pitono objekta i json faila, suformatuoja objekta (kabutes, atstumai, etc.) kad atitiktu json formata
        with open(f"{species_name}.json", 'w') as out_file:
            json.dump(species_dictionary, out_file, indent=4)
