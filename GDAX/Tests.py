import unittest
import GDAX.PublicClient

class TestPublicClient(unittest.TestCase):
    def setUp(self):
        publicClient = GDAX.PublicClient()

    def testGetProducts(self):
        pass

    def testProductOrderBook(self):
        pass

    def testProductTicker(self):
        pass

    def testProductTrades(self):
        pass

    def testProductHistoricalRates(self):
        pass

    def testgetProduct24HrStats(self):
        pass

    def testgetCurrencies(self):
        pass

    def testgetTime(self):
        pass

class TestAuthenticatedClient(unittest.TestCase):
    pass

class TestWebSocketClient(unittest.TestCase):
    pass