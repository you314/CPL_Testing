from os import path
from CPL_Prep import FileReader

class AcquisitionRate():

    def __init__(self,Tariffgeneration):
        relative_path = "/"
        csvFilename = "AK.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        self.TG = reader.readColumnFromCSV("TG", type=int)
        self.LifeTablecsvName = reader.readColumnFromCSV("Life Table csv name", type=str)
        B = self.TG
        c = list(B.values())
        Index = c.index(Tariffgeneration)
        self.LifetablecsvName = self.LifeTablecsvName[Index]