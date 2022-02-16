from csv import DictReader

class FileReader:
    """
    *description*

    We should consider using pandas or numpy to read and write from data.
    Performance issues will not be traced back on such well designed libraries, but our code
    and the huge amount of file access of reading basic probabilities instead of commutative values. (note by Timon)
    """

    def __init__(self, path):
        self.path = path
        pass

    def read_row_from_csv(self, row_number, type=None):
        with open(self.path, newline='') as csv_file:
            reader = DictReader(csv_file, delimiter=';')
            # result = reader[-1] # is the same as below, but without the iteration
            for i in range(row_number):
                result = next(reader)
            ######################

        if type is not None:
            return self.map_dict(result, type)

    def read_column_from_csv(self, identifier, type=None):
        result = {}
        with open(self.path, newline='') as csv_file:
            reader = DictReader(csv_file, delimiter=';')
            i = 0
            for x in reader:
                result[i] = x[identifier]
                i += 1

        if type is not None:
            return self.map_dict(result, type)

    def read_csv(self, type=None):
        result = {}
        with open(self.path, newline='') as csv_file:
            reader = DictReader(csv_file, delimiter=';')
            i = 0
            for x in reader:
                result[i] = x
                i += 1

        def helper(dict):
            return self.map_dict(dict, type)

        if type is not None:
            return self.map_dict(result, helper)

    @staticmethod
    def map_dict(dict, func):
        return {k: func(v) for k, v in dict.items()}

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


