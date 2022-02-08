from calculationbases.biometry.cpl_bio import BiometryCpl
from calculationbases.interest.interest_rate import Interest
from input.contract import ContractDTO


class PresentValues(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        self.biometry_cpl = BiometryCpl(contract_nr=contract_nr)
        self.Interest = Interest()

    def v(self):
        i = self.Interest.interest_vector(tariff_generation=self.tg())
        V = []
        for j in range(0, len(i)):
            v = 1/(1+i[j])
            V.append(v)
        return V

    def n_p_x(self, n: int, age:int, birth_date: int):
        prob = self.biometry_cpl.n_year_survival_probability(n=n, age=age, birth_date=birth_date)
        return prob

    def aeg(self, g):
        result = 0
        for j in range(0, g):
            summand = 1
            for k in range(0, j):
                summand = summand * self.v()[k]
            result = result + summand
        return result

    def aegk(self, g, k):
        result = 0
        for j in range(0, g):
            summand = 1
            for h in range(0, j):
                summand = summand * self.v()[h]
            summand = summand * (1 - self.v()[j])/(1 - self.v()[j] ** (1/k))
            result = result + summand
        result = 1/k * result
        return result

    def n_m_a_x(self, deferment_period, m, age, birth_date):
        outer_prod = 1
        summand = 0
        outer_probability = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        for j in range(0, deferment_period):
            outer_prod = outer_prod * self.v()[j]
        for count in range(0, m):
            inner_probability = self.n_p_x(n=count, age=age + deferment_period, birth_date=birth_date)
            inner_prod = 1
            for k in range(deferment_period, deferment_period + count):
                inner_prod = inner_prod * self.v()[k]
            summand = summand + inner_prod * inner_probability
        result = outer_probability * summand
        return result

    def f(self, k: int) -> float:
        """
        Computes the surcharge for different payment frequencies
        :param k: The payment frequency
        :return: The surcharge factor
        """
        summand1 = (k - 1) / (2 * k)
        i = self.Interest.interest_vector(tariff_generation=self.tg())[0]
        factor1 = (k * k - 1) / (6 * k * k)
        factor2 = i * (1 - i / 2)
        summand2 = factor1 * factor2
        result = summand1 + summand2
        return result

    def c0_nax_k(self, deferment_period, age, birth_date, payment_contributions_frequency):
        sum = 0
        for counter in range(deferment_period, 121 - age):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0] ** deferment_period
        return sum - factor1 * factor2

    def c1_naxl_k(self, deferment_period, age, birth_date, payment_contributions_frequency, pension_payment_period):
        '''
        :param pension_payment_period: stands for 'l' in the formula
        '''
        sum = 0
        for counter in range (deferment_period, deferment_period + pension_payment_period - 1):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=deferment_period + pension_payment_period, age=deferment_period, birth_date=birth_date) * self.v()[0] ** deferment_period
        factor3 = 1 / self.n_p_x(n=deferment_period + pension_payment_period, age=age, birth_date=birth_date)
        factor4 = self.v()[0] ** pension_payment_period
        return sum - factor1 * factor2 * (factor3 - factor4)

    def c2_gax_k(self, guarantee_time, age, birth_date, payment_contributions_frequency):
        sum = 0
        for counter in range (guarantee_time, 121 - age):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=guarantee_time, age=age, birth_date=birth_date) * self.v()[0] ** guarantee_time
        return sum - factor1 * factor2

    def c3_ag_k(self, guarantee_time, payment_contributions_frequency):
        nominator = 1 - self.v()[0] ** guarantee_time
        denominator = payment_contributions_frequency * (1 - self.v()[0] ** (1 / payment_contributions_frequency))
        return nominator / denominator

    def c4_nag_k(self, age, birth_date, deferment_period, guarantee_time, payment_contributions_frequency):
        nominator = 1 - self.v()[0] ** guarantee_time
        denominator = payment_contributions_frequency * (1 - self.v()[0] ** (1 / payment_contributions_frequency))
        factor = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0] ** deferment_period
        return factor * nominator / denominator

    def c5a_axn(self, age, birth_date, deferment_period):
        sum = 0
        for counter in range(0, deferment_period - 1):
            sum = self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        return sum

    def c5b_axn(self, age, birth_date, deferment_period):
        sum = 0
        for counter in (0, deferment_period - 1):
            sum = self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        return sum


print(PresentValues(123))

# print(eg.discountFactor(2001))
# print(eg.n_p_x('male', 10, 30, 1990))
# print(eg.aeg(4,2001))
# print(eg.aegk(4,2,2001))






