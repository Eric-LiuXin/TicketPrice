#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from PricePannel import PricePannel
import datetime
import re
import time
LOG = '''Flight information:AirRoute = {0}, Company = {1}, \
Flight = {2}, AircraftType = {3}, TakeoffAirport = {4}, \
ArrivalAirport = {5}, DepartureTime = {6}, Price = {7}, \
QueryTime = {8}\
'''
class Crawl:
    def __init__(self, start_urls):
        self.date_list = [str(datetime.date.today() + datetime.timedelta(days=key)) for key in range(0, 30)]
        self.price_pannel_list = list()
        self.driver = webdriver.PhantomJS()
        self.driver.set_page_load_timeout(10) 
        self.start_urls = start_urls
        self.scroll_js="document.body.scrollTop=100000"
        self.depart_city_js = 'return document.getElementById("DCityName1").value'
        self.arrive_city_js = 'return document.getElementById("ACityName1").value'
    
    def GotoPage(self, date):
        data_js = "document.getElementById(\"DDate1\").value=\"{0}\"".format(date)
        self.driver.execute_script(data_js)
        self.driver.find_element_by_id('btnReSearch').click()
        for i in range(10):
            self.driver.execute_script(self.scroll_js)
            time.sleep(2)
        
    def DateParse(self, date):
        self.GotoPage(date)
        elements = self.driver.find_elements_by_class_name("J_header_row")
        print (len(elements))
        for element in elements:
            try:
                price_pannel = PricePannel()
                price_pannel.air_route = self.depart_city + "-" + self.arrive_city
                flight_company_element = element.find_element_by_class_name("logo")
                arr = flight_company_element.text.split('\n')
                price_pannel.company = arr[0]
                price_pannel.flight = arr[1]
                price_pannel.aircraft_type = arr[2]
                                
                right_element = element.find_element_by_class_name("right")
                arr = right_element.text.split('\n')
                price_pannel.departure_time = date
                price_pannel.takeoff_airport = arr[1]
                    
                left_element = element.find_element_by_class_name("left")
                arr = left_element.text.split('\n')
                price_pannel.arrival_airport = arr[1]
                        
                price_element = element.find_element_by_class_name("price")
                price_pannel.price = re.sub(r'\D', "", price_element.text)
                
                self.price_pannel_list.append(price_pannel)
            except:
                continue
    
    def Run(self):
        for url in self.start_urls:
            self.driver.get(url)
            self.depart_city = self.driver.execute_script(self.depart_city_js)
            self.arrive_city = self.driver.execute_script(self.arrive_city_js)
            for date in self.date_list:
                self.DateParse(date)
        
    def Finish(self):
        self.driver.quit()
