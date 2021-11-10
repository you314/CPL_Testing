from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class AmortizationRate:

    def __init__(self, contract_nr): #ToDo: Logic for CostGroups needs to be included, or be part of the IntegrationLayer
        relative_path = "/"
        csv_filename = "AmortizationCostRates.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("AmortizationCostGroups")
        self.CostGroup = CostMapping(contract_nr=contract_nr).amortization_cost_group()

    def get_alpha_gamma_beta_by_name(self, cost_type):
        value = self.Mapping_dictionary[self.CostGroup][cost_type]
        return float(value)


print("Alpha_gamma cost rate is: " + str(AmortizationRate(contract_nr=124).get_alpha_gamma_beta_by_name("alpha_gamma")*100) + "%")
print("Alpha_beta cost rate is: " + str(AmortizationRate(contract_nr=124).get_alpha_gamma_beta_by_name("alpha_beta")*100) + "%")
