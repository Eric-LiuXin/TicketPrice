import datetime
class PricePannel:
    def __init__(self):
        self.company = None
        self.flight = None
        self.aircraft_type = None
        self.takeoff_city = None
        self.arrival_city = None
        self.departure_time =None
        self.price = None
        self.query_time = datetime.date.today()
