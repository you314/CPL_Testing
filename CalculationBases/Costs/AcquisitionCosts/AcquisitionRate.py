from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class AcquisitionRate:

    def __init__(self, contract_nr):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        relative_path = "/"
        csv_filename = "AcquisitionCostRates.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("AcquisitionCostGroups")
        self.CostGroup = CostMapping(contract_nr=contract_nr).acquisition_cost_group()

    def alpha_z(self):
        value = self.Mapping_dictionary[self.CostGroup]["alpha_z"]
        return float(value)

    def alpha(self):
        value = self.Mapping_dictionary[self.CostGroup]["alpha"]
        return float(value)

    def alpha_1(self):
        value = self.Mapping_dictionary[self.CostGroup]["alpha_1"]
        return float(value)

    def alpha_2(self):
        value = self.Mapping_dictionary[self.CostGroup]["alpha_2"]
        return float(value)

    def alpha_3(self):
        value = self.Mapping_dictionary[self.CostGroup]["alpha_3"]
        return float(value)

    def get_acqui_cost_by_name(self, cost_type):
        value = self.Mapping_dictionary[self.CostGroup][cost_type]
        return float(value)


print("Alpha_z rate is: " + str(AcquisitionRate(contract_nr=124).get_acqui_cost_by_name("alpha_z")*100) + "%")
print("Alpha rate is: " + str(AcquisitionRate(contract_nr=124).get_acqui_cost_by_name("alpha")*100) + "%")
print("Alpha_1 rate is: " + str(AcquisitionRate(contract_nr=124).get_acqui_cost_by_name("alpha_1")*100) + "%")
print("Alpha_2 rate is: " + str(AcquisitionRate(contract_nr=124).get_acqui_cost_by_name("alpha_2")*100) + "%")
print("Alpha_3 rate is: " + str(AcquisitionRate(contract_nr=124).get_acqui_cost_by_name("alpha_3")*100) + "%")
