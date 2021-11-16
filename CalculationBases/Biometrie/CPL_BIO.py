from math import exp
from os import path
from CPL_Prep import FileReader
from Contract import ContractDTO
from CalculationBases.Biometrie.LifeTable import LifeTable

class BiometrieCpl():

    def __init__(self, tariff_generation,contractnr):
        """
        This function intialises the required probability vectors and trend factors in order to use it later in calculation of probability with trend factors
        :param Tariffgeneration: the life table is determined according to tariff generation
        :return: probability vectors
               """


        self.LifeTable= LifeTable(Tariffgeneration=tariff_generation)
        self.contractDTO= ContractDTO()
        self.LifeTableName= self.LifeTable.LifetablecsvName
        relative_path = "/"
        csvFilename = self.LifeTableName
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        self.sex = self.contractDTO.sex(contract_nr=contractnr)
        if self.sex == "male":
            self.q_x_dict = reader.readColumnFromCSV("q_xm", type=float)
            self.trend_dict = reader.readColumnFromCSV("trend_m", type=float)
        elif self.sex == "female":
            self.q_x_dict = reader.readColumnFromCSV("q_xw", type=float)
            self.trend_dict = reader.readColumnFromCSV("trend_w", type=float)
        print(self.q_x_dict)
        self.Age = reader.readColumnFromCSV("AGE", type=float)
        self.MAX_AGE = 121




    def q_x(self, birthDate:int):
        """
         This function intialises the required death probability vector with trend factors in order to use it later in calculation of probability with trend factors
         :param birthDate: the birth year of the insured person
         :return: death probability vector
                """
        Max_Age = self.MAX_AGE
        QX= []
        for age in range(0, Max_Age + 1):
            qx= self.q_x_dict[age] * exp(-(birthDate + age - 1999) * self.trend_dict[age])
            QX.append(qx)
        return QX

    def oneYearDeathProbability(self, age, birthDate):
        """
        This function intialises the required one year death probability with taking in consideration the trend factor
        :param birthDate: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year death probability
                        """
        Vector = self.q_x(birthDate=birthDate)
        #print(Vector[51])
        qX = Vector[age]
        return qX

    def oneYearSurvivalProbability(self, age, birthDate):
        """
        This function intialises the required one year survival probability with taking in consideration the trend factor
        :param birthDate: the birth year of the insured person
        :param age: the age of the insured person
        :return: one year survival probability
                                """
        result = 1 - self.oneYearDeathProbability(age, birthDate=birthDate)
        return result

    def nYearSurvivalProbability(self, n, age, birthDate):

        """
        This function intialises the required n year death probability with taking in consideration the trend factor
        :param birthDate: the birth year of the insured person
        :param age: the age of the insured person
        :param n: the period in which the required probability is calculated
        :return: n year death probability
                                """
        Vector = self.q_x(birthDate=birthDate)
        if n <= 0:
            result = 1
        elif age >= len(Vector) - 1:
            result = 0
        else:
            result = 1
            for i in range(age, age + n):
                result*= self.oneYearSurvivalProbability(age=i, birthDate=birthDate)
        return result
