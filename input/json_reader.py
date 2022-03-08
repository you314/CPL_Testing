import json
from os import path


class JsonReader:

    def __init__(self):
        relative_path = "/"
        filename = "TestContract_pv.json"
        file_path = path.dirname(__file__) + relative_path + filename
        file = open(file_path, 'r')
        self.data = json.load(file)

    def actuarial_age(self) -> int:
        age_raw = json.dumps(self.data['contract']['TLSCHDETAIL']['new'][0]['BEITRALTER'])
        age = int(age_raw.replace("\"", ""))
        return age

    def tariff_name(self) -> str:
        tariff_name_raw = json.dumps(self.data['contract']['TLSCHDETAIL']['new'][0]['TARBEZEICHNUNG'])
        tariff_name = tariff_name_raw.replace("\"", "")
        return tariff_name

    def premium_payment_duration(self) -> str:
        PRZDA_raw = json.dumps(self.data['contract']['TLEBENSCHICHT']['new'][0]['PRZAHLDAUER'])
        PRZDA = PRZDA_raw.replace("\"", "")
        return int(int(PRZDA)/12)

    def tg(self) -> int:
        tarif_name_list = self.tariff_name().split(sep='/', maxsplit=1)
        tarif_generation = int(tarif_name_list[1])
        return tarif_generation

    def tariff(self) -> str:
        tarif_name_list = self.tariff_name().split(sep='/', maxsplit=1)
        return tarif_name_list[0]

    def birth_year(self) -> int:
        birth_date_raw = json.dumps(self.data['contract']['TNATPERS']['new'][0]['GEBURTSDATUM'])
        birth_date = birth_date_raw.replace("\"", "")
        birth_date_list = birth_date.split(sep='-')
        birth_year = int(birth_date_list[0])
        return birth_year

    def deferment_period(self) -> int:
        deferment_period_raw = json.dumps(self.data['contract']['TPENSVEREINBG']['new'][0]['RENTENAUFDAUER'])
        deferment_period1 = int(deferment_period_raw.replace("\"", ""))
        deferment_period= int(deferment_period1/12)

        return deferment_period

    def guarantee_time(self) -> int:
        guarantee_time_raw = json.dumps(self.data['contract']['TPENSVEREINBG']['new'][0]['REVERGARZEIT'])
        guarantee_time = int(guarantee_time_raw.replace("\"", ""))
        return guarantee_time

    # Needs to be determined how to create m. Maybe CalcDate-BEGINNDAT... For now setting m=0
    def m(self,) -> int:
        m = 1  # self.m_dict[self.contract_index()]
        return m

    def sex(self) -> str:
        sex_raw = json.dumps(self.data['contract']['TNATPERS']['new'][0]['GESCHLECHT'])
        sex = sex_raw.replace("\"", "")
        return sex

    def profession(self) -> str:
        profession_raw = json.dumps(self.data['contract']['TBERUF']['new'][0]['BERUF'])
        profession = profession_raw.replace("\"", "")
        return profession

    #TODO: Check if this is correct and how it can be translated!
    def is_non_contributory(self) -> int:
        is_non_contributory_raw = json.dumps(self.data['contract']['TVERTRAG']['new'][0]['ZUSTAND'])
        is_non_contributory_aux = is_non_contributory_raw.replace("\"", "")
        if is_non_contributory_aux == "A":
            is_non_contributory = 0
        else:
            is_non_contributory = 1
        return is_non_contributory

    # TODO: Output is M for monthly -> Discuss if logic should be part of this module.
    def payment_contributions_frequency(self) -> int:
        payment_contributions_frequency_raw = json.dumps(self.data['contract']['TVERTRAG']['new'][0]['ZAHLWEISE'])
        payment_contributions_frequency_aux = payment_contributions_frequency_raw.replace("\"", "")
        if payment_contributions_frequency_aux == "M":
            payment_contributions_frequency = 12
        elif payment_contributions_frequency_aux == "Q":
            payment_contributions_frequency = 4
        elif payment_contributions_frequency_aux == "S":
            payment_contributions_frequency = 2
        else:
            payment_contributions_frequency = 1
        return payment_contributions_frequency

    def pension_payment_period(self) -> int:
        pension_payment_period_raw = json.dumps(self.data['contract']['TLEBENSCHICHT']['new'][0]['LEISTUNGSDAUER'])
        pension_payment_period = int(pension_payment_period_raw.replace("\"", ""))
        return pension_payment_period




JsonReader = JsonReader()






