from CPL_Prep import FileReader
from os import path
from datetime import date
from typing import Union


class ContractDTO:

    def __init__(self, contract_nr):
        relative_path = "/"
        csv_filename = "Contract.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.contract_nr = contract_nr
        self.contract_nr_dict = csv_reader.readColumnFromCSV("ContractNr", type=int)
        self.tariff_dict = csv_reader.readColumnFromCSV("tariff", type=str)
        self.tariff_name_dict = csv_reader.readColumnFromCSV("tariff_name", type=str)
        self.age_dict = csv_reader.readColumnFromCSV("age", type=int)
        self.tg_dict = csv_reader.readColumnFromCSV("tg", type=int)
        self.birth_year_dict = csv_reader.readColumnFromCSV("birth_year", type=int)
        self.deferment_period_dict = csv_reader.readColumnFromCSV("deferment_period", type=int)
        self.m_dict = csv_reader.readColumnFromCSV("m", type=int)
        self.guarantee_time_dict = csv_reader.readColumnFromCSV("garantie_time", type=int)
        self.is_non_contributory_dict = csv_reader.readColumnFromCSV("is_non_contributory", type=int)
        self.sex_dict = csv_reader.readColumnFromCSV("sex", type=str)
        self.payment_contributions_frequency_dict = csv_reader.readColumnFromCSV("payment_contributions_frequency", type=str)
        self.pension_payment_period_dict = csv_reader.readColumnFromCSV("pension_payment_period", type=str)

    def contract_nr_auxiliary_function(self):
        contract_nr_list = list(self.contract_nr_dict.values())
        return contract_nr_list

    def contract_index(self):
        index = self.contract_nr_auxiliary_function().index(self.contract_nr)
        return index

    def actuarial_age(self):
        age = self.age_dict[self.contract_index()]
        return age

    def tg(self):
        tg = self.tg_dict[self.contract_index()]
        return tg

    def tariff(self):
        tariff = self.tariff_dict[self.contract_index()]
        return tariff

    def tariff_name(self):
        tariff_name = self.tariff_name_dict[self.contract_index()]
        return tariff_name

    def birth_year(self):
        birth_year = self.birth_year_dict[self.contract_index()]
        return birth_year

    def deferment_period(self):
        deferment_period = self.deferment_period_dict[self.contract_index()]
        return deferment_period

    def guarantee_time(self):
        guarantee_time = self.guarantee_time_dict[self.contract_index()]
        return guarantee_time

    def m(self,):
        m = self.m_dict[self.contract_index()]
        return m

    def sex(self):
        sex = self.sex_dict[self.contract_index()]
        return sex

    def is_non_contributory(self):
        is_non_contributory = self.is_non_contributory_dict[self.contract_index()]
        return is_non_contributory

    def payment_contributions_frequency(self):
        payment_contributions_frequency = self.payment_contributions_frequency_dict[self.contract_index()]
        return payment_contributions_frequency

    def pension_payment_period(self):
        pension_payment_period = self.pension_payment_period_dict[self.contract_index()]
        return pension_payment_period

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
    pension_payment_period_dict:  int = None


print(ContractDTO(contract_nr=123).contract_nr_auxiliary_function())

