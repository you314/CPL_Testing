from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class AdministrationRate:

    def __init__(self, contract_nr):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        relative_path = "/"
        csv_filename = "AdministrationCostRates.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("AdministrationCostGroups")
        self.CostGroup = CostMapping(contract_nr=contract_nr).administration_cost_group()

    def get_admin_cost_by_name(self, cost_type):
        value = self.Mapping_dictionary[self.CostGroup][cost_type]
        return float(value)


print("beta cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("beta")*100) + "%")
print("beta_SP cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("beta_SP")*100) + "%")
print("gamma_11 cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("gamma_11")*100) + "%")
print("gamma_12 cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("gamma_12")*100) + "%")
print("gamma_1 cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("gamma_1")*100) + "%")
print("gamma_2 cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("gamma_2")*100) + "%")
print("gamma_3 cost rate is: " + str(AdministrationRate(contract_nr=124).get_admin_cost_by_name("gamma_3")*100) + "%")
