from CalculationBases.Biometrie.CPL_BIO import BiometrieCpl
from CalculationBases.Interest.InterestRate import Interest
from Contract import ContractDTO


class Presentvalues():

    def __init__(self,Contractnr):
        self.ContractDTO= ContractDTO()
        Tariffgeneration=self.ContractDTO.Tg(Contractnr=Contractnr)
        self.BiometrieCpl= BiometrieCpl(Tariffgeneration=Tariffgeneration)
        self.Interest= Interest()

    def v(self,Tariffgeneration):
        i= self.Interest.Interest_Vector(Tariffgeneration=Tariffgeneration)
        V=[]
        for j in range(0,len(i)):
            v= 1/(1+i[j])
            V.append(v)
        return V



    def n_p_x(self, sex: str, n: int, age:int, birthDate: int):
        if sex == "female":
            prob = self.BiometrieCpl.nYearSurvivalProbabilityWomen(n=n, age=age, birthDate=birthDate)
        else:
            prob = self.BiometrieCpl.nYearSurvivalProbabilityMen(n=n, age=age, birthDate=birthDate)
        return prob


    def aeg(self, g,Tariffgeneration):
        result = 0
        for j in range(0, g):
            summand = 1
            for k in range(0, j):
                summand = summand * self.v(Tariffgeneration=Tariffgeneration)[k]
            result = result + summand

        return result

    def aegk(self, g, k,Tariffgeneration):
        result = 0
        for j in range(0, g):
            summand = 1
            for h in range(0, j):
                summand = summand * self.v(Tariffgeneration=Tariffgeneration)[h]
            summand = summand * (1 - self.v(Tariffgeneration=Tariffgeneration)[j])/(1 - self.v(Tariffgeneration=Tariffgeneration)[j] ** (1/k))
            result = result + summand
        result = 1/k * result

        return result

    def n_m_a_x(self, Defermentperiod, m, age, birthDate, sex,Tariffgeneration):
        outerProd = 1
        summand = 0
        if sex == "male":
            outerProbability = self.n_p_x(sex="male", n=Defermentperiod, age=age, birthDate=birthDate)
            for j in range(0, Defermentperiod):
                outerProd = outerProd * self.v(Tariffgeneration=Tariffgeneration)[j]
            for count in range(0, m):
                innerProbability = self.n_p_x(sex="male", n=count, age=age + Defermentperiod, birthDate=birthDate)
                innerProd = 1
                for k in range(Defermentperiod, Defermentperiod + count):
                    innerProd = innerProd * self.v(Tariffgeneration=Tariffgeneration)[k]
                summand = summand + innerProd * innerProbability
            result = outerProbability * summand
            return result



eg = Presentvalues(123)
# print(eg.discountFactor(2001))
# print(eg.n_p_x('male', 10, 30, 1990))
# print(eg.aeg(4,2001))
# print(eg.aegk(4,2,2001))






