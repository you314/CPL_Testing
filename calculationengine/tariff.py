from CPLTesting.CalculationBases.flagsterms.cflags.pv_annuity import PresentValues
from CPLTesting.input.contract import ContractDTO
from CPLTesting.CalculationBases.flagsterms.mf_annuity_flags import Flags


class Tariff(ContractDTO):

    def __init__(self, contract_nr: int):  # ToDo Evaluate if inheritance is the right approach here
        super().__init__(contract_nr=contract_nr)
        self.present_values = PresentValues(contract_nr=contract_nr)
        self.flags = Flags()
        self.flags_vector = self.flags.Gross_Premium_flags_vector(tariff= ContractDTO.tariff(self))


    def single_gross_premium_annuity(self) -> float:
        """
        Maxi Formula for the gross single premium annuity
        """
        gamma = 0.1
        ### maxi formula needs yet to be adjusted ###
        single_gross_premuium_annuity = (1+gamma) * self.flags_vector[1] * self.present_values.aeg(guarantee_time=self.guarantee_time()) * \
            self.flags_vector[2] + self.present_values.aegk(guarantee_time=self.guarantee_time(), k=self.m()) * \
            self.flags_vector[3] + self.present_values.n_m_a_x(deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(), birth_date=self.birth_year())

        return single_gross_premuium_annuity


    def annual_gross_premium_annuity(self) -> float:
        """
        Maxi Formula for the gross annual premium annuity
        """
        gamma = 0.1
        ### maxi formula needs yet to be adjusted ###
        annual_gross_premuium_annuity = (1+gamma) * self.flags_vector[1] * self.present_values.aeg(guarantee_time=self.guarantee_time()) * \
            self.flags_vector[2] + self.present_values.aegk(guarantee_time=self.guarantee_time(), k=self.m()) * \
            self.flags_vector[3] + self.present_values.n_m_a_x(deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(), birth_date=self.birth_year())

        return annual_gross_premuium_annuity


    def single_netto_premium_annuity(self) -> float:
        """
        Maxi Formula for the netto single premium annuity
        """
        gamma = 0.1
        ### maxi formula needs yet to be adjusted ###
        single_netto_premuium_annuity = (1 + gamma) * self.flags_vector[1] * self.present_values.aeg(
            guarantee_time=self.guarantee_time()) * \
                                        self.flags_vector[2] + self.present_values.aegk(
            guarantee_time=self.guarantee_time(), k=self.m()) * \
                                        self.flags_vector[3] + self.present_values.n_m_a_x(
            deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(),
            birth_date=self.birth_year())

        return single_netto_premuium_annuity


    def annual_netto_premium_annuity(self) -> float:
        """
        Maxi Formula for the netto annual premium annuity
        """
        gamma = 0.1
        ### maxi formula needs yet to be adjusted ###
        annual_netto_premuium_annuity = (1 + gamma) * self.flags_vector[1] * self.present_values.aeg(
            guarantee_time=self.guarantee_time()) * \
                                        self.flags_vector[2] + self.present_values.aegk(
            guarantee_time=self.guarantee_time(), k=self.m()) * \
                                        self.flags_vector[3] + self.present_values.n_m_a_x(
            deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(),
            birth_date=self.birth_year())

        return annual_netto_premuium_annuity


    def reserves_annuity(self, reserve_type='a') -> float:
        """
        Maxi Formula for the capital reserves a, b & c (reserve_type argument)
        """
        gamma = 0.1
        reserves_annuity = 0.
        if reserve_type == 'a':
            ### maxi formula needs yet to be adjusted ###
            reserves_annuity = (1 + gamma) * self.flags_vector[1] * self.present_values.aeg(
                guarantee_time=self.guarantee_time()) * \
                                            self.flags_vector[2] + self.present_values.aegk(
                guarantee_time=self.guarantee_time(), k=self.m()) * \
                                            self.flags_vector[3] + self.present_values.n_m_a_x(
                deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(),
                birth_date=self.birth_year())

        elif reserve_type == 'b':
            ### maxi formula needs yet to be adjusted ###
            reserves_annuity = (1 + gamma) * self.flags_vector[1] * self.present_values.aeg(
                guarantee_time=self.guarantee_time()) * \
                               self.flags_vector[2] + self.present_values.aegk(
                guarantee_time=self.guarantee_time(), k=self.m()) * \
                               self.flags_vector[3] + self.present_values.n_m_a_x(
                deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(),
                birth_date=self.birth_year())

        elif reserve_type == 'c':
            ### maxi formula needs yet to be adjusted ###
            reserves_annuity = (1 + gamma) * self.flags_vector[1] * self.present_values.aeg(
                guarantee_time=self.guarantee_time()) * \
                               self.flags_vector[2] + self.present_values.aegk(
                guarantee_time=self.guarantee_time(), k=self.m()) * \
                               self.flags_vector[3] + self.present_values.n_m_a_x(
                deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(),
                birth_date=self.birth_year())

        return reserves_annuity

print("NetPremium for example tariff: " + str(Tariff(contract_nr=123).Single_Gross_premium_annuity()) + " (Desired value: 21.51667818974244)")
