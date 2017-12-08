class BaseElement(object):
    def __init__(self, raw_string):
        try:
            self.name = raw_string[0]
            if len(raw_string[1]) == 0:
                self.character = None
            else:
                self.character = raw_string[1]
            self.count = int(raw_string[2])
        except IndexError as ie:
            print(ie)
