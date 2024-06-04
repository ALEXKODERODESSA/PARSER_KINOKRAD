import xlsxwriter
from pars_filmi_reiting_3 import funk_iz_main


def save_to_excel(filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet('MOVIES_REITING_80')

    row = 0
    column = 0

    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 50)
    worksheet.set_column('D:D', 50)

    for i in funk_iz_main():
        name_film = i['name_film']
        reiting = i['reiting']
        span_yes = i['span_yes']
        link_film = i['link_film']

        worksheet.write(row, column, name_film)
        worksheet.write(row, column + 1, reiting)
        worksheet.write(row, column + 2, span_yes)
        worksheet.write(row, column + 3, link_film)

        row += 1

    workbook.close()

save_to_excel(r'/Users/alexandr/Desktop/SPARSIL.xlsx')


