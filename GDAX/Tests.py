import unittest
import GDAX.PublicClient

class TestPublicClient(unittest.TestCase):
    def setUp(self):
        publicClient = GDAX.PublicClient()

    def testClient(self):
        pass

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

    def testGetProduct24HrStats(self):
        pass

    def testGetCurrencies(self):
        pass

    def testGetTime(self):
        pass

class TestAuthenticatedClient(unittest.TestCase):
    def setUp(self):
        authenticatedClient = GDAX.AuthenticatedClient()

    def testClient(self):
        pass

    def testGetAccount(self):
        pass

    def testGetAccounts(self):
        pass

    def testGetAccountHistory(self):
        pass

    def testHistoryPagination(self):
        pass

    def testGetAccountHolds(self):
        pass

    def testHoldsPagination(self):
        pass

    def testBuy(self):
        pass

    def testSell(self):
        pass

    def testCancelOrder(self):
        pass

    def testCancelAll(self):
        pass

    def testGetOrder(self):
        pass

    def testGetOrders(self):
        pass

    def testPaginateOrders(self):
        pass

    def testGetFills(self):
        pass

    def testPaginateFills(self):
        pass

    def testDeposit(self):
        pass

    def testWithdraw(self):
        pass

    def testGetPaymentMethods(self):
        pass

    def testGetCoinbaseAccounts(self):
        pass

    def testCreateReport(self):
        pass

    def testGetReport(self):
        pass

    def testGetTrailingVolume(self):
        pass

class TestWebSocketClient(unittest.TestCase):
    pass

class TestGdaxAuth(unittest.TestCase):
    pass