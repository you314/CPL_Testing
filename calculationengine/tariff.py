from calculationbases.flagsterms.cflags.pv_annuity import PresentValues
from calculationbases.flagsterms.eflags.cost_annuity import Costs
from calculationbases.biometry.cpl_bio import BiometryCpl
from input.json_reader import JsonReader
from calculationbases.cost.administrationcosts.administration_rate import AdministrationRate
from calculationbases.cost.amortizationcosts.amortization_rate import AmortizationRate
from calculationbases.cost.acquisitioncosts.acquisition_rate import AcquisitionRate
import time
from calculationbases.flagsterms.mf_annuity_flags import Flags




class Tariff():

        def __init__(self):
            self.present_values = PresentValues()
            self.Biometry = BiometryCpl()
            self.Cost_flags = Costs()
            self.administration = AdministrationRate()
            self.amorat = AmortizationRate()
            self.acqu = AcquisitionRate()
            self.flags = Flags()
            self.contract_Dto = JsonReader
            self.flags_vector_J = self.flags.gross_premium_flags_vector(tariff=self.contract_Dto.tariff_name())


        def Gross_premium_annuity(self) -> float:
            """
            Maxi formula for the gross  premium annuity
            """
            ### maxi formula needs yet to be adjusted ###
            start_time = time.time()
            Tc1 =(1 + self.administration.gamma_2())
            Tc2= self.present_values.c4_nag_k(deferment_period=self.contract_Dto.deferment_period(),age=self.Biometry.age_shifted(),birth_date= self.contract_Dto.birth_year(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency(),guarantee_time=self.contract_Dto.guarantee_time())
            Tc3= self.present_values.c7_ngax_k(deferment_period=self.contract_Dto.deferment_period(),guarantee_time=self.contract_Dto.guarantee_time(),payment_frequency=self.contract_Dto.payment_contributions_frequency(),age=self.Biometry.age_shifted(),birth_date=self.contract_Dto.birth_year())
            Tc4 = self.present_values.c38a(payment_duration=self.contract_Dto.premium_payment_duration(),age=self.Biometry.age_shifted(),birth_date=self.contract_Dto.birth_year())
            # #Tc5 = self.present_values.c38b(payment_duration=self.contract_Dto.premium_payment_duration(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            Tc6 = self.present_values.c44(deferment_period=self.contract_Dto.deferment_period(),payment_duration=self.contract_Dto.premium_payment_duration(),age=self.Biometry.age_shifted(),birth_date=self.contract_Dto.birth_year())
            Te2b = self.Cost_flags.e2b_asqcosta_z()
            Te15= self.Cost_flags.e_30(payment_duration=self.contract_Dto.premium_payment_duration(),max_provizionsbezug=30)
            # #Te45= self.Cost_flags.e_45()
            # #Te46 = self.Cost_flags.e_46()
            Te30 =self.Cost_flags.e_31a_Rxnt(deferment_period=self.contract_Dto.deferment_period(),age=self.Biometry.age_shifted(),birth_date=self.contract_Dto.birth_year(),payment_duration=self.contract_Dto.premium_payment_duration())
            # #T50= 10490.88*(Tc1*(self.present_values.c2_gax_k(guarantee_time=15,age=75,birth_date=1938,payment_contributions_frequency=12)+self.present_values.c3_ag_k(guarantee_time=15,payment_contributions_frequency=12)))/(1-0.015-0.004)
            #
            num = Tc1 * (Tc2+Tc3) + (0.005 * Tc4) + (0.0 * Tc4) + (0.005 * Tc6)
            den = (1-0.06) * Tc4 - (0.04 * Te15) - (1.05 * Te30)
            Result = 3002.76 * num/den
            #Result = 5785.8 * num / den
            end_time = time.time()
            return Result, end_time-start_time


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

        def barwert_testing(self) -> float:
            ### Barwert-Testing###
            start_time = time.time()
            deferment_period = self.contract_Dto.deferment_period()
            age=self.Biometry.age_shifted()
            birth_date = self.contract_Dto.birth_year()
            payment_contributions_frequency = self.contract_Dto.payment_contributions_frequency()
            guarantee_time = self.contract_Dto.guarantee_time()
            pension_payment_period = self.contract_Dto.pension_payment_period()
            agreed_duration = 2
            e = 10
            pension_dynamic = self.contract_Dto.pension_dynamic()
            payment_duration = self.contract_Dto.premium_payment_duration()
            c0 = self.present_values.c0_nax_k(deferment_period=deferment_period, age=age,birth_date=birth_date,payment_contributions_frequency=payment_contributions_frequency)
            c1 = self.present_values.c1_naxl_k(deferment_period=deferment_period, age=age,birth_date=birth_date,payment_contributions_frequency=payment_contributions_frequency,pension_payment_period=pension_payment_period)
            c2 = self.present_values.c2_gax_k(guarantee_time=guarantee_time,age=age,birth_date=birth_date,payment_contributions_frequency=payment_contributions_frequency)
            c3 = self.present_values.c3_ag_k(guarantee_time=guarantee_time,payment_contributions_frequency=payment_contributions_frequency)
            c4 = self.present_values.c4_nag_k(age=age,birth_date=birth_date, deferment_period=deferment_period, guarantee_time=guarantee_time,payment_contributions_frequency=payment_contributions_frequency)
            c5a = self.present_values.c5a_axn(age=age,birth_date=birth_date, deferment_period=deferment_period)
            c6 = self.present_values.c6_ax_k(payment_frequency=payment_contributions_frequency, age=age,
                                                birth_date=birth_date)
            c7 = self.present_values.c7_ngax_k(deferment_period=deferment_period,guarantee_time=guarantee_time, payment_frequency=payment_contributions_frequency, age=age,birth_date=birth_date)
            c8 = self.present_values.c8_nax_12(deferment_period=deferment_period, age=age, birth_date=birth_date)
            c9 = self.present_values.c9_nag_12(age=age, birth_date=birth_date, deferment_period=deferment_period,
                                              guarantee_time=guarantee_time)
            c10 = self.present_values.c10_ag_12(guarantee_time=guarantee_time)
            c11 = self.present_values.c11_ngax_12(deferment_period=deferment_period, age=age, birth_date=birth_date,
                                                    guarantee_time=guarantee_time)
            c12 = self.present_values.c12_ax_12(age=age, birth_date=birth_date)
            c13 = self.present_values.c13_gax_12(age=age, birth_date=birth_date, guarantee_time=guarantee_time)
            c14 = self.present_values.c14_axl_k(age=age, birth_date=birth_date, agreed_duration=agreed_duration)
            c15 = self.present_values.c15_nAx(deferment_period=deferment_period, age=age, birth_date=birth_date)
            c16 = self.present_values.c16_e0Ax_k(e=e, age=age, birth_date=birth_date,
                                                payment_frequency=payment_contributions_frequency)
            c17 = self.present_values.c17_enAx_k(deferment_period=deferment_period, e=10, age=age,
                                                 birth_date=birth_date, payment_frequency=payment_contributions_frequency)
            c21 = self.present_values.c21_ngaxs_k(pension_dynamic=pension_dynamic,
                                                  payment_frequency=payment_contributions_frequency,
                                                  guarantee_time=guarantee_time, deferment_period=deferment_period,
                                                  age=age, birth_date=birth_date)
            c38a = self.present_values.c38a(payment_duration=payment_duration, age=age, birth_date=birth_date)
            e31a = self.Cost_flags.e_31a_Rxnt(deferment_period=deferment_period, age=age,
                                              birth_date=birth_date, payment_duration=payment_duration)
            end_time = time.time()
            return c0, c1, c2, c3, c4, c5a, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c21, c38a, e31a, end_time - start_time


c0, c1, c2, c3, c4, c5a, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c21, c38a, e31a, timing = Tariff().barwert_testing()

print("c0 for tariff pv example: " + str(c0) + " (Desired value: 15.394247)")
print("c1 for tariff pv example: " + str(c1) + " (Desired value: 8.842316)")
print("c2 for tariff pv example: " + str(c2) + " (Desired value: 26.141518)")
print("c3 for tariff pv example: " + str(c3) + " (Desired value: 4.681005346)")
print("c4 for tariff pv example: " + str(c4) + " (Desired value: 2.70532)")
print("c5a for tariff pv example: " + str(c5a) + " (Desired value: 15.622082)")
print("c6 for tariff pv example: " + str(c6) + " (Desired value: 30.82098735)")
print("c7 for tariff pv example: " + str(c7) + " (Desired value: 12.69427175)")
print("c8 for tariff pv example: " + str(c8) + " (Desired value: 15.394247)")
print("c9 for tariff pv example: " + str(c9) + " (Desired value: 2.7053073653485)")
print("c10 for tariff pv example: " + str(c10) + " (Desired value: 4.681005346)")
print("c11 for tariff pv example: " + str(c11) + " (Desired value: 12.69427175)")
print("c12 for tariff pv example: " + str(c12) + " (Desired value: 30.82098735)")
print("c38a for tariff pv example: " + str(c38a) + " (Desired value: 15.622082)")
print("e31a for tariff pv example: " + str(e31a) + " (Desired value: 0.051903383)")
print("c13 for tariff pv example: " + str(c13) + " (Desired value: 26.14147528)")
print("c14 for tariff pv example: " + str(c14) + " (Desired value: ??? (cpl: 1.9485))")
print("c15 for tariff pv example: " + str(c15) + " (Desired value: 0.00395838)")
print("c16 for tariff pv example: " + str(c16) + " (Desired value: ??? (cpl: 0.023942))")
print("c17 for tariff pv example: " + str(c17) + " (Desired value: ??? (cpl: 0.023942))")
print("c18 for tariff pv example: Disabilities not yet implemented")
print("c19 for tariff pv example: Disabilities not yet implemented")
print("c20 for tariff pv example: Disabilities not yet implemented")
print("c21 for tariff pv example: " + str(c21) + " (Desired value: ??? (cpl: 20.64899))")
print("Runtime: " + str(timing) + " seconds")
print("Gross Premium for example for tariff ARZ/2004: " + str(Tariff().Gross_premium_annuity()) + " (Desired value: 1926.1143368887392)")

