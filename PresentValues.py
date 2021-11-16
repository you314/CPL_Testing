from CalculationBases.Biometrie.CPL_BIO import BiometrieCpl
from CalculationBases.Interest.InterestRate import Interest
from Contract import ContractDTO


class Presentvalues():

    def __init__(self,Contractnr):
        self.ContractDTO= ContractDTO(contract_nr=Contractnr)
        Tariffgeneration=self.ContractDTO.tg()
        print(Tariffgeneration)
        self.BiometrieCpl= BiometrieCpl(tariff_generation=Tariffgeneration)
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

    def n_m_a_x(self, Defermentperiod, m, age, birthDate, sex, Tariffgeneration):
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

    def F(self, k: int, Tariffgeneration: int) -> float:
        """
        Computes the surcharge for different payment frequencies
        :param k: The payment frequncy
        :param Tariffgeneration: The tariffgeneration that determines the interest rate
        :return: The surcharge factor
        """
        summand1 = (k - 1) / (2 * k)
        i = self.Interest.Interest_Vector(Tariffgeneration=Tariffgeneration)[0]
        factor1 = (k * k - 1) / (6 * k * k)
        factor2 = i * (1 - i / 2)
        summand2 = factor1 * factor2
        result = summand1 + summand2
        return result

    def c0_nax_k(self, Defermentperiod, age, birthDate, sex, Tariffgeneration, paymentContributionsFrequency):
        sum = 0
        for counter in range (Defermentperiod, 121 - age):
            sum = sum + self.n_p_x(sex = sex, n = counter, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** counter
        factor1 = self.F(k = paymentContributionsFrequency, Tariffgeneration = Tariffgeneration)
        factor2 = self.n_p_x(sex = sex, n = Defermentperiod, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** Defermentperiod
        return sum - factor1 * factor2

    def c1_naxl_k(self, Defermentperiod, age, birthDate, sex, Tariffgeneration, paymentContributionsFrequency, pensionPaymentPeriod):
        '''
        :param pensionPaymentPeriod: stands for 'l' in the formula
        '''
        sum = 0
        for counter in range (Defermentperiod, Defermentperiod + pensionPaymentPeriod - 1):
            sum = sum + self.n_p_x(sex = sex, n = counter, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** counter
        factor1 = self.F(k = paymentContributionsFrequency, Tariffgeneration = Tariffgeneration)
        factor2 = self.n_p_x(sex = sex, n = Defermentperiod + pensionPaymentPeriod, age = Defermentperiod, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** Defermentperiod
        factor3 = 1 / self.n_p_x(sex = sex, n = Defermentperiod + pensionPaymentPeriod, age = age, birthDate = birthDate)
        factor4 = self.v(Tariffgeneration = Tariffgeneration)[0] ** pensionPaymentPeriod
        return sum - factor1 * factor2 * (factor3 - factor4)

    def c2_gax_k(self, Garantietime, age, birthDate, sex, Tariffgeneration, paymentContributionsFrequency):
        sum = 0
        for counter in range (Garantietime, 121 - age):
            sum = sum + self.n_p_x(sex = sex, n = counter, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** counter
        factor1 = self.F(k = paymentContributionsFrequency, Tariffgeneration = Tariffgeneration)
        factor2 = self.n_p_x(sex = sex, n = Garantietime, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** Garantietime
        return sum - factor1 * factor2

    def c3_ag_k(self, Garantietime, Tariffgeneration, paymentContributionsFrequency):
        nominator = 1 - self.v(Tariffgeneration = Tariffgeneration)[0] ** Garantietime
        denominator = paymentContributionsFrequency * (1 - self.v(Tariffgeneration = Tariffgeneration)[0] ** (1 / paymentContributionsFrequency))
        return nominator / denominator

    def c4_nag_k(self, age, birthDate, sex, Defermentperiod, Garantietime, Tariffgeneration, paymentContributionsFrequency):
        nominator = 1 - self.v(Tariffgeneration = Tariffgeneration)[0] ** Garantietime
        denominator = paymentContributionsFrequency * (1 - self.v(Tariffgeneration = Tariffgeneration)[0] ** (1 / paymentContributionsFrequency))
        factor = self.n_p_x(sex = sex, n = Defermentperiod, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** Defermentperiod
        return factor * nominator / denominator

    def c5a_axn(self, age, birthDate, sex, Defermentperiod, Tariffgeneration):
        sum = 0
        for counter in range (0, Defermentperiod - 1):
            sum = self.n_p_x(sex = sex, n = counter, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** counter
        return sum

    def c5b_axn(self, age, birthDate, sex, Defermentperiod, Tariffgeneration):
        sum = 0
        for counter in range (0, Defermentperiod - 1):
            sum = self.n_p_x(sex = sex, n = counter, age = age, birthDate = birthDate) * self.v(Tariffgeneration = Tariffgeneration)[0] ** counter
        return sum









print(Presentvalues(123))

# print(eg.discountFactor(2001))
# print(eg.n_p_x('male', 10, 30, 1990))
# print(eg.aeg(4,2001))
# print(eg.aegk(4,2,2001))






