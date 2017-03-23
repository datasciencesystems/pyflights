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

        for results in search:
            print 'Sale total: %s' % results.sale_total()
            print 'Origin: %s' % results.origin()
            print 'Origin Terminal: %s' % results.origin_terminal()
            print 'Destination Terminal: %s' % results.destination_terminal()
            print 'Carrier: %s' % results.flight_carrier()
            print 'Destination: %s' % results.destination()
            print 'Departure Time: %s' % results.departure_time()
            print 'Arrival Time: %s' % results.arrival_time()
            print 'Duration: %s' % results.duration()
            print 'Booking Code Count: %s' % results.booking_code_count()
            print 'Flight number: %s' % results.flight_number()

