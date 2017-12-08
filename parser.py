import csv
from element import BaseElement


class Parser(object):
    def __init__(self, _fname):
        self.filename = _fname

    def read_file(self):
        try:
            csvfile = open(self.filename, 'r')
            raw_data = csv.reader(csvfile, delimiter=',')
            all_element = []
            for row in raw_data:
                all_element.append(BaseElement(row))
            csvfile.close()
            return all_element
        except OSError:
            print("I can't open file %s", self.filename)

    def prepare_output(self, all_element):
        result = [[all_element[0], all_element[0].name,  all_element[0].name]]
        for it in range(1, len(all_element)):
            if all_element[it].name[0] == result[-1][0].name[0] or all_element[it].name[:2] == result[-1][0].name[:2]:
                if all_element[it].character == result[-1][0].character:
                    result[-1][0].count += all_element[it].count
                    result[-1][2] = all_element[it].name
                else:
                    result.append([all_element[it], all_element[it].name, all_element[it].name])
            else:
                result.append([all_element[it], all_element[it].name, all_element[it].name])
        return result
        # for element in result:
        #     print('{0} - {1}: count: {2}, info: {3}'.format(element[1], element[2], element[0].count, element[0].character))