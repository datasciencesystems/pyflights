PyFlights
=========

A Python library for the Google Flights search API.

Install
-------

::

    pip install pyflights

Developing
----------

::

    git clone https://github.com/AnthonyBloomer/pyflights.git
    cd pyflights
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Usage
-----

.. code:: python

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
        print 'Sale total: %s' % results.sale_total()
        print 'Flight carrier: %s' % results.flight_carrier()
        print 'Origin: %s' % results.origin()
        print 'Destination: %s' % results.destination()
        print 'Deparure Time: %s' % results.departure_time()
        print 'Arrival Time: %s' % results.arrival_time()

Required Search Parameters
--------------------------

+-----+----------------------------------------------------------------+
| Par | Description                                                    |
| ame |                                                                |
| ter |                                                                |
+=====+================================================================+
| adu | The number of passengers that are adults.                      |
| lt_ |                                                                |
| cou |                                                                |
| nt  |                                                                |
+-----+----------------------------------------------------------------+
| ori | Airport or city IATA designator of the origin.                 |
| gin |                                                                |
+-----+----------------------------------------------------------------+
| max | Do not return solutions that cost more than this price. The    |
| _pr | currency is specified in ISO-4217. The format, in regex, is    |
| ice | [A-Z]{3}:raw-latex:`\d`+(.:raw-latex:`\d`+)?                   |
+-----+----------------------------------------------------------------+
| des | Airport or city IATA designator of the destination.            |
| tin |                                                                |
| ati |                                                                |
| on  |                                                                |
+-----+----------------------------------------------------------------+
| dat | Departure date in YYYY-MM-DD format.                           |
| e   |                                                                |
+-----+----------------------------------------------------------------+
| sol | The number of solutions to return, maximum 500.                |
| uti |                                                                |
| ons |                                                                |
+-----+----------------------------------------------------------------+

Flight
------

The flight class contains the following methods.

+---------+------------------------------------------------------------+
| Method  | Description                                                |
+=========+============================================================+
| sale_to | The total price for all passengers on the trip, in the     |
| tal     | form of a currency followed by an amount, e.g. USD253.35.  |
+---------+------------------------------------------------------------+
| duratio | The duration of the slice in minutes.                      |
| n       |                                                            |
+---------+------------------------------------------------------------+
| booking | The number of seats available in this booking code on this |
| _code_c | segment.                                                   |
| ount    |                                                            |
+---------+------------------------------------------------------------+
| flight_ | The 2-letter IATA airline designator for the segment.      |
| carrier |                                                            |
+---------+------------------------------------------------------------+
| flight_ | The flight number.                                         |
| number  |                                                            |
+---------+------------------------------------------------------------+
| origin  | The leg origin as a city and airport.                      |
+---------+------------------------------------------------------------+
| destina | The leg destination as a city and airport.                 |
| tion    |                                                            |
+---------+------------------------------------------------------------+
| origin_ | The terminal the flight is scheduled to depart from.       |
| termina |                                                            |
| l       |                                                            |
+---------+------------------------------------------------------------+
| origin_ | The terminal the flight is scheduled to arrive at.         |
| destina |                                                            |
| tion    |                                                            |
+---------+------------------------------------------------------------+
| departu | The scheduled departure time of the leg, local to the      |
| re_time | point of departure.                                        |
+---------+------------------------------------------------------------+
| arrival | The scheduled time of arrival at the destination of the    |
| _time   | leg, local to the point of arrival.                        |
+---------+------------------------------------------------------------+
