from calculationbases.flagsterms.cflags.pv_annuity import PresentValues
from calculationbases.flagsterms.eflags.cost_annuity import Costs
from input.json_reader import JsonReader
from calculationbases.cost.administrationcosts.administration_rate import AdministrationRate
from calculationbases.cost.amortizationcosts.amortization_rate import AmortizationRate
from calculationbases.cost.acquisitioncosts.acquisition_rate import AcquisitionRate
from input.contract import ContractDTO
import time
from calculationbases.flagsterms.mf_annuity_flags import Flags




class Tariff():

        def __init__(self):  # , contract_nr: int):  # ToDo Evaluate if inheritance is the right approach here
            # super().__init__()  # contract_nr=contract_nr)
            self.present_values = PresentValues()  # contract_nr=contract_nr)
            self.Cost_flags =Costs()
            self.administration = AdministrationRate()
            self.amorat = AmortizationRate()
            self.acqu =  AcquisitionRate()
            self.flags = Flags()
            self.contract_Dto = JsonReader

            # self.flags_vector = self.flags.Gross_Premium_flags_vector(tariff= ContractDTO.tariff(self))
            self.flags_vector_J = self.flags.gross_premium_flags_vector(tariff=self.contract_Dto.tariff_name())

        def Gross_premium_annuity(self) -> float:

            """
            Maxi formula for the gross single premium annuity
            """

            ### maxi formula needs yet to be adjusted ###
            Start_time= time.time()
            Tc1 =(1 + self.administration.gamma_2())
            Tc2=self.flags_vector_J[4] * self.present_values.c4_nag_k(deferment_period=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date= self.contract_Dto.birth_year(),payment_contributions_frequency=self.contract_Dto.payment_contributions_frequency(),guarantee_time=self.contract_Dto.guarantee_time())
            Tc3= self.flags_vector_J[8]* self.present_values.c7_ngax_k(deferment_period=self.contract_Dto.deferment_period(),guarantee_time=self.contract_Dto.guarantee_time(),payment_frequency=self.contract_Dto.payment_contributions_frequency(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            Tc4 =self.flags_vector_J[39]* self.present_values.c38a(payment_duration=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            Tc5 =self.flags_vector_J[39]* self.present_values.c38b(payment_duration=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            Tc6 =self.flags_vector_J[46]* self.present_values.c44(deferment_period=self.contract_Dto.deferment_period(),payment_duration=self.contract_Dto.deferment_period(),age=self.contract_Dto.actuarial_age(),birth_date=self.contract_Dto.birth_year())
            Te2b = self.Cost_flags.e2b_asqcosta_z()
            Te12 =1
            Te13 =1
            Te15= self.Cost_flags.e_30(payment_duration=self.contract_Dto.deferment_period(), max_provizionsbezug=100)
            Te45= self.Cost_flags.e_45()
            Te46 = self.Cost_flags.e_46()

            num = Tc1*(Tc2+Tc3)+self.amorat.alpha_gamma()+self.administration.gamma_12()+Tc4 + self.administration.gamma_11() * Tc4
            den= (1-self.administration.beta())* Tc4 - self.acqu.alpha_Z()+ self.Cost_flags.e_30(payment_duration=self.contract_Dto.deferment_period(), Max_provizionsbezug=100)+self.acqu.alpha_Z()+ self.Cost_flags.e_30(payment_duration=self.contract_Dto.deferment_period(), Max_provizionsbezug=100)
            Result = num/den

            end_time= time.time()
            return Result , end_time-Start_time


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

print("Gross Premium for example tariff: " + str(Tariff().Gross_premium_annuity()) + " (Desired value: 2.082159965161852)")
