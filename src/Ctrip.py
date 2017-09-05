import datetime
class Ctrip():
    City = {
        'BeiJing' : 'BJS', 'ShangHai' : 'SHA',
        'ChiFeng' : 'CIF', 'DaLian' : 'DLC'
    }
    @staticmethod
    def QueryURL():
        url_list = list()
        start_urls = "http://flights.ctrip.com/booking"
        today = datetime.date.today()
        for air_line in {\
                         Ctrip.City[from_city] + "-" + Ctrip.City[to_city] \
                         for from_city in Ctrip.City for to_city in Ctrip.City \
                         if from_city != to_city \
                        }:
            url = start_urls + "/{0}-day-1.html?DDate1=".format(air_line)
            [url_list.append(url + str(today + datetime.timedelta(days=wft))) for wft in range(0, 30)]
        
        return url_list

if __name__=="__main__":
    _list = Ctrip.QueryURL()
    for url in _list:
        print (url)
