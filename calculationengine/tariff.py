from CPLTesting.CalculationBases.flagsterms.cflags.pv_annuity import PresentValues
from CPLTesting.input.contract import ContractDTO
from CPLTesting.CalculationBases.flagsterms.mf_annuity_flags import Flags


class Tariff(ContractDTO):

    def __init__(self, contract_nr: int):  # ToDo Evaluate if inheritance is the right approach here
        super().__init__(contract_nr=contract_nr)
        self.present_values = PresentValues(contract_nr=contract_nr)
        self.flags = Flags()
        self.flags_vector = self.flags.Gross_Premium_flags_vector(tariff= ContractDTO.tariff(self))


    def Single_Gross_premium_annuity(self) -> float:
        """
        Maxi Formula for the gross single premium
        :return: gross single premium
        """
        gamma = 0.1
        GP = (1+gamma) * self.flags_vector[1] * self.present_values.aeg(guarantee_time=self.guarantee_time()) * \
            self.flags_vector[2] + self.present_values.aegk(guarantee_time=self.guarantee_time(), k=self.m()) * \
            self.flags_vector[3] + self.present_values.n_m_a_x(deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(), birth_date=self.birth_year())
        return GP


print("NetPremium for example tariff: " + str(Tariff(contract_nr=123).Single_Gross_premium_annuity()) + " (Desired value: 21.51667818974244)")
