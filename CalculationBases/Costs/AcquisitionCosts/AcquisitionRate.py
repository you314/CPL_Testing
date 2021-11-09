from os import path
from CPL_Prep import FileReader
from CalculationBases.Costs.CostMapping import CostMapping


class AcquisitionRate():

    def __init__(self,Contractnr): # ToDo: Logic for CostGroups needs to be included, or part of the IL
        relative_path = "/"
        csvFilename = "AcquisitionCostRates.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        self.reader = FileReader(pfad)
        self.CostGroup = CostMapping(Contractnr=Contractnr).acquisition_cost_group()
        self.CG_Index = list(self.reader.readColumnFromCSV("AcquisitionCostGroups", type=str).values()).index(self.CostGroup)
        self.CV = list(self.reader.readColumnFromCSV("CostVariables", type=str).values())

    def alpha_z(self):
        if "alpha_z" == self.CV[self.CG_Index]:
            return float(list(self.reader.readColumnFromCSV("Rates", type=str).values())[self.CG_Index])
        else:
            return 0

    def alpha(self):
        if "alpha" == self.CV[self.CG_Index]:
            return float(list(self.reader.readColumnFromCSV("Rates", type=str).values())[self.CG_Index])
        else:
            return 0

    def alpha_1(self):
        if "alpha_1" == self.CV[self.CG_Index]:
            return float(list(self.reader.readColumnFromCSV("Rates", type=str).values())[self.CG_Index])
        else:
            return 0

    def alpha_2(self):
        if "alpha_2" == self.CV[self.CG_Index]:
            return float(list(self.reader.readColumnFromCSV("Rates", type=str).values())[self.CG_Index])
        else:
            return 0

    def alpha_3(self):
        if "alpha_3" == self.CV[self.CG_Index]:
            return float(list(self.reader.readColumnFromCSV("Rates", type=str).values())[self.CG_Index])
        else:
            return 0

print("Alpha_z cost rate is: " + str(AcquisitionRate(Contractnr=124).alpha_z()*100) + "%")
print("Alpha cost rate is: " + str(AcquisitionRate(Contractnr=124).alpha()*100) + "%")
print("Alpha_1 cost rate is: " + str(AcquisitionRate(Contractnr=124).alpha_1()*100) + "%")
print("Alpha_2 cost rate is: " + str(AcquisitionRate(Contractnr=124).alpha_2()*100) + "%")
print("Alpha_3 cost rate is: " + str(AcquisitionRate(Contractnr=124).alpha_3()*100) + "%")
