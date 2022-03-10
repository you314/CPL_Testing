import calculationbases.biometry.cpl_bio as cpl_bio
from calculationbases.interest.interest_rate import Interest
from input.json_reader import JsonReader


class PresentValues:
    """
    The PresentValues class is a summary of all flags corresponding to present values in the maxi formula framework.
    c1 - c53 are implemented with constant interest rates, whereas c54 - c91 are done with dynamic interest rates.
    We hereby copy the current status of CPL.

    There may arise performance issues due to the implementation of all basic p- & q-probabilities instead of using
    commutative values. This fact already leads to performance issues in CPL, which is compiled to C code.
    In pure Python this will lead to even greater performance issues.
    Is a one-to-one copy of CPL the best way to set up a testing tool? (note by Timon)
    """

    def __init__(self):
        self.contractDTO = JsonReader
        self.biometry_cpl = cpl_bio.BiometryCpl()
        self.Interest = Interest()
        self.omega = 133

    ### general functions ###

    def v(self) -> list[float]:
        """
        v vector, based on the interest_old vector
        :return: v vector
        """
        i = self.Interest.interest_vector(tariff_generation=self.contractDTO.tg())
        v_vector = [(1 / (1 + i[j])) for j in range(0, len(i))]
        return v_vector

    def n_p_x_V(self, age: int, birth_date: int) -> list[float]:
        """
        This function yields n year death probability
        :param birth_date: the birth year of the insured person
        :param age: the age of the insured person
        :param n: the period in which the required probability is calculated
        :return: n year death probability
        """
        return self.biometry_cpl.survival_probability_vector(age=age, birth_date=birth_date)

    def aeg(self, guarantee_time: int) -> float:
        sum = 0.
        v = self.v()
        for j in range(guarantee_time+1):
            product = 1.
            for k in range(0, j+1):
                product *= v[k]
            sum += product
        return sum

    def aegk(self, guarantee_time: int, k: int) -> float:
        sum = 0.
        v = self.v()
        for j in range(0, guarantee_time+1):
            product = 1.
            for h in range(0, j+1):
                product *= v[h]
            product *= (1 - v[j]) / (1 - v[j] ** (1 / k))
            sum += product
        return 1 / k * sum

    def n_m_a_x(self, deferment_period: int, m: int, age: int, birth_date: int) -> float:
        # what purpose does outer_product have?
        outer_product = 1.
        v = self.v()
        for j in range(0, deferment_period):
            outer_product *= v[j]
        ######################################

        outer_probability = self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        sum = 0.
        for count in range(0, m+1):
            inner_product = 1.
            for k in range(deferment_period, deferment_period + count+1):
                inner_product *= v[k]

            inner_probability = self.biometry_cpl.n_p_x(n=count, age=age + deferment_period, birth_date=birth_date)
            sum += inner_product * inner_probability

        return outer_probability * sum

    def correction_factor(self, payment_frequency: int) -> float:
        v = self.v()
        i = 1 / v[0]-1
        summand1 = (payment_frequency - 1) / (2 * payment_frequency)
        summand2 = i*(1 - i / 2)*(payment_frequency**2 - 1) / (6 * payment_frequency**2)
        return summand1 + summand2

    ### c flags ###

    def c0_nax_k(self, deferment_period: int, age: int, birth_date: int, payment_contributions_frequency: int) -> float:
        summand = 0.
        v = self.v()
        survival_vec = self.n_p_x_V(age=age+deferment_period, birth_date=birth_date)
        survival_vec1 = self.n_p_x_V(age=age, birth_date=birth_date)
        for j in range(self.omega-age-deferment_period):
            summand += v[0]**j * survival_vec[j]
        correction = self.correction_factor(payment_frequency=payment_contributions_frequency)
        factor = v[0] ** deferment_period * survival_vec1[deferment_period]
        return factor * (summand - correction)

    def c1_naxl_k(self, deferment_period: int, age: int, birth_date: int, payment_contributions_frequency: int,
                  pension_payment_period: int) -> float:
        summand = 0.
        v = self.v()
        survival_vec = self.n_p_x_V(age=age, birth_date=birth_date)
        for j in range(deferment_period, deferment_period + pension_payment_period):
            summand += v[0]**j * survival_vec[j]

        correction = self.correction_factor(payment_frequency=payment_contributions_frequency) * \
                     v[0]**deferment_period * survival_vec[deferment_period] * (1 - v[0]**pension_payment_period * \
                     self.biometry_cpl.n_p_x(n=pension_payment_period, age=age+deferment_period, birth_date=birth_date))
        return summand - correction

    def c2_gax_k(self, guarantee_time: int, age: int, birth_date: int, payment_contributions_frequency: int) -> float:
        summand = 0.
        v = self.v()
        survival_vec = self.n_p_x_V(age=age, birth_date=birth_date)
        for j in range(guarantee_time, self.omega-age+1):
            summand += v[0]**j * survival_vec[j]
        correction = self.correction_factor(payment_frequency=payment_contributions_frequency) * \
                     v[0]**guarantee_time * survival_vec[guarantee_time]
        return summand - correction

    def c3_ag_k(self, guarantee_time: int, payment_contributions_frequency: int) -> float:
        v = self.v()
        nominator = 1 - v[0]**guarantee_time
        denominator = payment_contributions_frequency * (1 - v[0]**(1 / payment_contributions_frequency))
        return nominator / denominator

    def c4_nag_k(self, age: int, birth_date: int, deferment_period: int, guarantee_time: int,
                 payment_contributions_frequency: int) -> float:
        factor = self.v()[0]**deferment_period * self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        c3_ag_k = self.c3_ag_k(guarantee_time=guarantee_time,
                               payment_contributions_frequency=payment_contributions_frequency)
        return factor * c3_ag_k

    def c5a_axn(self, age: int, birth_date: int, deferment_period: int) -> float:
        v = self.v()
        summand = 0.
        for counter in range(deferment_period):
            summand += self.biometry_cpl.n_p_x(n=counter, age=age, birth_date=birth_date) * v[0] ** counter
        return summand

    def c5b_axn(self, age: int, birth_date: int, deferment_period: int) -> float:
        v = self.v()
        summand = 0.
        for counter in range(deferment_period):
            summand += self.biometry_cpl.n_p_x(n=counter, age=age, birth_date=birth_date) * v[0] ** counter
        return summand

    def c6_ax_k(self, payment_frequency, age, birth_date) -> float:
        v = self.v()
        summand = 0.
        for j in range(self.omega - age):
            summand += self.biometry_cpl.n_p_x(n=j, age=age, birth_date=birth_date) * v[0] ** j
        correction = self.correction_factor(payment_frequency=payment_frequency)
        return summand - correction

    def c7_ngax_k(self, deferment_period, guarantee_time, payment_frequency, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        survival_vec = self.n_p_x_V(age=age+deferment_period+guarantee_time, birth_date=birth_date)
        survival_vec1 = self.n_p_x_V(age=age, birth_date=birth_date)
        for j in range(self.omega - deferment_period - guarantee_time-age):
            sum += survival_vec[j] * v[0]**j
        factor = survival_vec1[deferment_period + guarantee_time] * v[0]**(deferment_period + guarantee_time)
        correction = self.correction_factor(payment_frequency=payment_frequency) \
                     * survival_vec1[deferment_period + guarantee_time] \
                     * v[0]**(deferment_period + guarantee_time)
        return factor * sum - correction

    def c8_nax_12(self, deferment_period, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        survival_vec = self.n_p_x_V(age=age + deferment_period, birth_date=birth_date)
        survival_vec1 = self.n_p_x_V(age=age, birth_date=birth_date)
        for j in range(self.omega - age - deferment_period):
            sum += v[0] ** j * survival_vec[j]
        correction = self.correction_factor(payment_frequency=12)
        factor = v[0] ** deferment_period * survival_vec1[deferment_period]
        return factor * (sum - correction)

    def c9_nag_12(self, guarantee_time, deferment_period, age, birth_date) -> float:
        v = self.v()
        term1 = v[0] ** deferment_period * self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        fraction = (1 - v[0] ** guarantee_time) / (12 * (1 - v[0] ** (1/12)))
        return term1 * fraction

    def c10_ag_12(self, guarantee_time: int) -> float:
        v = self.v()
        return (1 - v[0] ** guarantee_time) / (12 - 12 * v[0] ** (1/12))

    def c11_ngax_12(self, deferment_period, guarantee_time, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        for k in range(deferment_period + guarantee_time, self.omega - age +1):
            sum += self.biometry_cpl.n_p_x(n=k, age=age, birth_date=birth_date) * v[0] ** k
        correction = self.correction_factor(payment_frequency = 12) \
                     * self.biometry_cpl.n_p_x(n=deferment_period + guarantee_time, age=age, birth_date=birth_date) \
                     * v[0] ** (deferment_period + guarantee_time)
        return sum - correction

    def c12_ax_12(self, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        for k in range(0, self.omega - age +1):
            sum += self.biometry_cpl.n_p_x(n=k, age=age, birth_date=birth_date) * v[0] ** k
        correction = self.correction_factor(payment_frequency=12)
        return sum - correction

    def c13_gax_12(self, age, birth_date, guarantee_time) -> float:
        sum = 0.
        v = self.v()
        for k in range(guarantee_time, self.omega - age + 1):
            sum += self.biometry_cpl.n_p_x(n=k, age=age, birth_date=birth_date) * v[0] ** k
        correction = self.correction_factor(payment_frequency=12) \
                     * self.biometry_cpl.n_p_x(n=guarantee_time, age=age, birth_date=birth_date) \
                     * v[0] ** guarantee_time
        return sum - correction

    def c14_axl_k(self, age, birth_date, agreed_duration) -> float:
        sum = 0.
        v = self.v()
        for k in range(agreed_duration):
            sum += self.biometry_cpl.n_p_x(n=k, age=age, birth_date=birth_date) * v[0] ** k
        correction = self.correction_factor(payment_frequency=12) \
                     * (1 - self.biometry_cpl.n_p_x(n=agreed_duration, age=age, birth_date=birth_date)
                     * v[0] ** agreed_duration)
        return sum - correction

    def c15_nAx(self, deferment_period, age, birth_date) -> float:
        survivalvec = self.n_p_x_V(age=age, birth_date=birth_date)
        sum = 0.
        qx = self.biometry_cpl.q_x_vector(birth_date=birth_date)
        v = self.v()
        for k in range(deferment_period):
            sum += survivalvec[k] * qx[age+k] * v[0] ** (k+1)
        return sum

    def c16_e0Ax_k(self, e, age, birth_date, payment_frequency) -> float:
        sum = 0.
        correction = 0.
        qx = self.biometry_cpl.q_x_vector(birth_date=birth_date)
        v = self.v()
        for j in range(e):
            p_times_q = self.biometry_cpl.n_p_x(n=j, age=age, birth_date=birth_date) \
                        * qx[age + j]
            sum += (e-j) * v[0] ** (j+1) * p_times_q
            correction += v[0] ** (j+1) * p_times_q
        return sum - (payment_frequency-1)/(2*payment_frequency) * correction

    def c17_enAx_k(self, e, deferment_period, age, birth_date, payment_frequency) -> float:
        sum = 0.
        correction = 0.
        qx = self.biometry_cpl.q_x_vector(birth_date=birth_date)
        v = self.v()
        for j in range(e):
            p_times_q = self.biometry_cpl.n_p_x(n=j, age=age+deferment_period, birth_date=birth_date) \
             * qx[age + deferment_period + j]
            sum += (e-j) * v[0] ** (j+1) * p_times_q
            correction += v[0] ** (j+1) * p_times_q
        defer_to_n = v[0] ** deferment_period * self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        return defer_to_n * sum - (payment_frequency-1)/(2*payment_frequency) * defer_to_n * correction

    def c18_nax_aak(self, deferment_period, max_age, age, birth_date, payment_frequency) -> float:
        sum = 0.
        for j in range(max_age-deferment_period-age+1):
            sum += self.biometry_cpl.n_p_x(n=j, age=age+deferment_period, birth_date=birth_date) \
                     * self.biometry_cpl.n_year_disability_probability(n=j, age=age+deferment_period)
        factor = self.v()[0] ** deferment_period * self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date) \
                * self.biometry_cpl.n_year_disability_probability(n=deferment_period, age=age+deferment_period)
        correction = self.correction_factor(payment_frequency=payment_frequency)
        return factor * (sum - correction)

    def c19_ax_aik(self,) -> float:
        return 0    # still needs to be implemented, was blocked

    def c20_axn_aik(self, deferment_period, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        for j in range(deferment_period):
            sum += v[0] ** j * self.biometry_cpl.n_p_x(n=j, age=age, birth_date=birth_date) \
                   * cpl_bio.n_year_disability_probability(n=j, age=age)
        return sum

    def c21_ngaxs_k(self, pension_dynamic, payment_frequency, guarantee_time, deferment_period, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        for k in range(self.omega-age-deferment_period-guarantee_time):
            sum += self.biometry_cpl.n_p_x(n=k, age=age+deferment_period+guarantee_time, birth_date=birth_date) \
                   * v[0] ** k * (1 + pension_dynamic) ** k

        term1 = (1 + pension_dynamic) ** guarantee_time * v[0] ** (deferment_period + guarantee_time) \
                * self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date)
        term2 = (1 + pension_dynamic * (1 - self.correction_factor(payment_frequency=payment_frequency)))/(1 + pension_dynamic)
        correction = self.correction_factor(payment_frequency=payment_frequency) / (1 + pension_dynamic)
        return term1 * (term2 * sum - correction)

    def c22_gaxs_k(self, payment_frequency, pension_dynamic, guarantee_time, deferment_period, max_age, age, birth_date) -> float:
        sum = 0.
        v = self.v()
        for j in range(max_age-age-guarantee_time):
            sum += self.biometry_cpl.n_p_x(n=j, age=age+guarantee_time, birth_date=birth_date) \
                   * v[0]**j * (1 + pension_dynamic)**j

        term1 = (1 + pension_dynamic)**guarantee_time * self.biometry_cpl.n_p_x(n=guarantee_time, age=age, birth_date=birth_date) \
                * v[0]**guarantee_time
        correction1 = (1 + pension_dynamic * (1 - cpl_bio.n_year_disability_probability(n=deferment_period, age=age))) \
                      / (1 + pension_dynamic)
        correction2 = self.correction_factor(payment_frequency=payment_frequency) / (1 + pension_dynamic)
        return term1 * (correction1 * sum - correction2)

    def c23_naxs_k(self, payment_frequency, pension_dynamic, deferment_period, max_age, age, birth_date) -> float:
        sum = 0.
        for j in range(max_age-age-deferment_period):
            sum += self.biometry_cpl.n_p_x(n=j, age=age+deferment_period, birth_date=birth_date) \
                   * self.v()[0]**j * (1 + pension_dynamic)**j

        term1 = self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0]**deferment_period
        correction1 = (1 + pension_dynamic * (1 - self.correction_factor(payment_frequency=payment_frequency))) \
                      / (1 + pension_dynamic)
        correction2 = self.correction_factor(payment_frequency=payment_frequency) / (1 + pension_dynamic)
        return term1 * (correction1 * sum - correction2)

    def c24_nags_k(self, pension_dynamic, guarantee_time, deferment_period, payment_frequency, age, birth_date, interest_rate) -> float:
        term1 = self.biometry_cpl.n_p_x(n=deferment_period, age=age, birth_date=birth_date) * self.v()[0]**deferment_period \
                * 1/payment_frequency * (1 - self.v()[0]) / (1 - self.v()[0]**(1/payment_frequency))
        term2 = (1 - (self.v()[0] * (1+pension_dynamic))**guarantee_time) / (1 - self.v()[0]**(1+pension_dynamic))
        if pension_dynamic != interest_rate:
            pv = term1 + term2
        else:
            pv = term1 + guarantee_time
        return pv

    def c25_ags_k(self, pension_dynamic, guarantee_time, payment_frequency, interest_rate) -> float:
        term1 = 1/payment_frequency * (1 - self.v()[0]) / (1 - self.v()[0]**(1/payment_frequency))
        term2 = (1 - (self.v()[0] * (1+pension_dynamic))**guarantee_time) / (1 - self.v()[0]*(1+pension_dynamic))
        interest_rate = self.Interest.interest_vector(tariff_generation=self.contractDTO.tg())[0]
        pv = 0.
        if pension_dynamic != interest_rate:
            pv = term1 + term2
        else:
            pv = term1 + guarantee_time
        return pv

    def c26_axs_k(self, payment_frequency, pension_dynamic, max_age, age, birth_date) -> float:
        sum = 0.
        for j in range(max_age-age):
            sum += self.biometry_cpl.n_p_x(n=j, age=age, birth_date=birth_date) * self.v()[0]**j * (1+pension_dynamic)**j

        correction1 = (1 + pension_dynamic * (1 - self.correction_factor(payment_frequency=payment_frequency))) / (1+pension_dynamic)
        correction2 = self.correction_factor(payment_frequency=payment_frequency) / (1+pension_dynamic)
        return correction1 * sum - correction2

    def c27_tpxtpyv_t(self, payment_duration, age_male, age_female, birth_date, sex_male, sex_female) -> float:
        product = 1.
        for j in range(payment_duration):
            product *= self.v()[j]

        term1 = self.biometry_cpl.n_p_x(n=payment_duration, age=age_male, birth_date=birth_date, sex=sex_male) \
                * self.biometry_cpl.n_p_x(n=payment_duration, age=age_female, birth_date=birth_date, sex=sex_female)
        return term1 * product

    def c38a(self, payment_duration, age, birth_date):
        probabilityvec= self.n_p_x_V(age=age, birth_date=birth_date)
        term = 0
        for j in range(payment_duration):
            term += probabilityvec[j] * self.v()[0]**j
        return term

    def c38b(self, payment_duration, age, birth_date):
        term1 = 0
        for j in range(payment_duration-1):
            term1 = term1 + (self.biometry_cpl.n_p_x(n=payment_duration, age=age, birth_date=birth_date) * self.v()[j])**j
        return term1

    def c44(self, payment_duration, age, birth_date, deferment_period):
        survivalvec = self.n_p_x_V(age=age+payment_duration, birth_date=birth_date)
        survivalvec1 = self.n_p_x_V(age=age, birth_date=birth_date)
        term1 = 0
        for j in range(deferment_period-payment_duration-1):
            term1 += survivalvec[j] * self.v()[j+payment_duration]
        factor = survivalvec1[payment_duration] * self.v()[payment_duration]
        return factor*term1

    def c51(self, deferment_period, age, birth_date):
        survivalvec = self.n_p_x_V(age=age, birth_date=birth_date)
        sum = 0.
        v = self.v()
        qx = self.biometry_cpl.q_x_vector(birth_date=birth_date)
        for k in range(deferment_period):
            sum += (k+1) * survivalvec[k] * qx[age+k] * v[0] ** (k+1)
        return sum
