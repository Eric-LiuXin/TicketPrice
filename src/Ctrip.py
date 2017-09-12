#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
class Ctrip():
    City = {
        'BeiJing' : 'BJS', 'ShangHai' : 'SHA',
        'ChiFeng' : 'CIF', 'DaLian' : 'DLC'
    }
    @staticmethod
    def QueryURL():
        url_list = dict()
        start_urls = "http://flights.ctrip.com/booking"
        today = datetime.date.today()
        for air_line in {\
                         Ctrip.City[from_city] + "-" + Ctrip.City[to_city] \
                         for from_city in Ctrip.City for to_city in Ctrip.City \
                         if from_city != to_city \
                        }:
            url = start_urls + "/{0}-day-1.html?DDate1=".format(air_line)
            url_list[air_line] = dict()
            for key in range(0, 30):
                departure_time = str(today + datetime.timedelta(days=key))
                url_list[air_line][departure_time] = url + departure_time
        return url_list

if __name__=="__main__":
    url_list = Ctrip.QueryURL()
    for key in url_list:
        air_line = url_list[key]
        for departure_time in air_line:
            url = air_line[departure_time]
            print (url)