# encoding: utf-8
import xlwt


class Writer(object):
    def __init__(self, info_element):
        self.info_element = info_element

    def record(self):
        font0 = xlwt.Font()
        font0.name = 'Times New Roman'
        font0.colour_index = 2
        font0.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font0

        style1 = xlwt.XFStyle()
        style1.num_format_str = 'D-MMM-YY'

        wb = xlwt.Workbook()
        # Шапка документа
        sheet = wb.add_sheet('Результаты импорта')
        sheet.write(0, 0, 'Элементная база', style0)
        sheet.write(0, 1, 'Хар-ка элементов', style0)
        sheet.write(0, 2, 'Количество элементов', style0)

        # Заполнение документа
        row_num = 1
        for element in self.info_element:
            sheet.write(row_num, 0, '{0} - {1}'.format(element[1], element[2]), style0)
            sheet.write(row_num, 1, '{0}'.format(element[0].character), style0)
            sheet.write(row_num, 2, '{0}'.format(element[0].count), style0)
            row_num += 1

        wb.save('example.xls')
