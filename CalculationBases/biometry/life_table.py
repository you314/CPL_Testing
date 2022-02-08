from os import path
from helper.cpl_prep import FileReader
from input.contract import ContractDTO


class LifeTable(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        """
         This function selects the required life table that should be used in the calculations based on tariff generation from the LifeTables.CSV
         :param contract_nr: the life table is determined according to contract_nr
         :return: the required life table
        """
        relative_path = "/"
        csv_filename = "LifeTables.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        self.csv_reader = FileReader(csv_path)
        self.tg_dict = self.csv_reader.read_column_from_csv("tg", type=int)
        self.tg_list = list(self.tg_dict.values())

    def death_probability_table(self):
        life_table_name_dict = self.csv_reader.read_column_from_csv("Life_Table_csv_name", type=str)
        tg_index = self.tg_list.index(self.tg())  # gets the index of the required tariff generation
        return life_table_name_dict[tg_index]  # gets the required life table based on the index number

    def disability_probability_table(self):
        disability_table_name_dict = self.csv_reader.read_column_from_csv("Disability_Table_csv_name", type=str)
        tg_index = self.tg_list.index(self.tg())  # gets the index of the required tariff generation
        return disability_table_name_dict[tg_index]  # gets the required life table based on the index number

    def disabled_death_probability_table(self):
        return 0

    def disable_reactivation_probabilty_table(self):
        return 0
