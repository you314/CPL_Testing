from CPL_Prep import FileReader
from os import path

class Interest:

    def Interest_Vector(self,Tariffgeneration): #Todo improve to take one value of interest rate
            """
               This function selects the required interest vector  that should be used in the calculations based on tariff generation from the LifeTables.CSV
               :param Tariffgeneration: the interest vector is determined according to tariff generation
               :return: the required interest vector
              """
            relative_path = "/"
            csvFilename = "Interest.csv"
            pfad = path.dirname(__file__) + relative_path + csvFilename
            reader = FileReader(pfad)
            TG = str(Tariffgeneration)
            Vector= []
            Interest_Vector = reader.readColumnFromCSV(TG, type=str)
            x=len(Interest_Vector)
            for i in range(0,x):
                value= Interest_Vector[i]
                value1 = float(value)
                Vector.append(value1)
            return Vector





