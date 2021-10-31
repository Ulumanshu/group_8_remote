import json

with open("pets.json") as in_file:
    data = json.load(in_file)

print(data['pets'])

