from calculationbases.biometry.cpl_bio import BiometryCpl
from calculationbases.interest.interest_rate import Interest
from input.contract import ContractDTO


class Costs:

    def __init__(self, contract_nr):
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        self.biometry_cpl = BiometryCpl(contract_nr=contract_nr)
        self.Interest = Interest()


class Terms:

    def __init__(self, contract_nr):
        self.contractDTO = ContractDTO(contract_nr=contract_nr)
        self.biometry_cpl = BiometryCpl(contract_nr=contract_nr)
        self.Interest = Interest()

