from CPL_Prep import FileReader
from os import path


class Interest:

    def interest_vector(self, tariff_generation):  # Todo improve to take one value of interest rate
        """
        This function selects the required interest vector  that should be used in the calculations based on tariff generation from the LifeTables.CSV
        :param tariff_generation: the interest vector is determined according to tariff generation
        :return: the required interest vector
        """
        relative_path = "/"
        csv_file_name = "Interest.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_file_name
        csv_reader = FileReader(csv_path)
        tariff_generation_string = str(tariff_generation)
        interest_vector_dict = csv_reader.readColumnFromCSV(tariff_generation_string, type=str)
        interest_vector = []
        x = len(interest_vector_dict)
        for i in range(0, x):
            value = interest_vector_dict[i]
            value1 = float(value)
            interest_vector.append(value1)
        return interest_vector
