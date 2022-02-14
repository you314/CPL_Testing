from os import path
from helper.cpl_prep import FileReader
from calculationbases.cost.cost_mapping import CostMapping


class AcquisitionRate:
    """
    Class used to provide the acquisition cost rate. Its method relies on a csv.
    AcquisitionRates.csv links the unit cost rate to the acquisition cost group coming from the class cost_mapping.py.
    """

    def __init__(self, contract_nr):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        """
        :param int contract_nr: The mapping is done via the contract number, which provides the tariff name
        """
        relative_path = "/"
        csv_filename = "AcquisitionCostRates.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.mapping_dictionary = csv_reader.create_mapping_by_key("AcquisitionCostGroups")
        self.cost_group = CostMapping(contract_nr=contract_nr).acquisition_cost_group()

    def get_acquisition_cost_by_name(self, cost_type) -> float:
        """
        Getting the acquisitions cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Acquisition cost rate
        """
        value = self.mapping_dictionary[self.cost_group][cost_type]
        return float(value)

