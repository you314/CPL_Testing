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
        self.Test = reader.readCSV(type=str)
        self.Index = self.TN.index(self.TariffName)
        print(self.Index)
        #print(new_val)

    def AcquisitionCostGroup(self): #Todo improve to take one value of interest rate
        return self.ACG[self.Index]


print(CostMapping(Contractnr=123).AcquisitionCostGroup())

