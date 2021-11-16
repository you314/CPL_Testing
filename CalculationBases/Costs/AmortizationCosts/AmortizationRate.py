from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class AmortizationRate:
    """
    Class used to provide the amortization cost rate. Its method relies on a csv.
    AmortizationRates.csv links the unit cost rate to the amortization cost group coming from the class CostMapping.py.
    """

    def __init__(self, contract_nr):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        """
        :param int contract_nr: The mapping is done via the contract number, which provides the tariff name
        """
        relative_path = "/"
        csv_filename = "AmortizationCostRates.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("AmortizationCostGroups")
        self.CostGroup = CostMapping(contract_nr=contract_nr).amortization_cost_group()

    def get_amortization_cost_by_name(self, cost_type):
        """
        Getting the amortization cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Amortization cost rate
        """
        value = self.Mapping_dictionary[self.CostGroup][cost_type]
        return float(value)
