from calculationbases.flagsterms.cflags.pv_annuity import PresentValues
from input.json_reader import JsonReader
from input.contract import ContractDTO
from calculationbases.flagsterms.mf_annuity_flags import Flags


class Tariff():
    def __init__(self):  # , contract_nr: int):  # ToDo Evaluate if inheritance is the right approach here
        #super().__init__()  # contract_nr=contract_nr)
        self.present_values = PresentValues()  # contract_nr=contract_nr)
        self.flags = Flags()
        self.contract_Dto= JsonReader
        # self.flags_vector = self.flags.Gross_Premium_flags_vector(tariff= ContractDTO.tariff(self))
        self.flags_vector_J = self.flags.Gross_Premium_flags_vector(tariff=self.contract_Dto.tariff_name())

    def Single_Gross_premium_annuity(self) -> float:
        """
        Maxi Formula for the gross single premium
        :return: gross single premium
        """
        gamma = 0.1
        GP = (1+gamma) * self.flags_vector_J[1] * self.present_values.aeg(guarantee_time=self.contract_Dto.guarantee_time()) * \
            self.flags_vector_J[2] + self.present_values.aegk(guarantee_time=self.contract_Dto.guarantee_time(), k=self.contract_Dto.m()) * \
            self.flags_vector_J[3] + self.present_values.n_m_a_x(deferment_period=self.contract_Dto.deferment_period(), m=self.contract_Dto.m(), age=self.contract_Dto.actuarial_age(), birth_date=self.contract_Dto.birth_year())
        return GP


print("NetPremium for example tariff: " + str(Tariff().Single_Gross_premium_annuity()) + " (Desired value: 0.015481519377881664 )")
