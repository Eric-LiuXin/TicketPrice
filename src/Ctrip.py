#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from builtins import list
class Ctrip():
    City = {
         'BeiJing' : 'BJS', 'ShangHai' : 'SHA',
         'ChiFeng' : 'CIF', 'DaLian' : 'DLC'
    }
    @staticmethod
    def StartURL():
        start_url = "http://flights.ctrip.com/booking"
        today = datetime.date.today()
        start_urls = list()
        [start_urls.append(start_url + "/{0}-day-1.html?DDate1=".format(Ctrip.City[from_city] \
            + "-" + Ctrip.City[to_city]) + str(today)) \
            for from_city in Ctrip.City for to_city in Ctrip.City \
            if from_city != to_city ]
        return start_urls

if __name__=="__main__":
    start_urls = Ctrip.StartURL()
    print (start_urls)