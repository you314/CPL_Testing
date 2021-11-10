from CPL_Prep import FileReader
from Contract import ContractDTO
from os import path


class CostMapping:

    def __init__(self, contract_nr):
        self.ContractDTO = ContractDTO()
        self.TariffName = self.ContractDTO.tariff_name(Contractnr=contract_nr)
        relative_path = "/"
        csv_filename = "TariffName_CostMapping.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("TariffNames")

    def acquisition_cost_group(self):
        return self.Mapping_dictionary[self.TariffName]["AcquisitionCostGroup"]

    def amortization_cost_group(self):
        return self.Mapping_dictionary[self.TariffName]["AmortizationCostGroup"]

    def administration_cost_group(self):
        return self.Mapping_dictionary[self.TariffName]["AdministrationCostGroup"]

    def unit_cost_group(self):
        return self.Mapping_dictionary[self.TariffName]["UnitCostGroup"]


print("acquisition_cost_group name is: " + CostMapping(contract_nr=124).acquisition_cost_group())
print("amortization_cost_group name is: " + CostMapping(contract_nr=124).amortization_cost_group())
print("administration_cost_group name is: " + CostMapping(contract_nr=124).administration_cost_group())
print("unit_cost_group name is: " + CostMapping(contract_nr=124).unit_cost_group())
