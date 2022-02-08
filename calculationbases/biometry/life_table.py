from os import path
from CPLTesting.helper.cpl_prep import FileReader
from CPLTesting.input.contract import ContractDTO


class LifeTable:

    def __init__(self, contract_nr):
        """
         Initializes required life tables to be used in calculations based on tariff generation from the LifeTables.CSV
         :param contract_nr: the life table is determined according to contract_nr
        """
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        relative_path = "/"
        csv_filename = "LifeTables.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        self.csv_reader = FileReader(csv_path)
        self.tg_dict = self.csv_reader.read_column_from_csv("tg", type=int)
        self.tg_list = list(self.tg_dict.values())

    def death_probability_table(self) -> str:
        """
        :return: Name of the death (active) probability table
        """
        life_table_name_dict = self.csv_reader.read_column_from_csv("Life_Table_csv_name", type=str)
        tg_index = self.tg_list.index(self.contractDTO.tg())  # gets the index of the required tariff generation
        return life_table_name_dict[tg_index]  # gets the required life table based on the index number

    def disability_probability_table(self) -> str:
        """
        :return: Name of the disability probability table
        """
        disability_table_name_dict = self.csv_reader.read_column_from_csv("Disability_Table_csv_name", type=str)
        tg_index = self.tg_list.index(self.contractDTO.tg())  # gets the index of the required tariff generation
        return disability_table_name_dict[tg_index]  # gets the required life table based on the index number

    def disabled_death_probability_table(self) -> str:
        """
        :return: Name of the death (disabled) probability table
        """
        return "TableABC"

    def disable_reactivation_probability_table(self) -> str:
        """
        :return: Name of the reactivation (disabled) probability table
        """
        return "TableCBA"
