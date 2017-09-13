#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
class Ctrip():
    @staticmethod
    def StartURL():
        start_url = "http://flights.ctrip.com/booking"
        today = datetime.date.today()
        start_url = start_url + "/BJS-SHA-day-1.html?DDate1=" + str(today)
        return start_url
