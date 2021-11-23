from PresentValues import PresentValues
from Contract import ContractDTO
from FLags.Flags import Flags


class Tariff(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        self.present_values = PresentValues(contract_nr=contract_nr)
        self.flags = Flags()
        self.flags_vector = self.flags.flags_vector(tariff_generation=self.tg(), tariff=self.tariff())

    def net_premium_annuity(self):
        gamma = 0.1
        net_premium = (1+gamma) * self.flags_vector[1] * self.present_values.aeg(g=self.guarantee_time()) * \
            self.flags_vector[2] + self.present_values.aegk(g=self.guarantee_time(), k=self.m()) * \
            self.flags_vector[3] + self.present_values.n_m_a_x(deferment_period=self.deferment_period(), m=self.m(), age=self.actuarial_age(), birth_date=self.birth_year())
        return net_premium


print(Tariff(contract_nr=1234).net_premium_annuity())
