from calculationbases.flagsterms.cflags.pv_annuity import PresentValues
from input.json_reader import JsonReader
from input.contract import ContractDTO
from calculationbases.flagsterms.mf_annuity_flags import Flags




class Tariff():

        def __init__(self):  # , contract_nr: int):  # ToDo Evaluate if inheritance is the right approach here
            # super().__init__()  # contract_nr=contract_nr)
            self.present_values = PresentValues()  # contract_nr=contract_nr)
            self.flags = Flags()
            self.contract_Dto = JsonReader
            # self.flags_vector = self.flags.Gross_Premium_flags_vector(tariff= ContractDTO.tariff(self))
            self.flags_vector_J = self.flags.gross_premium_flags_vector(tariff=self.contract_Dto.tariff_name())

        def Gross_premium_annuity(self) -> float:
            """
            Maxi formula for the gross single premium annuity
            """
            gamma = 0.4
            ### maxi formula needs yet to be adjusted ###
            GP = (1 + gamma) * self.flags_vector_J[0] * self.present_values.c0_nax_k(deferment_period=self.contract_Dto.deferment_period(),
                                                                                     age=self.contract_Dto.actuarial_age()
                                                                                ,birth_date= self.contract_Dto.birth_year(),
                                                    payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency() )\
                 +\
                 self.flags_vector_J[2] + self.present_values.aegk(guarantee_time=self.contract_Dto.guarantee_time(), k=self.contract_Dto.m()) * \
                 self.flags_vector_J[3]
            return GP


        def annual_gross_premium_annuity(self) -> float:
            """
            Maxi formula for the gross annual premium annuity
            """
            gamma = 0.1
            annual_gross_premuium_annuity = 0
            return annual_gross_premuium_annuity

        def single_netto_premium_annuity(self) -> float:
            """
            Maxi formula for the netto single premium annuity
            """
            gamma = 0.1
            single_netto_premuium_annuity = 0
            return single_netto_premuium_annuity

        def annual_netto_premium_annuity(self) -> float:
            """
            Maxi formula for the netto annual premium annuity
            """
            gamma = 0.1
            annual_netto_premuium_annuity = 0
            return annual_netto_premuium_annuity

        def reserves_annuity(self, reserve_type='a') -> float:
            """
            Maxi formula for the capital reserves a, b & c (reserve_type argument)
            """
            gamma = 0.1
            reserves_annuity = 0.
            if reserve_type == 'a':
                reserves_annuity = 0

            elif reserve_type == 'b':
                reserves_annuity = 0

            elif reserve_type == 'c':
                reserves_annuity = 0

            return reserves_annuity

print("NetPremium for example tariff: " + str(1000*Tariff().Gross_premium_annuity()) + " (Desired value: 2.082159965161852)")
