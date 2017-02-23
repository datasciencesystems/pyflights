# PyFlights

A simple wrapper for the Google Flights Search API.

## Install

```
pip install pyflights
```

## Usage

```python
from pyflights import PyFlight

flight = PyFlight(api_key='your_api_key')

search = flight.search(params={
        'adult_count': 1,
        'origin': 'DUB',
        'max_price': 'EUR500',
        'destination': 'GDN',
        'date': '2017-02-23',
        'solutions': 1
})

for results in search:
    print 'Sale total: %s' % results.sale_total()
    print 'Origin: %s' % results.origin()
    print 'Destination: %s' % results.destination()
    print 'Deparure Time: %s' % results.departure_time()
    print 'Arrival Time: %s' % results.arrival_time()
```
