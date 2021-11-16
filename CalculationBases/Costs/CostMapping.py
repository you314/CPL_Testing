from CPL_Prep import FileReader
from Contract import ContractDTO
from os import path


class CostMapping:
    """
    A class used to provide a tariff name cost group mapping. Its methods rely on two csvs.
    TariffName_CostMapping.csv links the cost groups to the contract based on the tariff's name.
    Tariff_CostMapping_granular.csv adds a suffix to the cost group based on contract specific parameters.
    """

    def __init__(self, contract_nr):
        """
        :param int contract_nr: The mapping is done via the contract number, which provides the tariff name
        """
        self.contract_dto = ContractDTO()
        self.deferment_period = self.contract_dto.defermentperiod(Contractnr=contract_nr)
        self.tariff_name = self.contract_dto.tariff_name(Contractnr=contract_nr)
        self.is_non_contributory = self.contract_dto.is_non_contributory(Contractnr=contract_nr)
        relative_path = "/"
        csv_cost_mapping = "TariffName_CostMapping.csv"
        csv_cost_mapping_granular = "Tariff_CostMapping_granular.csv"
        file_tariff_name_cost_mapping = path.dirname(__file__) + relative_path + csv_cost_mapping
        file_tariff_name_cost_mapping_granular = path.dirname(__file__) + relative_path + csv_cost_mapping_granular
        self.reader_layer1 = FileReader(file_tariff_name_cost_mapping)
        self.reader_layer2 = FileReader(file_tariff_name_cost_mapping_granular)
        self.Mapping_dictionary1 = self.reader_layer1.create_mapping_by_key("TariffNames")
        self.Mapping_dictionary2 = self.reader_layer2.create_mapping_by_key("CostGroup")
        self.acquisition_cost_group_name = self.Mapping_dictionary1[self.tariff_name]["AcquisitionCostGroup"]
        self.amortization_cost_group_name = self.Mapping_dictionary1[self.tariff_name]["AmortizationCostGroup"]
        self.administration_cost_group_name = self.Mapping_dictionary1[self.tariff_name]["AdministrationCostGroup"]
        self.unit_cost_group_name = self.Mapping_dictionary1[self.tariff_name]["UnitCostGroup"]

    def acquisition_cost_group(self):
        """
        Determination of the acquisition's cost group
        :return: Combination of cost groups name and the suffix (optional)
        """
        if self.acquisition_cost_group_name in self.Mapping_dictionary2.keys():
            suffix = self.Mapping_dictionary2[self.acquisition_cost_group_name][self.acquisition_cost_group_granular()]
            return self.acquisition_cost_group_name + suffix
        else:
            return self.acquisition_cost_group_name

    def acquisition_cost_group_granular(self):
        """
        Determination of the acquisition's cost group suffix
        :return: The suffix of the cost group based on hard coded contract features
        """
        if self.acquisition_cost_group_name == "AK_4":
            if self.deferment_period < 55:
                return "Variant1"
            else:
                return "Variant2"
        elif self.acquisition_cost_group_name == "AK_8_Courtagestufe2":
            if self.deferment_period <= 21:
                return "Variant1"
            elif 21 < self.deferment_period <= 30:
                return "Variant2"
            else:
                return "Variant3"

    def amortization_cost_group(self):
        """
        Determination of the amortization's cost group
        :return: Combination of cost groups name and the suffix (optional)
        """
        if self.amortization_cost_group_name in self.Mapping_dictionary2.keys():
            suffix = self.Mapping_dictionary2[self.amortization_cost_group_name][self.amortization_cost_group_granular()]
            return self.amortization_cost_group_name + suffix
        else:
            return self.amortization_cost_group_name

    def amortization_cost_group_granular(self):
        """
        Determination of the amortization's cost group suffix
        :return: The suffix of the cost group based on hard coded contract features
        """
        if self.amortization_cost_group_name == "AMK5":
            if self.deferment_period <= 21:
                return "Variant1"
            elif 21 < self.deferment_period <= 30:
                return "Variant2"
            else:
                return "Variant3"

    def administration_cost_group(self):
        """
        Determination of the administration's cost group
        :return: Combination of cost groups name and the suffix (optional)
        """
        if self.administration_cost_group_name in self.Mapping_dictionary2.keys():
            suffix = self.Mapping_dictionary2[self.administration_cost_group_name][self.administration_cost_group_granular()]
            return self.administration_cost_group_name + suffix
        else:
            return self.administration_cost_group_name

    def administration_cost_group_granular(self):
        """
        Determination of the administration's cost group suffix
        :return: The suffix of the cost group based on hard coded contract features
        """
        if self.administration_cost_group_name == "LVK11":
            if self.is_non_contributory == 1:
                return "Variant1"
            else:
                return "Variant2"

    def unit_cost_group(self):
        """
        Determination of the unit's cost group
        :return: Cost group
        """
        return self.unit_cost_group_name
