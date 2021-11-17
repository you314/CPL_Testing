from PresentValues import Presentvalues
from Contract import ContractDTO
from FLags.Flags import Flags


class Tariff(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        self.Presentvalues = Presentvalues(contract_nr=contract_nr)
        self.Flags = Flags()
        self.flagsVector = self.Flags.flags_vector(tariff_generation=self.tg(), tariff=self.tariff())

    def NetPremiumRente(self):
        gamma =0.1
        netPremium = (1+gamma) * self.flagsVector[1] \
                     * self.Presentvalues.aeg(g=self.guarantee_time()) * \
                     self.flagsVector[2] + self.Presentvalues.aegk(g=self.guarantee_time(), k=self.m()) * \
                     self.flagsVector[3] + self.Presentvalues.n_m_a_x(Defermentperiod= self.deferment_period(), m=self.m(), age=self.actuarial_age(), birthDate=self.birth_year())
        return netPremium


print(Tariff(contract_nr=1234).NetPremiumRente())
