import unittest
import GDAX.PublicClient
import datetime

TEST_PRODUCT_ID = 'BTC-USD'


def validate_ISO_timestamp(string):
    format_string = '%Y-%m-%dT%H:%M:%S.%fZ'
    if datetime.datetime.strptime(string, format_string):
        return True
    else:
        return False


class TestPublicClient(unittest.TestCase):
    def setUp(self):
        self.publicClient = GDAX.PublicClient()

    def testClient(self):
        pass

    def testGetProducts(self):
        results = self.publicClient.getProducts()
        print(results)
        trunc_error_message = "value has too few digits after decimal, possible truncation error"
        for result in results:
            self.assertEqual(result['base_min_size'][::-1].find('.'), 2, msg=trunc_error_message)
            self.assertEqual(result['base_max_size'][::-1].find('.'), 2, msg=trunc_error_message)
            self.assertEqual(result['quote_increment'][::-1].find('.'), 8, msg=trunc_error_message)

        test = "2014-11-06T10:34:47.123456Z"
        print(validate_ISO_timestamp(test))

    def testProductOrderBook(self):
        pass

    def testProductTicker(self):
        results = self.publicClient.getProductTicker(product=TEST_PRODUCT_ID)

        trunc_error_message = "value has too few digits after decimal, possible truncation error"
        self.assertEqual(results['ask'][::-1].find('.'), 2, msg=trunc_error_message)
        self.assertEqual(results['bid'][::-1].find('.'), 2, msg=trunc_error_message)
        self.assertEqual(results['price'][::-1].find('.'), 8, msg=trunc_error_message)
        self.assertEqual(results['volume'][::-1].find('.'), 8, msg=trunc_error_message)

    def testProductTrades(self):
        pass

    def testProductHistoricalRates(self):
        pass

    def testGetProduct24HrStats(self):
        results = self.publicClient.getProduct24HrStats(product=TEST_PRODUCT_ID)

        key_is_missing_message = "response appears to be incomplete, key missing"
        self.assertTrue('open' in results, msg=key_is_missing_message)
        self.assertTrue('high' in results, msg=key_is_missing_message)
        self.assertTrue('low' in results, msg=key_is_missing_message)
        self.assertTrue('last' in results, msg=key_is_missing_message)
        self.assertTrue('volume_30day' in results, msg=key_is_missing_message)
        self.assertTrue('volume' in results, msg=key_is_missing_message)

        value_is_missing_message = "response appears to be incomplete, value missing"
        self.assertTrue(results['open'], msg=value_is_missing_message)
        self.assertTrue(results['high'], msg=value_is_missing_message)
        self.assertTrue(results['low'], msg=value_is_missing_message)
        self.assertTrue(results['last'], msg=value_is_missing_message)
        self.assertTrue(results['volume_30day'], msg=value_is_missing_message)
        self.assertTrue(results['volume'], msg=value_is_missing_message)

        trunc_error_message = "value has too few digits after decimal, possible truncation error"
        self.assertEqual(results['open'][::-1].find('.'), 8, msg=trunc_error_message)
        self.assertEqual(results['high'][::-1].find('.'), 8, msg=trunc_error_message)
        self.assertEqual(results['low'][::-1].find('.'), 8, msg=trunc_error_message)
        self.assertEqual(results['last'][::-1].find('.'), 8, msg=trunc_error_message)
        self.assertEqual(results['volume_30day'][::-1].find('.'), 8, msg=trunc_error_message)
        self.assertEqual(results['volume'][::-1].find('.'), 8, msg=trunc_error_message)

    def testGetCurrencies(self):
        pass

    def testGetTime(self):
        pass


class TestAuthenticatedClient(unittest.TestCase):
    # def setUp(self):
    #     authenticatedClient = GDAX.AuthenticatedClient()

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
