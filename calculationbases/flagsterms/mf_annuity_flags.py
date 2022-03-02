from helper.cpl_prep import FileReader
from os import path


class Flags():
    """
    *description*
    """

    def gross_premium_flags_vector(self, tariff: str) -> list[int]:
        relative_path1 = "/"
        csv_filename1 = "formulas used.csv"
        csv_path1 = path.dirname(__file__) + relative_path1 + csv_filename1
        csv_reader1 = FileReader(csv_path1)
        tariff_dict = csv_reader1.read_column_from_csv("Tariff", type=str)
        BEB_dict = csv_reader1.read_column_from_csv("BEB", type=str)
        x0 = list(tariff_dict.values())
        index_tariff = x0.index(tariff)
        formula_NR = BEB_dict[index_tariff]
        relative_path = "/"
        csv_filename = "Premium.FLags.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        flags_dict = csv_reader.read_column_from_csv(formula_NR, type=int)
        flags_vector = list(flags_dict.values())
        return flags_vector


print





