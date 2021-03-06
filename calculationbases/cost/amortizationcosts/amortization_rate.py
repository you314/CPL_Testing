from os import path
from helper.cpl_prep import FileReader
from calculationbases.cost.cost_mapping import CostMapping


class AmortizationRate:
    """
    Class used to provide the amortization cost rate. Its method relies on a csv.
    AmortizationRates.csv links the unit cost rate to the amortization cost group coming from the class cost_mapping.py.
    """

    def __init__(self):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        """
        :param int contract_nr: The mapping is done via the contract number, which provides the tariff name
        """
        relative_path = "/"
        csv_filename = "AmortizationCostRates.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.mapping_dictionary = csv_reader.create_mapping_by_key("AmortizationCostGroups")
        self.cost_group = CostMapping().amortization_cost_group()

    def alpha_gamma(self) -> float:
        """
        Getting the amortization cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Amortization cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["alpha_gamma"]
        return float(value)

    def alpha_beta(self) -> float:
        """
        Getting the amortization cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Amortization cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["alpha_beta"]
        return float(value)

