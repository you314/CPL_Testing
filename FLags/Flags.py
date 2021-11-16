from CPL_Prep import FileReader
from os import path



class Flags():


    def createMatrix(self, Tariffgeneration,Tariff:str): # Todo Change the code to understandable one
        relative_path = "/"
        csvFilename = "formulas used.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        NetPremium1 = reader.readColumnFromCSV("tg", type=int)
        x0= list(NetPremium1.values())
        rowCount = len(NetPremium1)
        NetPremium2 = reader.read_row_from_csv(0, type=str)
        x1 = list(NetPremium2.keys())
        indexTG = x0.index(int(Tariffgeneration))
        indexTariff = x1.index(Tariff)

        colCount = len(NetPremium2)
        mat = []
        for i in range(rowCount):
            X = reader.read_row_from_csv(i)
            rowList = []
            for j in range(colCount):
                # you need to increment through dataList here, like this:
                y = X[x1[j]]
                rowList.append(y)
            mat.append(rowList)
        Matrixentry= mat[indexTG][indexTariff]
        return Matrixentry

    def FlagsVector(self,Tariffgeneration,Tariff:str):
        relative_path = "/"
        csvFilename = "Premium.Flags.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        NetPremium1 = reader.readColumnFromCSV(self.createMatrix(Tariffgeneration=Tariffgeneration,Tariff=Tariff), type=str)
        FlagsVector= list(NetPremium1)
        return FlagsVector








