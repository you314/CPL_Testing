from PresentValues import Presentvalues
from Contract import ContractDTO
from FLags.Flags import Flags


class Tariff(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        self.Presentvalues = Presentvalues(contract_nr=contract_nr)
        self.Flags = Flags()
        self.flagsVector = self.Flags.FlagsVector(Tariffgeneration=self.tg(), Tariff=self.tariff())

    def NetPremiumRente(self):
        gamma =0.1
        netPremium =(1+gamma)*self.flagsVector[1]*self.Presentvalues.aeg(g=self.garantietime()) * \
                    self.flagsVector[2] +self.Presentvalues.aegk(g=self.garantietime(),k=self.m())*\
                    self.flagsVector[3] + self.Presentvalues.n_m_a_x(Defermentperiod= self.defermentperiod(),m=self.m(),age=self.actuarial_age(),birthDate=self.birthyear(),sex=self.sex())
        return netPremium


print(Tariff(contract_nr=1234).NetPremiumRente())
