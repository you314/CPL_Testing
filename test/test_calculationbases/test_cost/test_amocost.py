import unittest
from unittest.mock import MagicMock

from calculationengine.tariff import Tariff


class UnitTestBiometryCpl(unittest.TestCase):
    def setUp(self):
        self.contract_nr = 1234
        self.tariff = Tariff(self.contract_nr)