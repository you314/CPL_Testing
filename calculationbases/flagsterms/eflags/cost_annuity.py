import calculationbases.biometry.cpl_bio as cpl_bio
from calculationbases.interest.interest_rate import Interest
from input.json_reader import JsonReader
from calculationbases.cost.acquisitioncosts.acquisition_rate import AcquisitionRate
from calculationbases.cost.administrationcosts.administration_rate import AdministrationRate
from calculationbases.flagsterms.cflags.pv_annuity import PresentValues


class Costs:
    """
    The costs class is a summary of all flags corresponding to costs in the maxi formula framework: e0 - e98.
    We hereby copy the current status of CPL.
    """

    def __init__(self):
        self.contractDTO = JsonReader
        self.biometry_cpl = cpl_bio.BiometryCpl()
        self.Interest = Interest()
        self.acuisitioncost= AcquisitionRate()
        self.adminiscost = AdministrationRate()
        self.pv = PresentValues()

    ### general functions ###

    def alpha_z(self) -> float:
        return 0

    def alpha_1(self) -> float:
        return 0.

    def alpha_2(self) -> float:
        return 0.

    ### e flags ###

    def e0_1k(self, payment_frequency) -> float:
        return 1./payment_frequency

    def e1_12k(self) -> float:
        return 1./12.

    def e2a_asqcosta_z(self) -> float:
        return self.acuisitioncost.alpha_Z()

    def e2b_asqcosta_z(self) -> float:
        return self.acuisitioncost.alpha_Z()

    def e3_asqcosta_1(self) -> float:
        return self.acuisitioncost.alpha_1()

    def e4_asqcosta_2(self) -> float:
        return self.alpha_2()

    def e_12(self):
        value= 1
        return value

    def e_13(self):
        value= 1
        return value

    def e_30(self, payment_duration, max_provizionsbezug):
        value = min(payment_duration, max_provizionsbezug)
        return value


    def e_31a_Rxnt(self,deferment_period,age,birth_date,payment_duration):

        result = self.pv.c51(deferment_period=payment_duration, age=age, birth_date=birth_date) + \
                 payment_duration * self.pv.c15_nAx(deferment_period=deferment_period-payment_duration, age=age+payment_duration, birth_date=birth_date) \
                 * (self.pv.v()[0] ** payment_duration) * self.pv.n_p_x_V(age=age,birth_date=birth_date)[payment_duration]
        return result


    def e_45(self):
        return self.adminiscost.gamma_11()
    def e_46(self):
        return self.adminiscost.gamma_12()





