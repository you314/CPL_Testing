from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class AcquisitionRate:
    """
    Class used to provide the acquisition cost rate. Its method relies on a csv.
    AcquisitionRates.csv links the unit cost rate to the acquisition cost group coming from the class CostMapping.py.
    """

    def __init__(self, contract_nr):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        """
        :param int contract_nr: The mapping is done via the contract number, which provides the tariff name
        """
        relative_path = "/"
        csv_filename = "AcquisitionCostRates.csv"
        file_path = path.dirname(__file__) + relative_path + csv_filename
        self.reader = FileReader(file_path)
        self.Mapping_dictionary = self.reader.create_mapping_by_key("AcquisitionCostGroups")
        self.CostGroup = CostMapping(contract_nr=contract_nr).acquisition_cost_group()

    def get_acquisition_cost_by_name(self, cost_type):
        """
        Getting the acquisitions cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Acquisition cost rate
        """
        value = self.Mapping_dictionary[self.CostGroup][cost_type]
        return float(value)
