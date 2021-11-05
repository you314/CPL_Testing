from csv import DictReader


class FileReader:
    def __init__(self, path):
        self.path = path
        pass

    def readRowFromCSV(self, rowNumber, type=None):
        with open(self.path, newline='') as csvfile:
            reader = DictReader(csvfile, delimiter=';')
            for i in range(0, rowNumber+1):
                result = next(reader)
        if type is not None:
            result = self.mapDict(result, type)
        return result

    def readColumnFromCSV(self, identifier, type=None):
        with open(self.path, newline='') as csvfile:
            reader = DictReader(csvfile, delimiter=';')
            result = {}
            i = 0
            for x in reader:
                result[i] = x[identifier]
                i += 1
        if type is not None:
            result = self.mapDict(result, type)
        return result

    def readCSV(self, type=None):
        with open(self.path, newline='') as csvfile:
            reader = DictReader(csvfile, delimiter=';')
            result = {}
            i = 0
            for x in reader:
                result[i] = x
                i += 1
        if type is not None:
            def helper(dict):
                return self.mapDict(dict, type)
            result = self.mapDict(result, helper)
        return result

    @staticmethod
    def mapDict(dict, func):
        result = {k: func(v) for k, v in dict.items()}
        return result
