from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class UnitCost:

    def __init__(self, contract_nr):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        relative_path = "/"
        csv_filename = "UnitCostRates.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("UnitCostGroups")
        self.CostGroup = CostMapping(contract_nr=contract_nr).unit_cost_group()

    def get_unit_cost_by_name(self, cost_type):
        value = self.Mapping_dictionary[self.CostGroup][cost_type]
        return float(value)


print("kappa cost is: " + str(UnitCost(contract_nr=124).get_unit_cost_by_name("kappa")) + "€")
print("beta_SP cost rate is: " + str(UnitCost(contract_nr=124).get_unit_cost_by_name("kappa_SP")) + "€")
