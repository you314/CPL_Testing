
from CPL_Prep import FileReader
from os import path
from datetime import date
from typing import Union

class ContractDTO:

    def __init__(self):
        relative_path = "/"
        csvFilename = "Contract.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        self.ContractNR = reader.readColumnFromCSV("ContractNr", type=int)
        self.Tariff = reader.readColumnFromCSV("Tariff", type=str)
        self.Tariff_Name = reader.readColumnFromCSV("Tariff_Name", type=str)
        self.Age = reader.readColumnFromCSV("Age", type=int)
        self.TG = reader.readColumnFromCSV("TG", type=int)
        self.Birthyear = reader.readColumnFromCSV("Birthyear", type=int)
        self.Defermentperiod = reader.readColumnFromCSV("Deferment period", type=int)
        self.M = reader.readColumnFromCSV("m", type=int)
        self.Garantietime = reader.readColumnFromCSV("Garantie time", type=int)
        self.Sex= reader.readColumnFromCSV("Sex", type=str)

    def bedan(self):
        B= self.ContractNR
        c= list(B.values())
        return c


    def ContractIndex(self,Contractnr:int):
         Index= self.bedan().index(Contractnr)
         return Index

    def actuarialAge(self,Contractnr:int):
        Age=self.Age[self.ContractIndex(Contractnr=Contractnr)]
        return Age

    def Tg(self,Contractnr:int):
        Age=self.TG[self.ContractIndex(Contractnr=Contractnr)]
        return Age

    def tariff(self, Contractnr: int):
        tariff = self.Tariff[self.ContractIndex(Contractnr=Contractnr)]
        return tariff

    def tariff_name(self, Contractnr: int):
        tariff_name = self.Tariff_Name[self.ContractIndex(Contractnr=Contractnr)]
        return tariff_name

    def birthyear(self, Contractnr: int):
        Birthyear = self.Birthyear[self.ContractIndex(Contractnr=Contractnr)]
        return Birthyear

    def defermentperiod(self, Contractnr: int):
        Defermentperiod = self.Defermentperiod[self.ContractIndex(Contractnr=Contractnr)]
        return Defermentperiod

    def garantietime(self, Contractnr: int):
        Garantietime = self.Garantietime[self.ContractIndex(Contractnr=Contractnr)]
        return Garantietime

    def m(self, Contractnr: int):
        m = self.M[self.ContractIndex(Contractnr=Contractnr)]
        return m

    def sex(self, Contractnr: int):
        Sex = self.Sex[self.ContractIndex(Contractnr=Contractnr)]
        return Sex




    coinsuredActuarialAge: int = None
    actuarialAgeAtRetirement: int = None
    coinsuredActuarialAgeAtRetirement: int = None
    actuarialAgeAtRetirementFactual: int = None
    actuaralAgeAtInvalidity: int = None
    defermentPeriodInYears: int = None
    defermentPeriodInMonths: int = None
    paymentContributionsInYears: int = None
    paymentContributionsInMonths: int = None
    durationGuaranteeInYears: int = None
    pensionTermInYears: int = None
    zillmerizationInYears: int = None
    birthDate: date = None
    contractClosureDate: date = None
    coinsuredBirthDate: date = None
    paymentContributionsFrequency: int = None
    paymentAnnuityFrequency: int = None
    typeOfBrokerCortage: str = None
    numberPaymentsContributionsBeforeNonContributory: int = None
    isNonContributory: bool = None
    isAlive: bool = None
    isInRetirementStartingPhase: bool = None
    isDisabled: Union[bool,None] = None
    gender: str = None
    coinsuredGender: str = None
    collectiveType: str = None
    tariffType: str = None
    tariffLevel: str = None
    contractType: str = None
    tariffName: str = None
    tariffClass: int = None
    tariffThread: str = None
    profession: str = None
    contractState: str = None
    maximalBenefitPeriodInYears: int = None
    maximalBenefitPeriodInMonths: int = None
    waitingPeriodInMonths: int = None
    incrementOfGuaranteeOfYearlyIncreaseOfAnnuity: float = None
    professionSpecificFactor: float = None
    sumOfPayedPremiums: float = None



