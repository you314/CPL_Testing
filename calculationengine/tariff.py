from calculationbases.flagsterms.cflags.pv_annuity import PresentValues
from calculationbases.flagsterms.eflags.cost_annuity import Costs
from input.json_reader import JsonReader
from calculationbases.cost.administrationcosts.administration_rate import AdministrationRate
from calculationbases.cost.amortizationcosts.amortization_rate import AmortizationRate
from calculationbases.cost.acquisitioncosts.acquisition_rate import AcquisitionRate
import time
from calculationbases.flagsterms.mf_annuity_flags import Flags




class Tariff():

        def __init__(self):
            self.present_values = PresentValues()
            self.Cost_flags =Costs()
            self.administration = AdministrationRate()
            self.amorat = AmortizationRate()
            self.acqu =  AcquisitionRate()
            self.flags = Flags()
            self.contract_Dto = JsonReader
            self.flags_vector_J = self.flags.gross_premium_flags_vector(tariff=self.contract_Dto.tariff_name())

        def Gross_premium_annuity(self) -> float:

            """
            Maxi formula for the gross  premium annuity
            """

            ### maxi formula needs yet to be adjusted ###
            # start_time = time.time()
            # Tc1 =(1 + self.administration.gamma_2())
            # Tc2= self.present_values.c4_nag_k(deferment_period=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date= self.contract_Dto.birth_year(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency(),guarantee_time=self.contract_Dto.guarantee_time())
            # Tc3= self.present_values.c7_ngax_k(deferment_period=self.contract_Dto.deferment_period(),guarantee_time=self.contract_Dto.guarantee_time(),payment_frequency=self.contract_Dto.payment_contributions_frequency(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            # Tc4 = self.present_values.c38a(payment_duration=self.contract_Dto.premium_payment_duration(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            # #Tc5 = self.present_values.c38b(payment_duration=self.contract_Dto.premium_payment_duration(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            # Tc6 = self.present_values.c44(deferment_period=self.contract_Dto.deferment_period(),payment_duration=self.contract_Dto.premium_payment_duration(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            # #Te2b = self.Cost_flags.e2b_asqcosta_z()
            # Te15= self.Cost_flags.e_30(payment_duration=self.contract_Dto.premium_payment_duration(),max_provizionsbezug=30)
            # #Te45= self.Cost_flags.e_45()
            # #Te46 = self.Cost_flags.e_46()
            # Te30 =self.Cost_flags.e_31a_Rxnt(deferment_period=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year(),payment_duration=self.contract_Dto.premium_payment_duration())
            # #T50= 10490.88*(Tc1*(self.present_values.c2_gax_k(guarantee_time=15,age=75,birth_date=1938,payment_contributions_frequency=12)+self.present_values.c3_ag_k(guarantee_time=15,payment_contributions_frequency=12)))/(1-0.015-0.004)
            #
            # num = Tc1 * (Tc2+Tc3) + (0.005 * Tc4) + (0.0 * Tc4) + (0.005 * Tc6)
            # den = (1-0.06) * Tc4 - (0.04 * Te15) - (1.05 * Te30)
            # Result = 1000 * num/den
            # end_time = time.time()
            # return Result, end_time-start_time


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
            c0 = self.present_values.c0_nax_k(deferment_period=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date= self.contract_Dto.birth_year(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency())
            c1 = self.present_values.c1_naxl_k(deferment_period=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date= self.contract_Dto.birth_year(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency(),pension_payment_period=self.contract_Dto.pension_payment_period())
            c2 = self.present_values.c2_gax_k(guarantee_time=self.contract_Dto.guarantee_time(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency())
            c3 = self.present_values.c3_ag_k(guarantee_time=self.contract_Dto.guarantee_time(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency())
            # #Tc5 = self.present_values.c38b(payment_duration=self.contract_Dto.premium_payment_duration(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            # Tc6 = self.present_values.c44(deferment_period=self.contract_Dto.deferment_period(),payment_duration=self.contract_Dto.premium_payment_duration(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            # #Te2b = self.Cost_flags.e2b_asqcosta_z()
            # Te15= self.Cost_flags.e_30(payment_duration=self.contract_Dto.premium_payment_duration(),max_provizionsbezug=30)
            # #Te45= self.Cost_flags.e_45()
            # #Te46 = self.Cost_flags.e_46()
            # Te30 =self.Cost_flags.e_31a_Rxnt(deferment_period=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year(),payment_duration=self.contract_Dto.premium_payment_duration())
            # #T50= 10490.88*(Tc1*(self.present_values.c2_gax_k(guarantee_time=15,age=75,birth_date=1938,payment_contributions_frequency=12)+self.present_values.c3_ag_k(guarantee_time=15,payment_contributions_frequency=12)))/(1-0.015-0.004)
            #
            # num = Tc1 * (Tc2+Tc3) + (0.005 * Tc4) + (0.0 * Tc4) + (0.005 * Tc6)
            # den = (1-0.06) * Tc4 - (0.04 * Te15) - (1.05 * Te30)
            # Result = 1000 * num/den
            end_time = time.time()
            return c0, c1, c2, c3, end_time - start_time


c0, c1, c2, c3, timing = Tariff().barwert_testing()
print("c0 for tariff pv example: " + str(c0) + " (Desired value: 15.394247) " + "in " + str(timing) + " seconds" )
print("c1 for tariff pv example: " + str(c1) + " (Desired value: 8.842316) " + "in " + str(timing) + " seconds")
print("c2 for tariff pv example: " + str(c2) + " (Desired value: 26.41518) " + "in " + str(timing) + " seconds")
print("c3 for tariff pv example: " + str(c3) + " (Desired value: 4.681005) " + "in " + str(timing) + " seconds")
#print("Gross Premium for example for tariff ARZ/2004: " + str(Tariff().Gross_premium_annuity()) + " (Desired value: 1926.1143368887392)")

