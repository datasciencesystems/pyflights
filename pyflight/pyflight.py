import requests

from models import Flight


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
        return req.json()
