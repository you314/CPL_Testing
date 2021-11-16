from CPL_Prep import FileReader
from os import path


class Flags:

    def create_matrix(self, tariff_generation, tariff:str): # Todo Change the code to understandable one
        relative_path = "/"
        csv_file = "formulas used.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_file
        csv_reader = FileReader(csv_path)
        NetPremium1 = csv_reader.readColumnFromCSV("tg", type=int)
        x0= list(NetPremium1.values())
        rowCount = len(NetPremium1)
        NetPremium2 = csv_reader.read_row_from_csv(0, type=str)
        x1 = list(NetPremium2.keys())
        indexTG = x0.index(int(tariff_generation))
        indexTariff = x1.index(tariff)

        colCount = len(NetPremium2)
        mat = []
        for i in range(rowCount):
            X = csv_reader.read_row_from_csv(i)
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
        NetPremium1 = reader.readColumnFromCSV(self.create_matrix(tariff_generation=Tariffgeneration, tariff=Tariff), type=str)
        FlagsVector= list(NetPremium1)
        return FlagsVector








