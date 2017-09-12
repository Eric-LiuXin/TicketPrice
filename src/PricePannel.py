#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
class PricePannel:
    def __init__(self):
        self.air_route = None
        self.company = None
        self.flight = None
        self.aircraft_type = None
        self.takeoff_airport = None
        self.arrival_airport = None
        self.departure_time = None
        self.price = None
        self.query_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
