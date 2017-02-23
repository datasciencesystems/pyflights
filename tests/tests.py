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
        self.assertEqual(search[0].origin(), 'DUB')
        self.assertTrue(search[0].departure_time(), d)
        self.assertTrue(float(search[0].sale_total()[3:]) <= 1200)
