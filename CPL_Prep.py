from csv import DictReader


class FileReader:
    def __init__(self, path):
        self.path = path
        pass

    def read_row_from_csv(self, row_number, type=None):
        with open(self.path, newline='') as csvfile:
            reader = DictReader(csvfile, delimiter=';')
            for i in range(0, row_number+1):
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

    def create_mapping_by_key(self, key_name):
        """
        This function creates a dictionary for each row of the csv with the a specified column as key
        :param key_name: Determines, which column of the csv is used as key
        :return: dictionary with specified key
        """
        with open(self.path, newline='') as csvfile:
            reader = DictReader(csvfile, delimiter=';')
            mapping = dict()
            for row in reader:
                key = row[key_name]
                value = row.copy()
                mapping[key] = value
        return mapping


