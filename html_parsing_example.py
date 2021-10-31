from bs4 import BeautifulSoup
from pprint import pprint


def sort_complicated_stuff(some_tuple_from_big_list):
    char_digits = ''
    first_member = some_tuple_from_big_list[0]
    for symbol in first_member:
        if symbol.isdigit():
            char_digits += symbol
    # print(char_digits)
    if not char_digits:
        char_digits += '0'

    char_digits = int(char_digits)
    if "LD" in first_member:
       char_digits += 100

    return char_digits


example_file = 'html_example.html'

store_data = {}

with open(example_file) as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    all_table_lines = soup.find_all('tr')

    for line_number, table_line in enumerate(all_table_lines):
        if line_number == 0:
            continue
        line_columns = table_line.find_all('td')
        key = ''
        value = ''
        for column_number, col in enumerate(line_columns):

            if column_number == 2:
                key = col.text
            if column_number == 3:
                value = int(col.text)

        store_data[key] = value

# pprint(store_data, indent=4)
sortable_tuple_list = store_data.items()
sorted_data = sorted(sortable_tuple_list, key=sort_complicated_stuff)
pprint(sorted_data, indent=4)




