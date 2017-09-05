import sys
import time
import datetime

from Crawl import Crawl
from Ctrip import Ctrip
import SplunkLog

def Run():
    url_list = Ctrip.QueryURL()
    print(url_list)
    for url in url_list:
        my_crawl = Crawl(url)
        price_pannel_list = my_crawl.start()
        for price_pannel in price_pannel_list:
            SplunkLog.Save(price_pannel)

if __name__=="__main__":
    if(len(sys.argv)!=2 or (sys.argv[1]!='AutoRun')):
        Run()
        print ('If you want auto run it, should input: AutoRun')
    else:
        while True:
            print ("##{0}##Run TicketPrice...".format(datetime.datetime.now()))
            Run()
            time.sleep(60*60*24)
