class Flight(object):
    def __init__(self, flight_data):
        self.flight_data = flight_data

    def sale_total(self):
        return self.flight_data['saleTotal']

    def duration(self):
        return self.flight_data['slice'][0]['duration']

    def booking_code_count(self):
        return self.flight_data['slice'][0]['segment'][0]['bookingCodeCount']

    def flight_carrier(self):
        return self.flight_data['slice'][0]['segment'][0]['flight']['carrier']

    def flight_number(self):
        return self.flight_data['slice'][0]['segment'][0]['flight']['number']

    def origin(self):
        return self.flight_data['slice'][0]['segment'][0]['leg'][0]['origin']

    def destination(self):
        return self.flight_data['slice'][0]['segment'][0]['leg'][0]['destination']

    def origin_terminal(self):
        return self.flight_data['slice'][0]['segment'][0]['leg'][0]['originTerminal']

    def destination_terminal(self):
        return self.flight_data['slice'][0]['segment'][0]['leg'][0]['destinationTerminal']

    def departure_time(self):
        return self.flight_data['slice'][0]['segment'][0]['leg'][0]['departureTime']

    def arrival_time(self):
        return self.flight_data['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
