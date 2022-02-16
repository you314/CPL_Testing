import CPLTesting.CalculationBases.biometry.cpl_bio as cpl_bio
from CPLTesting.CalculationBases.Interest.interest_rate import Interest
from CPLTesting.input.contract import ContractDTO


class Costs:
    """
    The costs class is a summary of all flags corresponding to costs in the maxi formula framework: e0 - e98.
    We hereby copy the current status of CPL.
    """

    def __init__(self, contract_nr):
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        self.biometry_cpl = cpl_bio.BiometryCpl(contract_nr=contract_nr)
        self.Interest = Interest()

    ### general functions ###

    def alpha_z(self) -> float:
        return 0.

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
        return self.alpha_z()

    def e2b_asqcosta_z(self) -> float:
        return self.alpha_z()

    def e3_asqcosta_1(self) -> float:
        return self.alpha_1()

    def e4_asqcosta_2(self) -> float:
        return self.alpha_2()