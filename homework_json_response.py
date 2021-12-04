# -*- coding: utf-8 -*-
import json

import openpyxl
from homework_1_excell import AtaskaituKlase, ExelioEilute
from pprint import pprint


class ModifiedAtaskaituKlase(AtaskaituKlase):

    def get_requested_stats(self, keyword):
        """
        agr1 keyword: may be one of the following options ['regions', 'items', 'representatives']
        :return: python list with dictionaries of requested report objects for json serialization
        """
        keyword_map = {'regions': self.regions, 'items': self.items, 'representatives': self.representatives}
        res = []
        report_objects = keyword_map.get(keyword, []) or []
        for rep_obj in report_objects:
            # subres = dict()
            rep_obj.generate_stats()
            pradres = rep_obj.self_as_dict_deep()

            naujas_rezult = pradres.pop(keyword)[0]
            naujas_rezult["other_data"] = pradres
            # report_name = naujas_rezult and naujas_rezult[0].get("name") or ''
            # subres[report_name] = naujas_rezult
            # subres[report_name].append(rep_obj.self_as_dict_deep())
            res.append(naujas_rezult)

            naujas_rezult = rep_obj.self_as_dict_deep().get(keyword)
            print(naujas_rezult)

        return res

    def create_json_file(self, user_inputas):
        data_for_json = []
        if user_inputas == 'regions':
            data_for_json = ataskaitu_generatorius.get_requested_stats('regions')
            pprint(data_for_json, indent=4)

        elif user_inputas == 'items':
            data_for_json = ataskaitu_generatorius.get_requested_stats('items')
            pprint(data_for_json, indent=4)

        elif user_inputas == 'representatives':
            data_for_json = ataskaitu_generatorius.get_requested_stats('representatives')
            pprint(data_for_json, indent=4)

        with open(f"{user_inputas}.json", "w") as out_file:
            json.dump(data_for_json, out_file, indent=4)


if __name__ == "__main__":
    file_location_name = "./homework.xlsx"
    line_object_list = []
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
        # print(xlsx_line)
        eilutes_data = xlsx_line[0]
        eilutes_salis = xlsx_line[1]
        eilutes_pardavejas = xlsx_line[2]
        eilutes_produktas = xlsx_line[3]
        eilutes_prod_kiekis = xlsx_line[4]
        eilutes_prod_kaina = xlsx_line[5]
        eilutes_viso = xlsx_line[6]
        excell_line = ExelioEilute(
            ln_count,
            eilutes_data,
            eilutes_salis,
            eilutes_pardavejas,
            eilutes_produktas,
            eilutes_prod_kiekis,
            eilutes_prod_kaina,
            eilutes_viso
        )
        line_object_list.append(excell_line)

    ataskaitu_generatorius = ModifiedAtaskaituKlase(line_object_list)
    ataskaitu_generatorius.generate_stats()

    user_inputas = input("Įveskite norimą ataskaitą: ")
    user_inputas = str(user_inputas)

    ataskaitu_generatorius.create_json_file(user_inputas)

    # Pavyzdys kaip naudoti get_requested_stats
    # if user_inputas == 'regions':
    #     data_for_json = ataskaitu_generatorius.get_requested_stats('regions')
    #     pprint(data_for_json, indent=4)
    #
    # elif user_inputas == 'items':
    #     data_for_json = ataskaitu_generatorius.get_requested_stats('items')
    #     pprint(data_for_json, indent=4)
    #
    # elif user_inputas == 'representatives':
    #     data_for_json = ataskaitu_generatorius.get_requested_stats('representatives')
    #     pprint(data_for_json, indent=4)

    '''Uzduotis sukurti zemiau funcija kuri gavusi raktazodi
    viena is siu ['regions', 'items', 'representatives'],
    ishsaugotu duomenu ataskaitos dictionary json formatu i failiuka, su jusu pasirinktu pavadinimu
    sukurta funcija paleisti ir parodyti man koki gavoji jsonai

    PS
    Uzduociai atlikti yrasiau i EXS klase dvi funkcijas kad gautume dicta (self_as_dict_deep, self_as_dict)
    taipat ikeliau papildoma metoda get_requested_stats i AtaskaituKlase ja paveldedamas
    naudokites get_requested_stats savo funcijoje jei patiems bus per sunku.
    uzduoties esme ishmokti panaudoti get_requested_stats, ir jos resultatus uzseivinti i json failus.'''

    # def self_as_dict(self):
    #     res = dict()
    #     res['name'] = self.name
    #     res['parent_total'] = self.parent_total
    #     res['total_percent'] = self.total_percent
    #
    #     print(res)
    #     return res
    #
    #
    # def self_as_dict_deep(self):
    #     res = dict()
    #     res['regions'] = list()
    #     res['items'] = list()
    #     res['representatives'] = list()
    #
    #     for reg in self.regions:
    #         res['regions'].append(reg.self_as_dict())
    #
    #     for it in self.items:
    #         res['items'].append(it.self_as_dict())
    #
    #     for rep in self.representatives:
    #         res['representatives'].append(rep.self_as_dict())
    #
    #     return res




