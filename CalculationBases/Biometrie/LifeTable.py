from os import path
from CPL_Prep import FileReader
from Contract import ContractDTO

class LifeTable(ContractDTO):

    def __init__(self,contract_nr):
        super().__init__(contract_nr=contract_nr)
        """
         This function selects the required life table  that should be used in the calculations based on tariff generation from the LifeTables.CSV
         :param Tariffgeneration: the life table is determined according to tariff generation
         :return: the required life table
        """
        relative_path = "/"
        csvFilename = "LifeTables.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        self.TG = reader.readColumnFromCSV("tg", type=int)
        self.LifeTablecsvName = reader.readColumnFromCSV("Life Table csv name", type=str)
        B = self.TG
        c = list(B.values())
        Index = c.index(self.tg()) # gets the index of the required tariff generation
        self.LifetablecsvName = self.LifeTablecsvName[Index] #gets the required life table based on the index number







