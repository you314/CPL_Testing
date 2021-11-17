from PresentValues import Presentvalues
from Contract import ContractDTO
from Tariff import Tariff


class PremiumDecomposition(ContractDTO):

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        self.tariff = Tariff(Contractnr=contract_nr)
        self.present_values = Presentvalues(Contractnr=contract_nr)
        self.m = self.m(Contractnr=contract_nr)
        self.tariff_generation = self.Tg(Contractnr=contract_nr)
        self.deferment_period = self.defermentperiod(Contractnr=contract_nr)
        self.v = self.present_values.v(Tariffgeneration=self.tariff_generation)[self.m]

    def savings_premium(self):
        pr_x_1 = self.tariff.prospective_reserves(delta_m=0)
        pr_x_2 = self.tariff.prospective_reserves(delta_m=1)
        return self.v * pr_x_2 - pr_x_1

    def risk_premium(self):
        return 0

    def cost_premium(self):
        return 0

    def surcharges(self):
        return 0


print(PremiumDecomposition(contract_nr=123).savings_premium())
