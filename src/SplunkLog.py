#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
TO_ADDRESS = ('localhost', 514)
LOG = '''Flight information:AirRoute = {0}, Company = {1}, \
Flight = {2}, AircraftType = {3}, TakeoffAirport = {4}, \
ArrivalAirport = {5}, DepartureTime = {6}, Price = {7}, \
QueryTime = {8}\
'''
def Save(price_pannel):
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_str = LOG.format(\
                price_pannel.air_route, price_pannel.company, \
                price_pannel.flight,price_pannel.aircraft_type, price_pannel.takeoff_airport, \
                price_pannel.arrival_airport, price_pannel.departure_time, price_pannel.price,\
                price_pannel.query_time\
            )
    udp_client.sendto(("%s" %(my_str)).encode(), TO_ADDRESS)
    #print (my_str)