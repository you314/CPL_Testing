from CPL_Prep import FileReader
from Contract import ContractDTO
from os import path


class CostMapping:

    def __init__(self, Contractnr):
        self.ContractDTO = ContractDTO()
        self.TariffName = self.ContractDTO.tariff_name(Contractnr=Contractnr)
        relative_path = "/"
        csvFilename = "TariffName_CostMapping.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        self.reader = FileReader(pfad)
        self.TN_Index = list(self.reader.readColumnFromCSV("TariffNames", type=str).values()).index(self.TariffName)

    def acquisition_cost_group(self):
        return list(self.reader.readColumnFromCSV("AcquisitionCostGroup", type=str).values())[self.TN_Index]

    def amortization_cost_group(self):
        return list(self.reader.readColumnFromCSV("AmortizationCostGroup", type=str).values())[self.TN_Index]

    def administration_cost_group(self):
        return list(self.reader.readColumnFromCSV("AdministrationCostGroup", type=str).values())[self.TN_Index]

    def unit_cost_group(self):
        return list(self.reader.readColumnFromCSV("UnitCostGroup", type=str).values())[self.TN_Index]


print("Tariff name is: " + CostMapping(Contractnr=124).acquisition_cost_group())
