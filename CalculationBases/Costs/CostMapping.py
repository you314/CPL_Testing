from CPL_Prep import FileReader
from Contract import ContractDTO
from os import path


class CostMapping:

    def __init__(self, contract_nr):
        self.ContractDTO = ContractDTO()
        self.DefermentPeriod = self.ContractDTO.defermentperiod(Contractnr=contract_nr)
        self.TariffName = self.ContractDTO.tariff_name(Contractnr=contract_nr)
        self.isNonContributory = self.ContractDTO.is_non_contributory(Contractnr=contract_nr)
        relative_path = "/"
        csv_tariff_name_cost_mapping = "TariffName_CostMapping.csv"
        csv_tariff_name_cost_mapping_granular = "Tariff_CostMapping_granular.csv"
        file_tariff_name_cost_mapping = path.dirname(__file__) + relative_path + csv_tariff_name_cost_mapping
        file_tariff_name_cost_mapping_granular = path.dirname(__file__) + relative_path + csv_tariff_name_cost_mapping_granular
        self.reader_layer1 = FileReader(file_tariff_name_cost_mapping)
        self.reader_layer2 = FileReader(file_tariff_name_cost_mapping_granular)
        self.Mapping_dictionary1 = self.reader_layer1.create_mapping_by_key("TariffNames")
        self.Mapping_dictionary2 = self.reader_layer2.create_mapping_by_key("CostGroup")

    def acquisition_cost_group(self):
        self.CostGroup = self.Mapping_dictionary1[self.TariffName]["AcquisitionCostGroup"]
        if self.CostGroup in self.Mapping_dictionary2.keys():
            CostGroup_granular = self.Mapping_dictionary2[self.CostGroup][self.acquisition_cost_group_granular()]
            return self.CostGroup + CostGroup_granular
        else:
            return self.CostGroup

    def amortization_cost_group(self):
        return self.Mapping_dictionary1[self.TariffName]["AmortizationCostGroup"]

    def administration_cost_group(self):
        return self.Mapping_dictionary1[self.TariffName]["AdministrationCostGroup"]

    def unit_cost_group(self):
        return self.Mapping_dictionary1[self.TariffName]["UnitCostGroup"]

    def acquisition_cost_group_granular(self):
        if self.CostGroup == "AK_4":
            if self.DefermentPeriod < 55:
                return "Variant1"
            else:
                return "Variant2"
        elif self.CostGroup == "AK_8_Courtagestufe2":
            if self.DefermentPeriod <= 21:
                return "Variant1"
            elif 21 < self.DefermentPeriod <= 30:
                return "Variant2"
            else:
                return "Variant3"
        elif self.CostGroup == "AMK5":
            if self.DefermentPeriod <= 21:
                return "Variant1"
            elif 21 < self.DefermentPeriod <= 30:
                return "Variant2"
            else:
                return "Variant3"
        else:
            if self.isNonContributory == 1:
                return "Variant1"
            else:
                return "Variant2"

print("acquisition_cost_group name is: " + CostMapping(contract_nr=123).acquisition_cost_group())
#print("amortization_cost_group name is: " + CostMapping(contract_nr=124).amortization_cost_group())
#print("administration_cost_group name is: " + CostMapping(contract_nr=124).administration_cost_group())
#print("unit_cost_group name is: " + CostMapping(contract_nr=124).unit_cost_group())
