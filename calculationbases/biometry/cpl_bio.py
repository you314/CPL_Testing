from math import exp
from os import path
from helper.cpl_prep import FileReader
from calculationbases.biometry.life_table import LifeTable
from input.contract import ContractDTO


class BiometryCpl(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        """
        This function initialises the required probability vectors and trend factors in order to use it later in calculation of probability with trend factors
        :param contract_nr: the life table is determined according to contract_nr
        :return: probability vectors
        """
        self.life_table = LifeTable(contract_nr=contract_nr)
        self.death_table_name = self.life_table.death_probability_table()
        self.disability_table_name = self.life_table.disability_probability_table()
        relative_path = "/"
        death_csv_filename = self.death_table_name
        death_csv_path = path.dirname(__file__) + relative_path + death_csv_filename
        death_csv_reader = FileReader(death_csv_path)
        self.death_age_dict = death_csv_reader.read_column_from_csv("AGE", type=float)
        if self.sex() == "male":
            self.q_x_dict = death_csv_reader.read_column_from_csv("q_xm", type=float)
            self.trend_dict = death_csv_reader.read_column_from_csv("trend_m", type=float)
        elif self.sex() == "female":
            self.q_x_dict = death_csv_reader.read_column_from_csv("q_xw", type=float)
            self.trend_dict = death_csv_reader.read_column_from_csv("trend_w", type=float)
        self.death_min_age = list(self.death_age_dict.keys())[0]
        self.death_max_age = list(self.death_age_dict.keys())[-1]

        disability_csv_filename = self.disability_table_name
        disability_csv_path = path.dirname(__file__) + relative_path + disability_csv_filename
        disability_csv_reader = FileReader(disability_csv_path)
        if self.sex() == "male":
            group_name = "Group_" + self.profession() + "_m"
        elif self.sex() == "female":
            group_name = "Group_" + self.profession() + "_f"
        self.disability_age_dict = disability_csv_reader.read_column_from_csv("AGE", type=float)
        self.i_x_dict = disability_csv_reader.read_column_from_csv(group_name, type=float)
        self.disability_min_age = list(self.disability_age_dict.keys())[0]
        self.disability_max_age = list(self.disability_age_dict.keys())[-1]

    def q_x_vector(self, birth_date: int):
        """
         This function initialises the required death probability vector with trend factors in order to use it later in calculation of probability with trend factors
         :param birth_date: the birth year of the insured person
         :return: death probability vector
        """
        max_age = self.death_max_age
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

    def i_x_vector(self, birth_date: int):
        """
         This function initialises the required disability probability vector
         :param birth_date: the birth year of the insured person
         :return: disability probability vector
        """
        min_age = self.disability_min_age
        max_age = self.disability_max_age
        ix_vector = []
        for age in range(min_age, max_age + 1):
            ix = self.i_x_dict[age]
            ix_vector.append(ix)
        return ix_vector

    def one_year_disability_probability(self, age, birth_date):
        """
        This function initialises the required one year disability probability
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year disability probability
        """
        ix_vector = self.i_x_vector(birth_date=birth_date)
        ix = ix_vector[age]
        return ix

    def one_year_active_probability(self, age, birth_date):
        """
        This function initialises the required one year probability that the insured person remains active
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year active probability
        """
        result = 1 - self.one_year_disability_probability(age, birth_date=birth_date)
        return result


print(BiometryCpl(contract_nr=1234).q_x_vector(1960))
