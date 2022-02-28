from os import path
from helper.cpl_prep import FileReader
from calculationbases.cost.cost_mapping import CostMapping


class AdministrationRate:
    """
    Class used to provide the administration cost rate. Its method relies on a csv.
    AdministrationRates.csv links the unit cost rate to the admin cost group coming from the class cost_mapping.py.
    """

    def __init__(self):  # ToDo: Logic for CostGroups needs to be included, or be part of the IL
        """
        :param int contract_nr: The mapping is done via the contract number, which provides the tariff name
        """
        relative_path = "/"
        csv_filename = "AdministrationCostRates.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.mapping_dictionary = csv_reader.create_mapping_by_key("AdministrationCostGroups")
        self.cost_group = CostMapping().administration_cost_group()

    def beta(self) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["beta"]
        return float(value)

    def beta_SP(self) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["beta_SP"]
        return float(value)

    def gamma_11(self) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["gamma_11"]
        return float(value)

    def gamma_12(self, cost_type) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["gamma_12"]
        return float(value)

    def gamma_1(self) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["gamma_1"]
        return float(value)

    def gamma_2(self) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["gamma_2"]
        return float(value)

    def gamma_3(self) -> float:
        """
        Getting the administration cost rate for a cost type, based on cost group
        :param cost_type: Needs to match the cost_type name in the csv
        :return: Administration cost rate
        """
        value = self.mapping_dictionary[self.cost_group]["gamma_3"]
        return float(value)


print(AdministrationRate().gamma_3())
