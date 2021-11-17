from os import path
from CPL_Prep import FileReader
from Contract import ContractDTO


class LifeTable(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        """
         This function selects the required life table  that should be used in the calculations based on tariff generation from the LifeTables.CSV
         :param contract_nr: the life table is determined according to contract_nr
         :return: the required life table
        """
        relative_path = "/"
        csv_filename = "LifeTables.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.tg_dict = csv_reader.read_column_from_csv("tg", type=int)
        self.life_table_name_dict = csv_reader.read_column_from_csv("Life Table csv name", type=str)
        self.tg_list = list(self.tg_dict.values())
        tg_index = self.tg_list.index(self.tg())  # gets the index of the required tariff generation
        self.life_table_name = self.life_table_name_dict[tg_index]  # gets the required life table based on the index number
