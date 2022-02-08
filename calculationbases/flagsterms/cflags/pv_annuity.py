from calculationbases.biometry.cpl_bio import BiometryCpl
from calculationbases.interest.interest_rate import Interest
from input.contract import ContractDTO


class PresentValues:

    def __init__(self, contract_nr):
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        self.biometry_cpl = BiometryCpl(contract_nr=contract_nr)
        self.Interest = Interest()

    def v(self) -> list[float]:
        """
        v vector, based on the interest_old vector
        :return: v vector
        """
        i = self.Interest.interest_vector(tariff_generation=self.contractDTO.tg())
        v_vector = []
        for j in range(0, len(i)):
            v = 1 / (1 + i[j])
            v_vector.append(v)
        return v_vector

    def n_p_x(self, n: int, age: int, birth_date: int) -> float:
        """
        This function yields n year death probability
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :param n: the period in which the required probability is calculated
        :return: n year death probability
        """
        prob = self.biometry_cpl.n_year_survival_probability(n=n, age=age, birth_date=birth_date)
        return prob

    def aeg(self, guarantee_time: int) -> float:
        """

        :param guarantee_time:
        :return:
        """
        result = 0
        for j in range(0, guarantee_time):
            summand = 1
            for k in range(0, j):
                summand = summand * self.v()[k]
            result = result + summand
        return result

    def aegk(self, guarantee_time: int, k: int) -> float:
        """

        :param guarantee_time:
        :param k:
        :return:
        """
        result = 0
        for j in range(0, guarantee_time):
            summand = 1
            for h in range(0, j):
                summand = summand * self.v()[h]
            summand = summand * (1 - self.v()[j]) / (1 - self.v()[j] ** (1 / k))
            result = result + summand
        result = 1 / k * result
        return result

    def n_m_a_x(self, deferment_period: int, m: int, age: int, birth_date: int) -> float:
        """

        :param deferment_period:
        :param m:
        :param age:
        :param birth_date:
        :return:
        """
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
        i = self.Interest.interest_vector(tariff_generation=self.contractDTO.tg())[0]
        factor1 = (k * k - 1) / (6 * k * k)
        factor2 = i * (1 - i / 2)
        summand2 = factor1 * factor2
        result = summand1 + summand2
        return result

    def c0_nax_k(self, deferment_period: int, age: int, birth_date: int, payment_contributions_frequency: int) -> float:
        """

        :param deferment_period:
        :param age:
        :param birth_date:
        :param payment_contributions_frequency:
        :return:
        """
        sum = 0
        for counter in range(deferment_period, 121 - age):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0] ** deferment_period
        return sum - factor1 * factor2

    def c1_naxl_k(self, deferment_period: int, age: int, birth_date: int, payment_contributions_frequency: int,
                  pension_payment_period: int) -> float:
        """

        :param deferment_period:
        :param age:
        :param birth_date:
        :param payment_contributions_frequency:
        :param pension_payment_period: stands for 'l' in the formula
        :return:
        """
        sum = 0
        for counter in range(deferment_period, deferment_period + pension_payment_period - 1):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=deferment_period + pension_payment_period, age=deferment_period, birth_date=birth_date) * \
                  self.v()[0] ** deferment_period
        factor3 = 1 / self.n_p_x(n=deferment_period + pension_payment_period, age=age, birth_date=birth_date)
        factor4 = self.v()[0] ** pension_payment_period
        return sum - factor1 * factor2 * (factor3 - factor4)

    def c2_gax_k(self, guarantee_time: int, age: int, birth_date: int, payment_contributions_frequency: int) -> float:
        """

        :param guarantee_time:
        :param age:
        :param birth_date:
        :param payment_contributions_frequency:
        :return:
        """
        sum = 0
        for counter in range(guarantee_time, 121 - age):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=guarantee_time, age=age, birth_date=birth_date) * self.v()[0] ** guarantee_time
        return sum - factor1 * factor2

    def c3_ag_k(self, guarantee_time: int, payment_contributions_frequency: int) -> float:
        """

        :param guarantee_time:
        :param payment_contributions_frequency:
        :return:
        """
        nominator = 1 - self.v()[0] ** guarantee_time
        denominator = payment_contributions_frequency * (1 - self.v()[0] ** (1 / payment_contributions_frequency))
        return nominator / denominator

    def c4_nag_k(self, age: int, birth_date: int, deferment_period: int, guarantee_time: int,
                 payment_contributions_frequency: int) -> float:
        """

        :param age:
        :param birth_date:
        :param deferment_period:
        :param guarantee_time:
        :param payment_contributions_frequency:
        :return:
        """
        nominator = 1 - self.v()[0] ** guarantee_time
        denominator = payment_contributions_frequency * (1 - self.v()[0] ** (1 / payment_contributions_frequency))
        factor = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0] ** deferment_period
        return factor * nominator / denominator

    def c5a_axn(self, age: int, birth_date: int, deferment_period: int) -> float:
        """

        :param age:
        :param birth_date:
        :param deferment_period:
        :return:
        """
        sum = 0
        for counter in range(0, deferment_period - 1):
            sum = self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        return sum

    def c5b_axn(self, age: int, birth_date: int, deferment_period: int) -> float:
        """

        :param age:
        :param birth_date:
        :param deferment_period:
        :return:
        """
        sum = 0
        for counter in (0, deferment_period - 1):
            sum = self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        return sum
