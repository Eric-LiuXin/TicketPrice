#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import time
import datetime

from Crawl import Crawl
from Ctrip import Ctrip
import SplunkLog

def Run():
    start_url = Ctrip.StartURL()
    my_crawl = Crawl(start_url)
    try:
        my_crawl.Run()
        price_pannel_list = my_crawl.price_pannel_list
        for price_pannel in price_pannel_list:
            SplunkLog.Save(price_pannel)
    finally:
        my_crawl.Finish()

if __name__=="__main__":
    if(len(sys.argv)!=2 or (sys.argv[1]!='AutoRun')):
        Run()
        print ('If you want auto run it, should input: AutoRun')
    else:
        while True:
            print ("##{0}##Run TicketPrice...".format(datetime.datetime.now()))
            Run()
            time.sleep(60*60*24)
