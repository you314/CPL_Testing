from PresentValues import PresentValues
from Contract import ContractDTO
from FLags.Flags import Flags


class Tariff(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        self.Presentvalues = PresentValues(contract_nr=contract_nr)
        self.Flags = Flags()
        self.flagsVector = self.Flags.flags_vector(tariff_generation=self.tg(), tariff=self.tariff())

    def NetPremiumRente(self):
        gamma =0.1
        netPremium = (1+gamma) * self.flagsVector[1] \
                     * self.Presentvalues.aeg(g=self.guarantee_time()) * \
                     self.flagsVector[2] + self.Presentvalues.aegk(g=self.guarantee_time(), k=self.m()) * \
                     self.flagsVector[3] + self.Presentvalues.n_m_a_x(deferment_period= self.deferment_period(), m=self.m(), age=self.actuarial_age(), birth_date=self.birth_year())
        return netPremium


print(Tariff(contract_nr=1234).NetPremiumRente())
