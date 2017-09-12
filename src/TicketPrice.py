#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
import datetime

from Crawl import Crawl
from Ctrip import Ctrip
import SplunkLog
import random

def Run():
    url_list = Ctrip.QueryURL()
    for air_line in url_list:
        for departure_time in url_list[air_line]:
            url = url_list[air_line][departure_time]
            my_crawl = Crawl(air_line, departure_time, url)
            price_pannel_list = my_crawl.start()
            for price_pannel in price_pannel_list:
                SplunkLog.Save(price_pannel)
                n_time = random.uniform(1, 10)
                time.sleep(n_time*10)

if __name__=="__main__":
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    if(len(sys.argv)!=2 or (sys.argv[1]!='AutoRun')):
        Run()
        print ('If you want auto run it, should input: AutoRun')
    else:
        while True:
            print ("##{0}##Run TicketPrice...".format(datetime.datetime.now()))
            Run()
            time.sleep(60*60*24)
