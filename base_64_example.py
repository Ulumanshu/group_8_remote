import base64
from bs4 import BeautifulSoup
with open('base64_text.txt', 'r') as f:
    file_data = f.read()
    print(file_data)
    # print(base64.b64decode(file_data))
    soup = BeautifulSoup(base64.b64decode(file_data), 'html.parser')
    print(soup.prettify())
