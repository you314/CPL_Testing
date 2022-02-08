import unittest
from unittest.mock import MagicMock

from calculationengine.tariff import Tariff


class UnitTestTariff(unittest.TestCase):
    def setUp(self):
        self.contract_nr = 1234
        self.tariff = Tariff(self.contract_nr)

    def test_net_premium(self):
        self.assertEqual(self.tariff.net_premium_annuity(), 21.51667818974244)

    def test_net_premium_annuity_calls_PresentValues_aeg(self):
        self.tariff.present_values.aeg = MagicMock()
        self.tariff.net_premium_annuity()
        self.tariff.present_values.aeg.assert_called_once_with(guarantee_time=4)

    def test_net_premium_annuity_calls_PresentValues_aegk(self):
        self.tariff.present_values.aegk = MagicMock()
        self.tariff.net_premium_annuity()
        self.tariff.present_values.aegk.assert_called_once_with(guarantee_time=4, k=2)

    def test_net_premium_annuity_calls_PresentValues_n_m_a_x(self):
        self.tariff.present_values.n_m_a_x = MagicMock()
        self.tariff.net_premium_annuity()
        self.tariff.present_values.n_m_a_x.assert_called_once_with(deferment_period=5, m=2, age=61, birth_date=1960)
