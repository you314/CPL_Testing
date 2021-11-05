
from PresentValues import Presentvalues
from Contract import ContractDTO
from FLags.Flags import Flags



class Tariff():

    def __init__(self,Contractnr):
        self.ContractDTO = ContractDTO()
        self.Presentvalues= Presentvalues(Contractnr=Contractnr)
        self.Flags= Flags()
        self.Tariff = self.ContractDTO.tariff(Contractnr=Contractnr)
        self.Tariffgeneration = self.ContractDTO.Tg(Contractnr=Contractnr)
        self.Defermentperiod = self.ContractDTO.defermentperiod(Contractnr=Contractnr)
        self.BirthDate = self.ContractDTO.birthyear(Contractnr=Contractnr)
        self.Garantietime = self.ContractDTO.garantietime(Contractnr=Contractnr)
        self.m = self.ContractDTO.m(Contractnr=Contractnr)
        self.flagsVector = self.Flags.FlagsVector(Tariffgeneration=self.Tariffgeneration, Tariff=self.Tariff)
        self.Age = self.ContractDTO.actuarialAge(Contractnr)
        self.sex = self.ContractDTO.sex(Contractnr)


    def NetPremiumRente(self):
        gamma =0.1
        netPremium =(1+gamma)*self.flagsVector[1]*self.Presentvalues.aeg(g=self.Garantietime,Tariffgeneration=self.Tariffgeneration) * \
                    self.flagsVector[2] +self.Presentvalues.aegk(g=self.Garantietime,k=self.m,Tariffgeneration=self.Tariffgeneration)*\
                    self.flagsVector[3] + self.Presentvalues.n_m_a_x(Defermentperiod= self.Defermentperiod,m=self.m,age=self.Age,birthDate=self.BirthDate,sex=self.sex,Tariffgeneration=self.Tariffgeneration)


        return netPremium

print(Tariff(Contractnr=1234).NetPremiumRente())


