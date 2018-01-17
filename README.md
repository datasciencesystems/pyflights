# PyFlights

A Python wrapper for the Google QPX Express Search API.

**Note: The QPX Express API service will end on April 10, 2018. [Click here for more information.](https://developers.google.com/qpx-express/faq#EndOfServiceFAQs)**
 
Check out the [API documentation](https://developers.google.com/qpx-express/v1/trips/search).


## Install

```
pip install pyflights
```

## Developing 

```
git clone https://github.com/AnthonyBloomer/pyflights.git
cd pyflights
virtualenv env
source env/bin/activate
pip install -r requirements.txt
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
        'date': 'enter departure date here',
        'solutions': 1
})

for results in search:
    print('Sale total: %s' % results.sale_total())
    print('Flight carrier: %s' % results.flight_carrier())
    print('Origin: %s' % results.origin())
    print('Destination: %s' % results.destination())
    print('Deparure Time: %s' % results.departure_time())
    print('Arrival Time: %s' % results.arrival_time())
```

## Required Search Parameters

| Parameter   | Description                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| adult_count | The number of passengers that are adults.                                                                                                   |
| origin      | Airport or city IATA designator of the origin.                                                                                              |
| max_price   | Do not return solutions that cost more than this price. The currency is specified in ISO-4217. The format, in regex, is [A-Z]{3}\d+(\.\d+)? |
| destination | Airport or city IATA designator of the destination.                                                                                         |
| date        | Departure date in YYYY-MM-DD format.                                                                                                        |
| solutions   | The number of solutions to return, maximum 500.                                                                                             |

## Flight

The flight class contains the following methods.

| Method             | Description                                                                                                      |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| sale_total         | The total price for all passengers on the trip, in the form of a currency followed by an amount, e.g. USD253.35. |
| duration           | The duration of the slice in minutes.                                                                            |
| booking_code_count | The number of seats available in this booking code on this segment.                                              |
| flight_carrier     | The 2-letter IATA airline designator for the segment.                                                            |
| flight_number      | The flight number.                                                                                               |
| origin             | The leg origin as a city and airport.                                                                            |
| destination        | The leg destination as a city and airport.                                                                       |
| origin_terminal    | The terminal the flight is scheduled to depart from.                                                             |
| origin_destination | The terminal the flight is scheduled to arrive at.                                                               |
| departure_time     | The scheduled departure time of the leg, local to the point of departure.                                        |
| arrival_time       | The scheduled time of arrival at the destination of the leg, local to the point of arrival.                      |
