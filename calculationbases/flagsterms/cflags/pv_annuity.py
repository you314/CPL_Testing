from CPLTesting.CalculationBases.biometry.cpl_bio import BiometryCpl
from CPLTesting.CalculationBases.Interest.interest_rate import Interest
from CPLTesting.input.contract import ContractDTO


class PresentValues:

    def __init__(self, contract_nr):
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        self.biometry_cpl = BiometryCpl(contract_nr=contract_nr)
        self.Interest = Interest()


    ### general functions ###

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
        result = 0.
        for j in range(0, guarantee_time+1):
            summand = 1.
            for k in range(0, j+1):
                summand *= self.v()[k]
            result += summand
        return result


    def aegk(self, guarantee_time: int, k: int) -> float:
        result = 0.
        for j in range(0, guarantee_time+1):
            summand = 1.
            for h in range(0, j+1):
                summand *= self.v()[h]

            summand *= (1 - self.v()[j]) / (1 - self.v()[j] ** (1 / k))
            result += summand

        result *= 1 / k
        return result


    def n_m_a_x(self, deferment_period: int, m: int, age: int, birth_date: int) -> float:
        outer_prod = 1.
        for j in range(0, deferment_period):
            outer_prod *= self.v()[j]

        summand = 0.
        outer_probability = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        for count in range(0, m+1):
            inner_prod = 1.
            for k in range(deferment_period, deferment_period + count+1):
                inner_prod *= self.v()[k]

            inner_probability = self.n_p_x(n=count, age=age + deferment_period, birth_date=birth_date)
            summand += inner_prod * inner_probability

        result = outer_probability * summand
        return result


    def f(self, k: int) -> float:
        """
        Computes the surcharge for different payment frequencies
        :param k: The payment frequency
        :return: The surcharge factor
        """
        i = self.Interest.interest_vector(tariff_generation=self.contractDTO.tg())[0]
        term1 = (k - 1) / (2 * k)
        term2 = (k**2 - 1) / (6 * k**2)
        term3 = i * (1 - i / 2)
        return term1 + term2 * term3


    def correction_factor(self, payment_frequency) -> float:
        return (payment_frequency - 1)/(2*payment_frequency) + self.v()[0]*(1 - self.v()[0]/2)*(payment_frequency**2 - 1)\
               /(6*payment_frequency**2)


    ### c flags ###

    def c0_nax_k(self, deferment_period: int, age: int, birth_date: int, payment_contributions_frequency: int) -> float:
        sum = 0.
        for counter in range(deferment_period, 121-age+1):
            sum += self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter

        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0] ** deferment_period
        return sum - factor1 * factor2


    def c1_naxl_k(self, deferment_period: int, age: int, birth_date: int, payment_contributions_frequency: int,
                  pension_payment_period: int) -> float:
        sum = 0.
        for counter in range(deferment_period, deferment_period + pension_payment_period):# - 1):
            sum += self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter

        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=deferment_period + pension_payment_period, age=deferment_period, birth_date=birth_date) * \
                  self.v()[0] ** deferment_period
        factor3 = 1 / self.n_p_x(n=deferment_period + pension_payment_period, age=age, birth_date=birth_date)
        factor4 = self.v()[0] ** pension_payment_period
        return sum - factor1 * factor2 * (factor3 - factor4)


    def c2_gax_k(self, guarantee_time: int, age: int, birth_date: int, payment_contributions_frequency: int) -> float:
        sum = 0.
        for counter in range(guarantee_time, 121-age+1):
            sum = sum + self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter

        factor1 = self.f(k=payment_contributions_frequency)
        factor2 = self.n_p_x(n=guarantee_time, age=age, birth_date=birth_date) * self.v()[0] ** guarantee_time
        return sum - factor1 * factor2

    def c3_ag_k(self, guarantee_time: int, payment_contributions_frequency: int) -> float:
        nominator = 1 - self.v()[0] ** guarantee_time
        denominator = payment_contributions_frequency * (1 - self.v()[0] ** (1 / payment_contributions_frequency))
        return nominator / denominator


    def c4_nag_k(self, age: int, birth_date: int, deferment_period: int, guarantee_time: int,
                 payment_contributions_frequency: int) -> float:
        factor = self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0] ** deferment_period
        nominator = 1 - self.v()[0] ** guarantee_time
        denominator = payment_contributions_frequency * (1 - self.v()[0] ** (1 / payment_contributions_frequency))
        return factor * nominator / denominator


    def c5a_axn(self, age: int, birth_date: int, deferment_period: int) -> float:
        sum = 0.
        for counter in range(0, deferment_period):# - 1):
            sum += self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        return sum


    def c5b_axn(self, age: int, birth_date: int, deferment_period: int) -> float:
        sum = 0.
        for counter in (0, deferment_period):# - 1):
            sum += self.n_p_x(n=counter, age=age, birth_date=birth_date) * self.v()[0] ** counter
        return sum

    ### ...

    def c10_ag_12(self, guarantee_time: int) -> float:
        return (1 - self.v()[0] ** guarantee_time) / (12 - 12 * self.v()[0] ** (1/12))


    def c11_ngax_12(self, deferment_period, guarantee_time, max_age, age, birth_date) -> float:
        sum = 0.
        for k in range(deferment_period + guarantee_time, max_age - age +1):
            sum += self.n_p_x(n=k, age=age, birth_date=birth_date) * self.v()[0] ** k

        correction = self.correction_factor(payment_frequency = 12) \
                     * self.n_p_x(n=deferment_period + guarantee_time, age=age, birth_date=birth_date) \
                     * self.v()[0] ** (deferment_period + guarantee_time)
        return sum - correction


    def c12_ax_12(self, max_age, age, birth_date) -> float:
        sum = 0.
        for k in range(0, max_age - age +1):
            sum += self.n_p_x(n=k, age=age, birth_date=birth_date) * self.v()[0] ** k

        correction = self.correction_factor(payment_frequency=12)
        return sum - correction


    def c13_gax_12(self, max_age, age, birth_date, guarantee_time) -> float:
        sum = 0.
        for k in range(guarantee_time, max_age - age + 1):
            sum += self.n_p_x(n=k, age=age, birth_date=birth_date) * self.v()[0] ** k

        correction = self.correction_factor(payment_frequency=12) \
                     * self.n_p_x(n=guarantee_time, age=age, birth_date=birth_date) \
                     * self.v()[0] ** guarantee_time
        return sum - correction


    def c14_axl_k(self, age, birth_date, agreed_duration) -> float:
        sum = 0.
        for k in range(agreed_duration):
            sum += self.n_p_x(n=k, age=age, birth_date=birth_date) * self.v()[0] ** k

        correction = self.correction_factor(payment_frequency=12) \
                     * ( 1 - self.n_p_x(n=agreed_duration, age=age, birth_date=birth_date) \
                     * self.v()[0] ** agreed_duration )
        return sum - correction


    def c15_nAx(self, deferment_period, age, birth_date) -> float:
        sum = 0.
        for k in range(deferment_period):
            sum += self.n_p_x(n=k, age=age, birth_date=birth_date) \
                   * cpl_bio.one_year_death_probability(age=age+k, birth_date=birth_date) * self.v()[0] ** (k+1)
        return sum


    def c16_e0Ax_k(self, e, age, birth_date, payment_frequency) -> float:
        sum = 0.
        correction = 0.
        for j in range(e):
            p_times_q = self.n_p_x(n=j, age=age, birth_date=birth_date) \
             * cpl_bio.one_year_death_probability(age=age+j, birth_date=birth_date)

            sum += (e-j) * self.v()[0] ** (j+1) * p_times_q
            correction += self.v()[0] ** (j+1) * p_times_q

        return sum - (payment_frequency-1)/(2*payment_frequency) * correction


    def c17_enAx_k(self, e, deferment_period, age, birth_date, payment_frequency) -> float:
        sum = 0.
        correction = 0.
        for j in range(e):
            p_times_q = self.n_p_x(n=j, age=age+deferment_period, birth_date=birth_date) \
             * cpl_bio.one_year_death_probability(age=age+deferment_period+j, birth_date=birth_date)

            sum += (e-j) * self.v()[0] ** (j+1) * p_times_q
            correction += self.v()[0] ** (j+1) * p_times_q

        defer_to_n = self.v()[0] ** deferment_period * self.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        return defer_to_n * sum - (payment_frequency-1)/(2*payment_frequency) * defer_to_n * correction


    def c18_nax_aak(self, deferment_period, max_age, age, birth_date, payment_frequency) -> float:
        sum = 0.
        for j in range(max_age-deferment_period-age+1):
            sum += self.n_p_x(n=j, age=age+deferment_period, birth_date=birth_date) \
                     * cpl_bio.n_year_disability_probability(deferment_period=j, age=age+deferment_period)

        factor = self.v()[0] ** deferment_period * self.n_p_x(n=deferment_period, age=age, birth_date=birth_date) \
                * cpl_bio.n_year_disability_probability(deferment_period=deferment_period, age=age+deferment_period)
        correction = self.correction_factor(payment_frequency=payment_frequency)
        return factor * (sum - correction)