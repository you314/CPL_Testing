from os import path
from helper.cpl_prep import FileReader
from input.json_reader import JsonReader


class LifeTable:
    """
    *description*
    """

    def __init__(self):
        """
        Initializes required life tables to be used in calculations based on tariff generation from the LifeTables.csv
        :param contract_nr: the life table is determined according to contract_nr
        """
        self.contractDTO = JsonReader
        relative_path = "/"
        csv_filename = "LifeTables.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        self.csv_reader = FileReader(csv_path)
        self.tariff_generation_dict = self.csv_reader.read_column_from_csv("tariff_name", type=str)
        self.tariff_generation_list = list(self.tariff_generation_dict.values())


    # #def probability_table_of(self, table_type) -> str:
    #     table_name_dict = []
    #     if table_type == 'life':
    #         table_name_dict = self.csv_reader.read_column_from_csv("Life_Table_csv_name", type=str)
    #     elif table_type == 'disability':
    #         table_name_dict = self.csv_reader.read_column_from_csv("Disability_Table_csv_name", type=str)
    #     elif table_type == 'disabled_life':
    #         table_name_dict = self.csv_reader.read_column_from_csv("_Table_csv_name", type=str)
    #     elif table_type == 'disable_reactivation':
    #         table_name_dict = self.csv_reader.read_column_from_csv("_Table_csv_name", type=str)
    #
    #     tariff_generation_index = self.tariff_generation_list.index(self.contractDTO.tariff_generation())
    #     return table_name_dict[tariff_generation_index]

    # the above function can replace all four below
    ###########################################################################################################

    def death_probability_table(self) -> str:
        """
        :return: Name of the death (active) probability table
        """
        life_table_name_dict = self.csv_reader.read_column_from_csv("Life_Table_csv_name", type=str)
        # gets the index of the required tariff generation
        tariff_generation_index = self.tariff_generation_list.index(self.contractDTO.tariff_name())
        # gets the required life table based on the index number
        return life_table_name_dict[tariff_generation_index]

    def disability_probability_table(self) -> str:
        """
        :return: Name of the disability probability table
        """
        disability_table_name_dict = self.csv_reader.read_column_from_csv("Disability_Table_csv_name", type=str)
        # gets the index of the required tariff generation
        tariff_generation_index = self.tariff_generation_list.index(self.contractDTO.tariff_name())
        # gets the required life table based on the index number
        return disability_table_name_dict[tariff_generation_index]

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
print(LifeTable().death_probability_table())



