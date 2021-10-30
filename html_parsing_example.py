from bs4 import BeautifulSoup

example_file = 'html_example.html'

with open(example_file) as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    all_p_elements = soup.find_all('p')
    print(all_p_elements)
    print(type(all_p_elements))
    for found_element in all_p_elements:
        print(found_element)
        print(type(found_element))
