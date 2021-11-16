from CPL_Prep import FileReader
from Contract import ContractDTO
from os import path


class CostMapping(ContractDTO):
    """
    A class used to provide a tariff name cost group mapping. Its methods rely on two csvs.
    TariffName_CostMapping.csv links the cost groups to the contract based on the tariff's name.
    Tariff_CostMapping_granular.csv adds a suffix to the cost group based on contract specific parameters.
    """

    def __init__(self, contract_nr):
        super().__init__(contract_nr=contract_nr)
        relative_path = "/"
        csv_cost_mapping = "TariffName_CostMapping.csv"
        csv_cost_mapping_granular = "Tariff_CostMapping_granular.csv"
        file_tariff_name_cost_mapping = path.dirname(__file__) + relative_path + csv_cost_mapping
        file_tariff_name_cost_mapping_granular = path.dirname(__file__) + relative_path + csv_cost_mapping_granular
        self.reader_layer1 = FileReader(file_tariff_name_cost_mapping)
        self.reader_layer2 = FileReader(file_tariff_name_cost_mapping_granular)
        self.Mapping_dictionary1 = self.reader_layer1.create_mapping_by_key("TariffNames")
        self.Mapping_dictionary2 = self.reader_layer2.create_mapping_by_key("CostGroup")

    def acquisition_cost_group(self):
        self.CostGroup = self.Mapping_dictionary1[self.tariff_name()]["AcquisitionCostGroup"]
        if self.CostGroup in self.Mapping_dictionary2.keys():
            CostGroup_granular = self.Mapping_dictionary2[self.CostGroup][self.acquisition_cost_group_granular()]
            return self.CostGroup + CostGroup_granular
        else:
            return self.CostGroup

    def acquisition_cost_group_granular(self):
        if self.CostGroup == "AK_4":
            if self.defermentperiod() < 55:
                return "Variant1"
            else:
                return "Variant2"
        elif self.CostGroup == "AK_8_Courtagestufe2":
            if self.defermentperiod() <= 21:
                return "Variant1"
            elif 21 < self.defermentperiod() <= 30:
                return "Variant2"
            else:
                return "Variant3"

    def amortization_cost_group(self):
        self.CostGroup = self.Mapping_dictionary1[self.tariff_name()]["AmortizationCostGroup"]
        if self.CostGroup in self.Mapping_dictionary2.keys():
            CostGroup_granular = self.Mapping_dictionary2[self.CostGroup][self.amortization_cost_group_granular()]
            return self.CostGroup + CostGroup_granular
        else:
            return self.CostGroup

    def amortization_cost_group_granular(self):
        if self.CostGroup == "AMK5":
            if self.defermentperiod() <= 21:
                return "Variant1"
            elif 21 < self.defermentperiod() <= 30:
                return "Variant2"
            else:
                return "Variant3"

    def administration_cost_group(self):
        self.CostGroup = self.Mapping_dictionary1[self.tariff_name()]["AdministrationCostGroup"]
        if self.CostGroup in self.Mapping_dictionary2.keys():
            CostGroup_granular = self.Mapping_dictionary2[self.CostGroup][self.administration_cost_group_granular()]
            return self.CostGroup + CostGroup_granular
        else:
            return self.CostGroup

    def administration_cost_group_granular(self):
        if self.CostGroup == "LVK11":
            if self.is_non_contributory() == 1:
                return "Variant1"
            else:
                return "Variant2"

    def unit_cost_group(self):
        return self.Mapping_dictionary1[self.tariff_name()]["UnitCostGroup"]


print("acquisition_cost_group name is: " + CostMapping(contract_nr=123).acquisition_cost_group())
print("amortization_cost_group name is: " + CostMapping(contract_nr=123).amortization_cost_group())
print("administration_cost_group name is: " + CostMapping(contract_nr=123).administration_cost_group())
print("unit_cost_group name is: " + CostMapping(contract_nr=123).unit_cost_group())
