import openpyxl
import xlsxwriter


def get_xlsx_sheet_data(xlsx_file_path):
    wb_obj = openpyxl.load_workbook(xlsx_file_path)
    sheet = wb_obj.active
    res = []
    for row_ in sheet.iter_rows(max_col=10, min_row=1, max_row=1000):
        row_values = []
        for cell in row_:
            row_values.append(cell.value)

        res.append(row_values)

    return res


if __name__ == "__main__":
    xlsx_file = '/home/wooden/workspace/sdacademy/group_8_remote/my_file.xlsx'
    excell_data = get_xlsx_sheet_data(xlsx_file)
    print(excell_data)
