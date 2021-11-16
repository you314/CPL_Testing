
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
        self.contract_nr = reader.readColumnFromCSV("ContractNr", type=int)
        self.Tariff = reader.readColumnFromCSV("tariff", type=str)
        self.tariff_name = reader.readColumnFromCSV("tariff_name", type=str)
        self.age = reader.readColumnFromCSV("age", type=int)
        self.Tg = reader.readColumnFromCSV("tg", type=int)
        self.birth_year = reader.readColumnFromCSV("birth_year", type=int)
        self.deferment_period = reader.readColumnFromCSV("deferment_period", type=int)
        self.M = reader.readColumnFromCSV("m", type=int)
        self.garantie_time = reader.readColumnFromCSV("garantie_time", type=int)
        self.is_non_contributory = reader.readColumnFromCSV("is_non_contributory", type=int)
        self.Sex = reader.readColumnFromCSV("sex", type=str)
        self.payment_contributions_frequency = reader.readColumnFromCSV("payment_contributions_frequency", type=str)
        self.pension_payment_period = reader.readColumnFromCSV("pension_payment_period", type=str)

    def bedan(self):
        B= self.contract_nr
        c= list(B.values())
        return c

    def contract_index(self, contract_nr:int):
         Index= self.bedan().index(contract_nr)
         return Index

    def actuarial_age(self, contract_nr:int):
        Age=self.age[self.contract_index(contract_nr=contract_nr)]
        return Age

    def tg(self, contract_nr:int):
        Age=self.Tg[self.contract_index(contract_nr=contract_nr)]
        return Age

    def tariff(self, contract_nr: int):
        tariff = self.Tariff[self.contract_index(contract_nr=contract_nr)]
        return tariff

    def tariff_name(self, contract_nr: int):
        tariff_name = self.tariff_name[self.contract_index(contract_nr=contract_nr)]
        return tariff_name

    def birthyear(self, contract_nr: int):
        Birthyear = self.birth_year[self.contract_index(contract_nr=contract_nr)]
        return Birthyear

    def defermentperiod(self, contract_nr: int):
        Defermentperiod = self.deferment_period[self.contract_index(contract_nr=contract_nr)]
        return Defermentperiod

    def garantietime(self, contract_nr: int):
        Garantietime = self.garantie_time[self.contract_index(contract_nr=contract_nr)]
        return Garantietime

    def m(self, contract_nr: int):
        m = self.M[self.contract_index(contract_nr=contract_nr)]
        return m

    def sex(self, contract_nr: int):
        Sex = self.Sex[self.contract_index(contract_nr=contract_nr)]
        return Sex

    def is_non_contributory(self, contract_nr: int):
        isNonContributory = self.is_non_contributory[self.contract_index(contract_nr=contract_nr)]
        return isNonContributory

    def paymentContributionsFrequency(self, contract_nr: int):
        paymentContributionsFrequency = self.payment_contributions_frequency[self.contract_index(contract_nr=contract_nr)]
        return paymentContributionsFrequency

    def pensionPaymentPeriod(self, contract_nr: int):
        pensionPaymentPeriod = self.pension_payment_period[self.contract_index(contract_nr=contract_nr)]
        return pensionPaymentPeriod




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
    paymentAnnuityFrequency: int = None
    typeOfBrokerCortage: str = None
    numberPaymentsContributionsBeforeNonContributory: int = None
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
    pension_payment_period:  int = None



