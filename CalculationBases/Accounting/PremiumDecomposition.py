from PresentValues import Presentvalues
from Contract import ContractDTO
from Tariff import Tariff

class PremiumDecomposition():

    def __init__(self, contract_nr):
        self.ContractDTO = ContractDTO()
        self.Tariff = Tariff(Contractnr=contract_nr)
        self.Presentvalues = Presentvalues(Contractnr=contract_nr)
        self.m = self.ContractDTO.m(Contractnr=contract_nr)
        self.tariffgeneration = self.ContractDTO.Tg(Contractnr=contract_nr)
        self.defermentperiod = self.ContractDTO.defermentperiod(Contractnr=contract_nr)
        self.v = self.Presentvalues.v(Tariffgeneration=self.tariffgeneration)[self.m]

    def savings_premium(self):
        pr_x_1 = self.Tariff.prospective_reserves(delta_m=0)
        pr_x_2 = self.Tariff.prospective_reserves(delta_m=1)
        return self.v * pr_x_2 - pr_x_1

    def risk_premium(self):
        return 0

    def cost_premium(self):
        return 0

    def surcharges(self):
        return 0



print(PremiumDecomposition(contract_nr=123).savings_premium())