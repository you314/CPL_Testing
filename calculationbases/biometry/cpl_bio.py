from math import exp
from os import path
from helper.cpl_prep import FileReader
from calculationbases.biometry.life_table import LifeTable
from input.json_reader import JsonReader


class BiometryCpl:

    def __init__(self):
        self.contractDTO = JsonReader
        self.tariff_generation = self.contractDTO.tg()
        self.birth_year = self.contractDTO.birth_year()
        self.life_table = LifeTable()
        self.death_table_name = self.life_table.death_probability_table()
        self.disability_table_name = self.life_table.disability_probability_table()
        self.relative_path = "/"
        self.actuarial_age = self.contractDTO.actuarial_age_2()
        self.omega = 133

    def age_shifted(self) -> int:  # TODO: implement a switch to turn of the AgeShift in case trend function is used
        """
        This function amends the birth year by applying the age shift as per Tätigkeitsplan
        :return: calculatory age as int
        """
        actuarial_age = self.actuarial_age
        actual_birth_year = self.birth_year
        age_shift_csv_filename = "AgeShift.csv"
        age_shift_csv_path = path.dirname(__file__) + self.relative_path + age_shift_csv_filename
        age_shift_csv_reader = FileReader(age_shift_csv_path)
        age_shift_dict = age_shift_csv_reader.create_mapping_by_key("Birthyear")
        age_shift_for_year = age_shift_dict[str(actual_birth_year)]
        if self.contractDTO.sex() == "M":
            column_name = "A04_A_M"
        else:
            column_name = "A04_A_F"
        age_shift = int(age_shift_for_year[column_name])
        return actuarial_age + age_shift

    def modification(self) -> int:
        """
        This function calculates the shift of the table based on the tariff generation
        :return: amount of rows, the table needs to be shifted
        """
        tariff_generation = self.tariff_generation
        modification_csv_filename = "Modifikation.csv"
        modification_csv_path = path.dirname(__file__) + self.relative_path + modification_csv_filename
        modification_csv_reader = FileReader(modification_csv_path)
        modification_dict = modification_csv_reader.create_mapping_by_key("Generation")
        modification_years = modification_dict[str(tariff_generation)]
        if self.contractDTO.sex() == "M":
            column_name = "Mod_M"
        else:
            column_name = "Mod_F"
        modification_shift = int(modification_years[column_name])
        return modification_shift

    def q_x_vector(self, birth_date: int) -> list[float]:
        """
         Initialises death probability vector with trend factors
         :param birth_date: the birth year of the insured person
         :return: death probability vector
        """
        death_csv_filename = self.death_table_name
        modification = self.modification()
        death_csv_path = path.dirname(__file__) + self.relative_path + death_csv_filename
        death_csv_reader = FileReader(death_csv_path)
        death_age_dict = death_csv_reader.read_column_from_csv("AGE", type=float)
        if self.contractDTO.sex() == "M":
            q_x_dict = death_csv_reader.read_column_from_csv("q_xm", type=float)
            trend_dict = death_csv_reader.read_column_from_csv("trend_m", type=float)
        else:
            q_x_dict = death_csv_reader.read_column_from_csv("q_xw", type=float)
            trend_dict = death_csv_reader.read_column_from_csv("trend_w", type=float)
        min_age = list(death_age_dict.keys())[0]
        max_age = list(death_age_dict.keys())[-1]
        qx_vector = []
        for age in range(min_age, modification):
            qx = q_x_dict[0]
            qx_vector.append(qx)
        for age in range(min_age+modification, max_age + 1):
            qx = q_x_dict[age-modification] #* exp(-(birth_date + age - 1999) * trend_dict[age])
            qx_vector.append(qx)
        return qx_vector

    def one_year_death_probability(self, age, birth_date) -> float:
        """
        Initialises required one year death probability considering a trend factor
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year death probability
        """
        qx_vector = self.q_x_vector(birth_date=birth_date)
        qx = qx_vector[age]
        return qx

    def one_year_survival_probability(self, age, birth_date) -> float:
        """
        Initialises required one year survival probability considering a trend factor
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year survival probability
        """
        result = 1 - self.one_year_death_probability(age, birth_date=birth_date)
        return result

    def n_year_survival_probability(self, n, age, birth_date) -> float:
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

    def survival_probability_vector(self, age, birth_date) -> list[float]:
        result = 1
        nPX_vector = [result]
        qx_vector = self.q_x_vector(birth_date=birth_date)
        for k in range(age, self.omega):
            result *= (1-qx_vector[k])
            nPX_vector.append(result)
        return nPX_vector

    def i_x_vector(self) -> list[float]:
        """
         This function initialises the required disability probability vector
         :return: disability probability vector
        """
        disability_csv_filename = self.disability_table_name
        disability_csv_path = path.dirname(__file__) + self.relative_path + disability_csv_filename
        disability_csv_reader = FileReader(disability_csv_path)
        if self.contractDTO.sex() == "male":
            group_name = "Group_" + self.contractDTO.profession() + "_m"
        else:
            group_name = "Group_" + self.contractDTO.profession() + "_f"
        disability_age_dict = disability_csv_reader.read_column_from_csv("AGE", type=float)
        i_x_dict = disability_csv_reader.read_column_from_csv(group_name, type=float)
        min_age = list(disability_age_dict.keys())[0]
        max_age = list(disability_age_dict.keys())[-1]
        ix_vector = []
        for age in range(min_age, max_age + 1):
            ix = i_x_dict[age]
            ix_vector.append(ix)
        return ix_vector

    def one_year_disability_probability(self, age) -> float:
        """
        This function initialises the required one year disability probability
        :param age: the age of the insured person
        :return: one year disability probability
        """
        ix_vector = self.i_x_vector()
        ix = ix_vector[age]
        return ix

    def one_year_active_probability(self, age) -> float:
        """
        This function initialises the required one year probability that the insured person remains active
        :param age: the age of the insured person
        :return: one year active probability
        """
        result = 1 - self.one_year_disability_probability(age)
        return result
