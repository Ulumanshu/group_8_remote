import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Alice has a cat", "Python programming is great"),
    'c': [False, True, False]
}

# # Saving to pickle
# with open('betkokspavpicklui.pickle', 'wb') as f:
#     pickle.dump(data, f)


# Loading from pickle
with open('betkokspavpicklui.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)
