import json

class JSONDATA:
    def __init__(self, data=[], path=None):
        self.Jsonfile = data
        self.JSONDATA = list()
        self.path = path

        self.OPEN_JSON_DATA()

    def OPEN_JSON_DATA(self):
        for each_file in self.Jsonfile:
            with open(self.path + "/" + each_file, 'r', encoding='UTF8') as json_file:
                self.JSONDATA.append(json.load(json_file))

