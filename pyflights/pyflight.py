import requests
from pyflights.objects import Flight

class PyFlight:
    endpoint = 'https://www.googleapis.com/qpxExpress/v1/trips/search?'

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, params):
        req = self._call(params)
        flights = []
        [flights.append(Flight(res)) for res in req['trips']['tripOption']]
        return flights

    def _call(self, params):
        url = self.endpoint + 'key=' + self.api_key
        req = requests.post(url, json={
            'request': {
                'passengers': {
                    'adultCount': params['adult_count']
                },
                'slice': [
                    {
                        'origin': params['origin'],
                        'date': params['date'],
                        'destination': params['destination']
                    }
                ],
                'maxPrice': params['max_price'],
                'solutions': params['solutions']
            }
        })
        print(req.json())
        if not req.status_code == 200:
            errors = req.json()
            error_code = errors['error']['code']
            message = errors['error']['message']
            reason = errors['error']['errors'][0]['reason']
            raise PyFlightException(error_code, reason, message)
        return req.json()


class PyFlightException(Exception):
    def __init__(self, status_code, reason, text):
        self.status_code = status_code
        self.reason = reason
        self.text = text

    def __str__(self):
        return "PyFlights returned an error: %s - %s - %s" % (self.status_code, self.reason, self.text)
