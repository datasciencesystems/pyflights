# PyFlights

A simple wrapper for the Google Flights search API.

Create a new application in the [Google API Console](https://console.developers.google.com) to obtain an API key.  
Check out the [API documentation](https://developers.google.com/qpx-express/v1/trips/search).


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
    print 'Airline: %s' % results.flight_airline()
    print 'Origin: %s' % results.origin()
    print 'Destination: %s' % results.destination()
    print 'Deparure Time: %s' % results.departure_time()
    print 'Arrival Time: %s' % results.arrival_time()
```

| Parameter   | Description                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| adult_count | The number of passengers that are adults.                                                                                                   |
| origin      | Airport or city IATA designator of the origin.                                                                                              |
| max_price   | Do not return solutions that cost more than this price. The currency is specified in ISO-4217. The format, in regex, is [A-Z]{3}\d+(\.\d+)? |
| destination | Airport or city IATA designator of the destination.                                                                                         |
| date        | Departure date in YYYY-MM-DD format.                                                                                                        |
| solutions   | The number of solutions to return, maximum 500.                                                                                             |
