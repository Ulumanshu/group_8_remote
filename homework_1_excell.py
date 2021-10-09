# -*- coding: utf-8 -*-

import openpyxl
from io import BytesIO
import base64


class EXS:
    def __init__(self, data_lines):
        self.lines = data_lines
        self.regions = []
        self.items = []
        self.representatives = []

    def sort_by_field(self, parameter='country', report_obj=None):
        res = []
        # susirenkam uniklaius irasus pagal pateikta lauka
        unique_parameters = set()
        for eil in self.lines:
            unique_parameters.add(getattr(eil, parameter))

        # Randam exelio eilutes pagal ta lauka
        for uniq_parameter in unique_parameters:
            parameter_lines = [ln for ln in self.lines if getattr(ln, parameter) == uniq_parameter]
            region_object = EXS_Region(parameter_lines)
            res.append(region_object)

        return res

    def exs_region(self):
        rep_objects = self.sort_by_field(parameter='country', report_obj=EXS_Region)
        self.regions = rep_objects

    def exs_rep(self):
        rep_objects = self.sort_by_field(parameter='salesperson', report_obj=EXS_Rep)
        self.representative = rep_objects

    def exs_item(self):
        rep_objects = self.sort_by_field(parameter='product', report_obj=EXS_Item)
        self.items = rep_objects


class EXS_Region(EXS):
    def __init__(self, region_lines):
        super(EXS_Region, self).__init__(region_lines)

    @property
    def total_sold(self):
        return sum([float(e.total) for e in self.lines])


class EXS_Rep(EXS):
    def __init__(self, salesman_lines):
        super(EXS_Rep, self).__init__(salesman_lines)

    @property
    def total_sold(self):
        return sum([float(e.total) for e in self.lines])


class EXS_Item(EXS):
    def __init__(self, item_lines):
        super(EXS_Item, self).__init__(item_lines)

    @property
    def total_sold(self):
        return sum([float(e.total) for e in self.lines])


class ExelioEilute:
    def __init__(
            self,
            nr,
            date,
            country,
            salesperson,
            product,
            product_qty,
            product_unit_price,
            price_total,
    ):
        self.nr = nr
        self.date = date
        self.country = country
        self.salesperson = salesperson
        self.product = product
        self.product_qty = product_qty
        self.unit_price = product_unit_price
        self.total = price_total

    def __repr__(self):
        return f"Nr. {self.nr}, {self.country}, {self.salesperson}, {self.product}"


class AtaskaituKlase(EXS):
    def __init__(self):
        init_lines = []
        super(AtaskaituKlase, self).__init__(init_lines)


file_location_name = "./homework.xlsx"
# 1. Pasirasyti pora klasiu duomenu is exelio eilutems talpinti (Klases Regionams, Pardavejams ir Itemams)
# 2. Sutalpinus duomenis is savo strukturas tu klasiu objektuose, paruosti duomenis eksportui i tris ataskaitas.
    # * Regionai pagal pardavimus (Total stulpelis), turi buti sekmingiausio regione pardavejo ir produkto laukai su ju %
    # nuo bendros regiono apyvartos
    # * Pardavejai pagal pardavimus ir sekmingiausias regionas, labiausiai parduodama preke su % nuo visu pardavejo pardavimu
    # * Itemai pagal pargavimus geriausias regionas/pardavejas ir ju %.
if __name__ == "__main__":
    ataskaitu_generatorius = AtaskaituKlase()
    wb = openpyxl.load_workbook(
        filename=file_location_name,
        read_only=True,
    )
    ws = wb.active
    ln_count = 0

    for xlsx_line in ws.iter_rows(
            min_row=2,  # Adjust this if header size changes, index of row from witch to read file (starts from 1)
            max_row=None,
            min_col=None,
            max_col=None,
            values_only=True
    ):
        ln_count += 1
        print(xlsx_line)
        eilutes_data = xlsx_line[0]
        eilutes_salis = xlsx_line[1]
        eilutes_pardavejas = xlsx_line[2]
        eilutes_produktas = xlsx_line[3]
        eilutes_prod_kiekis = xlsx_line[4]
        eilutes_prod_kaina = xlsx_line[5]
        eilutes_viso = xlsx_line[6]
        eilute = ExelioEilute(
            ln_count,
            eilutes_data,
            eilutes_salis,
            eilutes_pardavejas,
            eilutes_produktas,
            eilutes_prod_kiekis,
            eilutes_prod_kaina,
            eilutes_viso
        )
        ataskaitu_generatorius.lines.append(eilute)

    ataskaitu_generatorius.exs_region()
    ataskaitu_generatorius.exs_rep()
    ataskaitu_generatorius.exs_item()

    for reg in ataskaitu_generatorius.regions:
        print(reg.total_sold)

    for item in ataskaitu_generatorius.items:
        print(item.total_sold)

    for rep in ataskaitu_generatorius.representatives:
        print(rep.total_sold)