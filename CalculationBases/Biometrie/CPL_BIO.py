from math import exp
from os import path
from CPL_Prep import FileReader
from CalculationBases.Biometrie.LifeTable import LifeTable
from Contract import ContractDTO


class BiometryCpl(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        """
        This function initialises the required probability vectors and trend factors in order to use it later in calculation of probability with trend factors
        :param contract_nr: the life table is determined according to contract_nr
        :return: probability vectors
        """
        self.life_table = LifeTable(contract_nr=contract_nr)
        self.life_table_name = self.life_table.LifetablecsvName
        relative_path = "/"
        csv_filename = self.life_table_name
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.age_dict = csv_reader.readColumnFromCSV("AGE", type=float)
        if self.sex() == "male":
            self.q_x_dict = csv_reader.readColumnFromCSV("q_xm", type=float)
            self.trend_dict = csv_reader.readColumnFromCSV("trend_m", type=float)
        elif self.sex() == "female":
            self.q_x_dict = csv_reader.readColumnFromCSV("q_xw", type=float)
            self.trend_dict = csv_reader.readColumnFromCSV("trend_w", type=float)
        self.MAX_AGE = 121

    def q_x_vector(self, birth_date: int):
        """
         This function initialises the required death probability vector with trend factors in order to use it later in calculation of probability with trend factors
         :param birth_date: the birth year of the insured person
         :return: death probability vector
        """
        max_age = self.MAX_AGE
        qx_vector = []
        for age in range(0, max_age + 1):
            qx = self.q_x_dict[age] * exp(-(birth_date + age - 1999) * self.trend_dict[age])
            qx_vector.append(qx)
        return qx_vector

    def one_year_death_probability(self, age, birth_date):
        """
        This function initialises the required one year death probability with taking in consideration the trend factor
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year death probability
        """
        qx_vector = self.q_x_vector(birth_date=birth_date)
        qx = qx_vector[age]
        return qx

    def one_year_survival_probability(self, age, birth_date):
        """
        This function initialises the required one year survival probability with taking in consideration the trend factor
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year survival probability
        """
        result = 1 - self.one_year_death_probability(age, birth_date=birth_date)
        return result

    def n_year_survival_probability(self, n, age, birth_date):
        """
        This function initialises the required n year death probability with taking in consideration the trend factor
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :param n: the period in which the required probability is calculated
        :return: n year death probability
        """
        qx_vector = self.q_x_vector(birth_date=birth_date)
        if n <= 0:
            result = 1
        elif age >= len(qx_vector) - 1:
            result = 0
        else:
            result = 1
            for i in range(age, age + n):
                result *= self.one_year_survival_probability(age=i, birth_date=birth_date)
        return result


print(BiometryCpl(contract_nr=1234).q_x_vector(1960))
