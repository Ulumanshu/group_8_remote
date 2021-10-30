import openpyxl
# import xlsxwriter
from xlsxwriter.workbook import Workbook
from pprint import pprint


def get_xlsx_sheet_data(xlsx_file_path):
    wb_obj = openpyxl.load_workbook(xlsx_file_path)
    sheet = wb_obj.active
    res = []
    for row_ in sheet.iter_rows():
        row_values = []
        for cell in row_:
            row_values.append(cell.value)

        res.append(row_values)

    return res


if __name__ == "__main__":
    xlsx_file = '/home/wooden/workspace/sdacademy/group_8_remote/my_file.xlsx'
    excell_data = get_xlsx_sheet_data(xlsx_file)
    pprint(excell_data, indent=4)

    workbook = Workbook('result.xlsx')
    worksheet = workbook.add_worksheet(str('Sheet1'))
    for row, data_line in enumerate(excell_data):
        for col, data_value in enumerate(data_line):
            worksheet.write(row, col, data_value)  # Writes None

    workbook.close()
