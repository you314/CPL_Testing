from helper.cpl_prep import FileReader
from os import path


class Flags:

    def create_matrix(self, tariff_generation, tariff: str):  # Todo Change the code to understandable one
        relative_path = "/"
        csv_filename = "formulas used.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        tariff_generation_dict = csv_reader.read_column_from_csv("tg", type=int)
        x0 = list(tariff_generation_dict.values())
        tariff_aux_dict = csv_reader.read_row_from_csv(0, type=str)
        x1 = list(tariff_aux_dict.keys())
        index_tg = x0.index(int(tariff_generation))
        index_tariff = x1.index(tariff)
        row_count = len(tariff_generation_dict)
        col_count = len(tariff_aux_dict)
        mat = []
        for i in range(row_count):
            x = csv_reader.read_row_from_csv(i)
            row_list = []
            for j in range(col_count):
                # you need to increment through dataList here, like this:
                y = x[x1[j]]
                row_list.append(y)
            mat.append(row_list)
        matrix_entry = mat[index_tg][index_tariff]
        return matrix_entry

    def flags_vector(self, tariff_generation, tariff: str):
        relative_path = "/"
        csv_filename = "Premium.FLags.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        flags_dict = csv_reader.read_column_from_csv(self.create_matrix(tariff_generation=tariff_generation, tariff=tariff), type=str)
        flags_vector = list(flags_dict)
        return flags_vector
