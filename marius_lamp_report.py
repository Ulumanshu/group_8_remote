import codecs
from string import digits


class LampReport:

    right_code = "LD"
    left_code = "LK"
    right_special_key = "ST_PRM_lemp_matmuo_LDF"
    left_special_key = "ST_PRM_lemp_matmuo_LKF"
    sides = ['right', 'left']

    def __init__(self, input_file_path='', output_file_path=''):
        self.input_path = input_file_path
        self.output_path = output_file_path
        self.universal_variables = {}
        self.right_variables = {}
        self.left_variables = {}
        self.process_file_variables()
        self.order = str(self.universal_variables.get("Pardavimo_dokumentas", '') or '')
        self.roof_length_A = int(self.universal_variables.get("ST_plokstes_ilgis_A", 0) or 0)
        self.back_page_len_D = int(self.universal_variables.get("ST_PVC_galinio_lapo_ilgis_D", 0) or 0)
        self.front_page_len_F = int(self.universal_variables.get("ST_PVC_priekinio_lapo_ilgis_F", 0) or 0)
        self.full_pages = int(self.universal_variables.get("ST_PVC_pilnu_lapu_skaicius", 0) or 0)
        self.full_page_len_E = int(self.universal_variables.get("ST_PVC_pilnu_lapu_ilgis_E", 0) or 0)
        self.page_width = int(self.full_page_len_E / self.full_pages)
        self.right_special = int(self.right_variables.pop(self.right_special_key) or 0)
        self.left_special = int(self.left_variables.pop(self.left_special_key) or 0)
        self.sorted_right_values = self.sort_side_values(self.right_variables)
        self.sorted_left_values = self.sort_side_values(self.left_variables)
        self.calculated_right = []
        self.calculated_left = []

    def __call__(self, *args, **kwargs):
        for side in self.sides:
            self.generate_lamp_distance_list(side)
            self.generate_report_file(side)

    @staticmethod
    def get_string_digits(mod_string):
        res = ''
        for character in mod_string:
            if character in digits:
                res += character

        return res

    @staticmethod
    def sort_side_values(side_value_dict):
        sortable_tuple_list = [it for it in side_value_dict.items()]
        sorted_value_list = sorted(
            sortable_tuple_list,
            key=lambda tup: int(LampReport.get_string_digits(tup[0]))
        )

        return [sor[1] for sor in sorted_value_list]

    def process_file_variables(self):
        with open(self.input_path) as f:
            for line in f:
                name, value = line.split(".")
                if self.right_code in name:
                    self.right_variables[name.strip()] = int(value.strip())
                elif self.left_code in name:
                    self.left_variables[name.strip()] = int(value.strip())
                else:
                    self.universal_variables[name.strip()] = int(value.strip())

    def generate_lamp_distance_list(self, side):
        if side in self.sides:
            if side == 'right':
                lamp_distance_list = self.calculated_right
                first_member = self.front_page_len_F - self.right_special
                input_variables = self.sorted_right_values
            elif side == 'left':
                lamp_distance_list = self.calculated_left
                first_member = self.front_page_len_F - self.left_special
                input_variables = self.sorted_left_values

            lamp_distance_list.append(first_member)
            lamp_count = 0
            for page_index in range(self.full_pages - 1, -1, -1):
                if input_variables[page_index] > 0:
                    lamp_distance_list[-1] += input_variables[page_index]
                    lamp_distance_list.append(self.page_width - input_variables[page_index])
                    lamp_count += 1
                else:
                    lamp_distance_list[-1] += self.page_width
            if side == 'left':
                lamp_distance_list.pop(-1)
            else:
                lamp_distance_list[-1] = lamp_distance_list[-1] + self.back_page_len_D

            lamp_distance_list.reverse()
            for i in range(0, 8):
                if i >= lamp_count:
                    lamp_distance_list.append(0)

        else:
            raise ValueError("Side must be 'left' or 'right'!!!")

    def generate_report_file(self, side):
        if side in self.sides:
            if side == 'right':
                lamp_distance_list = self.calculated_right
                side_code = self.right_code
                beletristics = 'dešinėje'

            elif side == 'left':
                lamp_distance_list = self.calculated_left
                side_code = self.left_code
                beletristics = 'kairėje'

            with codecs.open(f"{self.output_path + '_' + side}.txt", 'w', 'utf-8') as f:
                tekstas = [
                    '\n',
                    f'Užsakymas {self.order}\n',
                    '\n',
                    'Brėžinys D2091103\n',
                    '\n',
                    f'Lempų grandinė {beletristics}:\n'
                ]
                f.writelines(tekstas)
                for i in range(0, 8):
                    f.write(f'{side_code}{str(i + 1)} = {lamp_distance_list[i]} mm \n')
        else:
            raise ValueError("Side must be 'left' or 'right'!!!")


if __name__ == "__main__":
    lamp_report = LampReport(input_file_path='input.txt', output_file_path='output')
    lamp_report()
