import base64
from bs4 import BeautifulSoup
from pprint import pprint

# Uzdavinys
    # 1. Esama funcionaluma perkelti i klase.
    # Klase turi paimti failo lokacija (export.MHTML) i init ir turi ishpjauti jusu geidziama HTML
    # dabar base64.b64decode(base64_encoded_part)
    # 2. Klase galetu nuskaityti toliau html ir padaryti objektus kuriuos irasys i excell faila
    # jau skirta zmogui patogiai ziureti.
    # Klase aprasykite po uzduotim, inicijuokite po if __name__ == "__main__":
    # ten kvieskite klases MHTML nuskaitymo ir xcell kurimo funcijas
    # rezultatas xcell failas.

if __name__ == "__main__":
    with open('export.MHTML', 'r') as f:
        file_data = f.read()
        # pprint(file_data, indent=4)
        base64_encoded_part = ''
        read_marker = False
        for nr, text_line in enumerate(file_data.split('\n')):
            # Surenku tas base64 sukodintas eilutes
            # print(text_line)
            if 'NextPart' in text_line and nr > 50:
                break
            if read_marker:
                base64_encoded_part += text_line
            if 'charset' in text_line:
                read_marker = True

        # Nukarpau \n ir tarpus kurie fore prisidejos
        base64_encoded_part = base64_encoded_part.strip()

        print(base64_encoded_part)
        # Paverciu i html
        soup = BeautifulSoup(base64.b64decode(base64_encoded_part), 'html.parser')
        pprint(soup.prettify(), indent=4)