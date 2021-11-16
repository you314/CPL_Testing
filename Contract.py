
from CPL_Prep import FileReader
from os import path
from datetime import date
from typing import Union


class ContractDTO:

    def __init__(self, contract_nr):
        relative_path = "/"
        csvFilename = "Contract.csv"
        pfad = path.dirname(__file__) + relative_path + csvFilename
        reader = FileReader(pfad)
        self.contract_nr = contract_nr
        self.contract_nr_dict = reader.readColumnFromCSV("ContractNr", type=int)
        self.Tariff = reader.readColumnFromCSV("tariff", type=str)
        self.Tariff_name = reader.readColumnFromCSV("tariff_name", type=str)
        self.age = reader.readColumnFromCSV("age", type=int)
        self.Tg = reader.readColumnFromCSV("tg", type=int)
        self.birth_year = reader.readColumnFromCSV("birth_year", type=int)
        self.deferment_period = reader.readColumnFromCSV("deferment_period", type=int)
        self.M = reader.readColumnFromCSV("m", type=int)
        self.garantie_time = reader.readColumnFromCSV("garantie_time", type=int)
        self.Is_non_contributory = reader.readColumnFromCSV("is_non_contributory", type=int)
        self.Sex = reader.readColumnFromCSV("sex", type=str)
        self.payment_contributions_frequency = reader.readColumnFromCSV("payment_contributions_frequency", type=str)
        self.pension_payment_period = reader.readColumnFromCSV("pension_payment_period", type=str)

    def bedan(self):
        B = self.contract_nr_dict
        c = list(B.values())
        return c

    def contract_index(self):
         Index= self.bedan().index(self.contract_nr)
         return Index

    def actuarial_age(self):
        Age=self.age[self.contract_index()]
        return Age

    def tg(self):
        Age=self.Tg[self.contract_index()]
        return Age

    def tariff(self):
        tariff = self.Tariff[self.contract_index()]
        return tariff

    def tariff_name(self):
        tariff_name = self.Tariff_name[self.contract_index()]
        return tariff_name

    def birthyear(self):
        Birthyear = self.birth_year[self.contract_index()]
        return Birthyear

    def defermentperiod(self):
        Defermentperiod = self.deferment_period[self.contract_index()]
        return Defermentperiod

    def garantietime(self):
        Garantietime = self.garantie_time[self.contract_index()]
        return Garantietime

    def m(self,):
        m = self.M[self.contract_index()]
        return m

    def sex(self):
        Sex = self.Sex[self.contract_index()]
        return Sex

    def is_non_contributory(self):
        isNonContributory = self.Is_non_contributory[self.contract_index()]
        return isNonContributory

    def paymentContributionsFrequency(self):
        paymentContributionsFrequency = self.payment_contributions_frequency[self.contract_index()]
        return paymentContributionsFrequency

    def pensionPaymentPeriod(self):
        pensionPaymentPeriod = self.pension_payment_period[self.contract_index()]
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


print(ContractDTO(contract_nr=123).bedan())

