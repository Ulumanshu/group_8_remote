# -*- coding: utf-8 -*-

from copy import deepcopy

if __name__ == "__main__":
    # kitokios taisykles simple ir complex datai
    simple_data = 5  # "abc", ('abs', 5)
    complex_data = ['abc', 5]  # setai, kiti dictionariai {} ir custominiai objektai
    sample_dict = {'key1': 5, 'key2': 'abc', 'key3': complex_data}

    new_dict = sample_dict.copy()  # Sukuria nauja isorini dicta su tuo pat turiniu (ty visi kompleksiniai kintamieji jame tie patys)
    new_dict3 = dict(sample_dict)  # Sukuria nauja isorini dicta su tuo pat turiniu (ty visi kompleksiniai kintamieji jame tie patys)

    new_dict4 = sample_dict  # nauja nuoroda i ta pati sample dict

    new_dict2 = deepcopy(sample_dict) # visikai nauja pagrindinio dicto ir visu kompleksiniu kintamuju jame kopija


    complex_data.append(6)
    sample_dict['key1'] = 19
    sample_dict['key3'].append(19)

    print('sample dict - original', sample_dict)
    print('simple copy', new_dict)
    print('deep copy', new_dict2)
    print('simple copy new dict()', new_dict3)
    print('just assigment to new variable', new_dict4)



    api_response = {
        'country': {
            'latitude': 2.0000,
            'capital': "Vilnius",
        },
        'country': {
            'latitude': 2.0000,
            'capital': "Vilnius",
        }

    }