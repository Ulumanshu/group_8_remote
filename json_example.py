import json


if __name__ == "__main__":
    # Nuskaito json faila, sukuria data kintamaji kuriame failo turinys yra pitono objekte
    # dict() arba list() tipo kiek zinau
    with open("pets.json") as in_file:
        data = json.load(in_file)

    print(data['pets'])
    all_pets = data['pets']

    # Uzduotis:
    # ishkirti all_pets kintamaji tipas dict() i dvi dalis, irgi tipo dict(), vienoje tik sunys, kitoje tik kates,
    # ir irasyti i skirtingus json failus


    # Iraso pitono objekta i json faila, suformatuoja objekta (kabutes, atstumai, etc.) kad atitiktu json formata
    with open("output.json", 'w') as out_file:
        json.dump(all_pets, out_file, indent=4)




