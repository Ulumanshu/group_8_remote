# -*- coding: utf-8 -*-

import openpyxl
from io import BytesIO
import base64


file_location_name = "./homework.xlsx"
# 1. Pasirasyti pora klasiu duomenu is exelio eilutems talpinti (Klases Regionams, Pardavejams ir Itemams)
# 2. Sutalpinus duomenis is savo strukturas tu klasiu objektuose, paruosti duomenis eksportui i tris ataskaitas.
    # * Regionai pagal pardavimus (Total stulpelis), turi buti sekmingiausio regione pardavejo ir produkto laukai su ju %
    # nuo bendros regiono apyvartos
    # * Pardavejai pagal pardavimus ir sekmingiausias regionas, labiausiai parduodama preke su % nuo visu pardavejo pardavimu
    # * Itemai pagal pargavimus geriausias regionas/pardavejas ir ju %.
if __name__ == "__main__":
    wb = openpyxl.load_workbook(
        filename=file_location_name,
        read_only=True,
    )
    ws = wb.active
    ln_count = 0

    for xlsx_line in ws.iter_rows(
            min_row=1,  # Adjust this if header size changes, index of row from witch to read file (starts from 1)
            max_row=None,
            min_col=None,
            max_col=None,
            values_only=True
    ):
        ln_count += 1
        print(xlsx_line)
