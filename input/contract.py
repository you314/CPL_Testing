from CPLTesting.helper.cpl_prep import FileReader
from os import path
from datetime import date
from typing import Union


class ContractDTO:

    def __init__(self, contract_nr: int):
        relative_path = "/"
        csv_filename = "Contract.csv"
        csv_path = path.dirname(__file__) + relative_path + csv_filename
        csv_reader = FileReader(csv_path)
        self.contract_nr = contract_nr
        self.contract_nr_dict = csv_reader.read_column_from_csv("ContractNr", type=int)
        self.tariff_dict = csv_reader.read_column_from_csv("tariff", type=str)
        self.tariff_name_dict = csv_reader.read_column_from_csv("tariff_name", type=str)
        self.age_dict = csv_reader.read_column_from_csv("age", type=int)
        self.tg_dict = csv_reader.read_column_from_csv("tg", type=int)
        self.birth_year_dict = csv_reader.read_column_from_csv("birth_year", type=int)
        self.deferment_period_dict = csv_reader.read_column_from_csv("deferment_period", type=int)
        self.m_dict = csv_reader.read_column_from_csv("m", type=int)
        self.guarantee_time_dict = csv_reader.read_column_from_csv("garantie_time", type=int)
        self.is_non_contributory_dict = csv_reader.read_column_from_csv("is_non_contributory", type=int)
        self.sex_dict = csv_reader.read_column_from_csv("sex", type=str)
        self.payment_contributions_frequency_dict = csv_reader.read_column_from_csv("payment_contributions_frequency", type=str)
        self.pension_payment_period_dict = csv_reader.read_column_from_csv("pension_payment_period", type=str)
        self.profession_dict = csv_reader.read_column_from_csv("profession", type=str)

    def contract_nr_auxiliary_function(self) -> list[int]:
        contract_nr_list = list(self.contract_nr_dict.values())
        return contract_nr_list

    def contract_index(self) -> int:
        index = self.contract_nr_auxiliary_function().index(self.contract_nr)
        return index

    def actuarial_age(self) -> int:
        age = self.age_dict[self.contract_index()]
        return age

    def tg(self) -> int:
        tg = self.tg_dict[self.contract_index()]
        return tg

    def tariff(self) -> str:
        tariff = self.tariff_dict[self.contract_index()]
        return tariff

    def tariff_name(self) -> str:
        tariff_name = self.tariff_name_dict[self.contract_index()]
        return tariff_name

    def birth_year(self) -> int:
        birth_year = self.birth_year_dict[self.contract_index()]
        return birth_year

    def deferment_period(self) -> int:
        deferment_period = self.deferment_period_dict[self.contract_index()]
        return deferment_period

    def guarantee_time(self) -> int:
        guarantee_time = self.guarantee_time_dict[self.contract_index()]
        return guarantee_time

    def m(self,) -> int:
        m = self.m_dict[self.contract_index()]
        return m

    def sex(self) -> str:
        sex = self.sex_dict[self.contract_index()]
        return sex

    def profession(self) -> str:
        profession = self.profession_dict[self.contract_index()]
        return profession

    def is_non_contributory(self) -> int:
        is_non_contributory = self.is_non_contributory_dict[self.contract_index()]
        return is_non_contributory

    def payment_contributions_frequency(self) -> int:
        payment_contributions_frequency = self.payment_contributions_frequency_dict[self.contract_index()]
        return payment_contributions_frequency

    def pension_payment_period(self) -> int:
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
    contractState: str = None
    maximalBenefitPeriodInYears: int = None
    maximalBenefitPeriodInMonths: int = None
    waitingPeriodInMonths: int = None
    incrementOfGuaranteeOfYearlyIncreaseOfAnnuity: float = None
    professionSpecificFactor: float = None
    sumOfPayedPremiums: float = None
    pension_payment_period_dict:  int = None


print("Available contract numbers: " + str(ContractDTO(contract_nr=123).contract_nr_auxiliary_function()))
