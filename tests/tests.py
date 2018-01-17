import unittest
import datetime
from pyflights import PyFlight


class PyFlightTest(unittest.TestCase):
    def test_search(self):
        today = datetime.date.today()
        # Assume we should find a flight to NYC 4 days from now.
        d = today + datetime.timedelta(days=4)
        flight_api = PyFlight(api_key='')
        search = flight_api.search(params={
            'adult_count': 1,
            'origin': 'DUB',
            'max_price': 'EUR1200',
            'destination': 'NYC',
            'date': str(d),
            'solutions': 1
        })
        self.assertIsNotNone(search)
        first = search[0]
        self.assertEqual(first.origin(), 'DUB')
        self.assertTrue(first.departure_time(), d)
        self.assertTrue(float(first.sale_total()[3:]) <= 1200)
        self.assertIsNotNone(first.sale_total())
        self.assertIsNotNone(first.origin())
        self.assertIsNotNone(first.origin_terminal())
        self.assertIsNotNone(first.destination_terminal())
        self.assertIsNotNone(first.flight_carrier())
        self.assertIsNotNone(first.destination())
        self.assertIsNotNone(first.departure_time())
        self.assertIsNotNone(first.arrival_time())
        self.assertIsNotNone(first.duration())
        self.assertIsNotNone(first.booking_code_count())
        self.assertIsNotNone(first.flight_number())


