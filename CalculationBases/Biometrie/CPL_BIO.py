from math import exp
from os import path
from CPL_Prep import FileReader
from CalculationBases.Biometrie.LifeTable import LifeTable

class BiometrieCpl():

    def __init__(self,Tariffgeneration):


        self.LifeTable= LifeTable(Tariffgeneration=Tariffgeneration)
        self.LifeTableName= self.LifeTable.LifetablecsvName
        relative_path = "/"
        csvFilename = self.LifeTableName
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        self.Age = reader.readColumnFromCSV("AGE", type=float)
        self.q_x_m = reader.readColumnFromCSV("q_xm", type=float)
        self.q_x_w = reader.readColumnFromCSV("q_xw", type=float)
        self.trend_m = reader.readColumnFromCSV("trend_m", type=float)
        self.trend_w = reader.readColumnFromCSV("trend_w", type=float)
        self.MAX_AGE = 121




    def q_x_M(self, birthDate:int):
        Max_Age = self.MAX_AGE
        QX_M = []
        for age in range(0, Max_Age + 1):
            qx_m = self.q_x_m[age] * exp(-(birthDate + age - 1999) * self.trend_m[age])
            QX_M.append(qx_m)
        return QX_M

    def oneYearDeathProbabilityMen(self, age, birthDate):
        Vector = self.q_x_M(birthDate=birthDate)
        #print(Vector[51])
        qX = Vector[age]
        return qX

    def oneYearSurvivalProbabilityMen(self, age, birthDate):
        result = 1 - self.oneYearDeathProbabilityMen(age, birthDate=birthDate)
        return result

    def nYearSurvivalProbabilityMen(self, n, age, birthDate):
        Vector = self.q_x_M(birthDate=birthDate)
        if n <= 0:
            result = 1
        elif age >= len(Vector) - 1:
            result = 0
        else:
            result = 1
            for i in range(age, age + n):
                result*= self.oneYearSurvivalProbabilityMen(age=i, birthDate=birthDate)
        return result

    def q_x_W(self, birthDate):
        Max_Age = self.MAX_AGE
        QX_W = []
        for age in range(0, Max_Age + 1):
            qx_w = self.q_x_w[age] * exp(-(birthDate + age - 1999) * self.trend_w[age])
            QX_W.append(qx_w)
        return QX_W

    def oneYearDeathProbabilityWomen(self, age, birthDate):
        Vector = self.q_x_W(birthDate=birthDate)
        qX = Vector[age]
        return qX

    def oneYearSurvivalProbabilityWomen(self, age, birthDate):
        result = 1 - self.oneYearDeathProbabilityWomen(age, birthDate=birthDate)
        return result

    def nYearSurvivalProbabilityWomen(self, n, age, birthDate):
        Vector = self.q_x_W(birthDate=birthDate)
        if n <= 0:  # TODO: Check if this condition is correct
            result = 1
        elif age >= len(Vector) - 1:
            result = 0
        else:
            result = 1
            for i in range(age, age + n):
                result*= self.oneYearSurvivalProbabilityMen(age=i, birthDate=birthDate)
        return result



    def q_x_Women(self, BirthDate):
        Max_Age = self.MAX_AGE
        QX_W = []
        if BirthDate >= 79 & BirthDate <= 83:

            for age in range(0, Max_Age + 1):
                if age + 7 >= self.MAX_AGE:
                    qx_w = 1
                    QX_W.append(qx_w)
                else:
                    qx_w = self.q_x_w[age + 7]
                    QX_W.append(qx_w)
            return QX_W