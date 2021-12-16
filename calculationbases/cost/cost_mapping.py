from helper.cpl_prep import FileReader
from input.contract import ContractDTO
from os import path


class CostMapping:
    """
    A class used to provide a tariff name cost group mapping. Its methods rely on two csvs.
    TariffName_CostMapping.csv links the cost groups to the contract based on the tariff's name.
    Tariff_CostMapping_granular.csv adds a suffix to the cost group based on contract specific parameters.
    """

    def __init__(self, contract_nr):
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        relative_path = "/"
        csv_filename = "TariffName_CostMapping.csv"
        csv_filename_granular = "Tariff_CostMapping_granular.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_path_granular = path.dirname(__file__) + relative_path + csv_filename_granular
        reader = FileReader(csv_path)
        reader_granular = FileReader(csv_path_granular)
        self.mapping_dictionary = reader.create_mapping_by_key("TariffNames")
        self.mapping_dictionary_granular = reader_granular.create_mapping_by_key("CostGroup")
        self.acqui_cost_group = self.mapping_dictionary[self.contractDTO.tariff_name()]["AcquisitionCostGroup"]
        self.amort_cost_group = self.mapping_dictionary[self.contractDTO.tariff_name()]["AmortizationCostGroup"]
        self.admin_cost_group = self.mapping_dictionary[self.contractDTO.tariff_name()]["AdministrationCostGroup"]

    def acquisition_cost_group(self) -> str:
        """
        Builds the acquisition cost group based on the mapping table and potentially a granular table
        :return: Acquisition cost group
        """
        if self.acqui_cost_group in self.mapping_dictionary_granular.keys():
            suffix = self.mapping_dictionary_granular[self.acqui_cost_group][self.acquisition_cost_group_granular()]
            return self.acqui_cost_group + suffix
        else:
            return self.acqui_cost_group

    def acquisition_cost_group_granular(self) -> str:
        """
        Is needed in case the cost group depends on other contract specific data than tariff name
        :return: Granular acquisition cost group
        """
        if self.acqui_cost_group == "AK_4":
            if self.contractDTO.deferment_period() < 55:
                return "Variant1"
            else:
                return "Variant2"
        elif self.acqui_cost_group == "AK_8_Courtagestufe2":
            if self.contractDTO.deferment_period() <= 21:
                return "Variant1"
            elif 21 < self.contractDTO.deferment_period() <= 30:
                return "Variant2"
            else:
                return "Variant3"

    def amortization_cost_group(self) -> str:
        """
        Builds the amortization cost group based on the mapping table and potentially a granular table
        :return: amortization cost group
        """
        if self.amort_cost_group in self.mapping_dictionary_granular.keys():
            suffix = self.mapping_dictionary_granular[self.amort_cost_group][self.amortization_cost_group_granular()]
            return self.amort_cost_group + suffix
        else:
            return self.amort_cost_group

    def amortization_cost_group_granular(self) -> str:
        """
        Is needed in case the cost group depends on other contract specific data than tariff name
        :return: Granular amortization cost group
        """
        if self.amort_cost_group == "AMK5":
            if self.contractDTO.deferment_period() <= 21:
                return "Variant1"
            elif 21 < self.contractDTO.deferment_period() <= 30:
                return "Variant2"
            else:
                return "Variant3"

    def administration_cost_group(self) -> str:
        """
        Builds the administration cost group based on the mapping table and potentially a granular table
        :return: administration cost group
        """
        self.admin_cost_group = self.mapping_dictionary[self.contractDTO.tariff_name()]["AdministrationCostGroup"]
        if self.admin_cost_group in self.mapping_dictionary_granular.keys():
            suffix = self.mapping_dictionary_granular[self.admin_cost_group][self.administration_cost_group_granular()]
            return self.admin_cost_group + suffix
        else:
            return self.admin_cost_group

    def administration_cost_group_granular(self) -> str:
        """
        Is needed in case the cost group depends on other contract specific data than tariff name
        :return: Granular administration cost group
        """
        if self.admin_cost_group == "LVK11":
            if self.contractDTO.is_non_contributory() == 1:
                return "Variant1"
            else:
                return "Variant2"

    def unit_cost_group(self) -> str:
        """
        Builds the unit cost group based on the mapping table and potentially a granular table
        :return: unit cost group
        """
        return self.mapping_dictionary[self.contractDTO.tariff_name()]["UnitCostGroup"]
