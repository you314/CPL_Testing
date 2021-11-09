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
        reader = FileReader(pfad)

        self.TN = list(reader.readColumnFromCSV("TariffNames", type=str).values())
        self.ACG = list(reader.readColumnFromCSV("AcquisitionCostGroup", type=str).values())
        self.ACT = list(reader.readColumnFromCSV("ACType", type=str).values())
        self.AMG = list(reader.readColumnFromCSV("AmortizationCostGroup", type=str).values())
        self.AMT = list(reader.readColumnFromCSV("AMType", type=str).values())
        self.ADG = list(reader.readColumnFromCSV("AdministrationCostGroup", type=str).values())
        self.ADT = list(reader.readColumnFromCSV("ADType", type=str).values())
        self.UCG = list(reader.readColumnFromCSV("UnitCostGroup", type=str).values())
        self.UCT = list(reader.readColumnFromCSV("UCType", type=str).values())
        self.Index = self.TN.index(self.TariffName)

    def AcquisitionCostGroup(self):
        return self.ACG[self.Index]
    def AcquisitionCostType(self):
        return self.ACT[self.Index]
    def AmortizationCostGroup(self):
        return self.AMG[self.Index]
    def AmortizationCostType(self):
        return self.AMT[self.Index]
    def AdministrationCostGroup(self):
        return self.ADG[self.Index]
    def AdminstrationCostType(self):
        return self.ADT[self.Index]
    def AdministrationCostGroup(self):
        return self.ADG[self.Index]
    def AdminstrationCostType(self):
        return self.ADT[self.Index]

print(CostMapping(Contractnr=123).AcquisitionCostGroup())
print(CostMapping(Contractnr=123).AcquisitionCostType())
