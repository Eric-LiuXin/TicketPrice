#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from PricePannel import PricePannel
import datetime
import re

class Crawl:
    def __init__(self, start_url):
        self.city_list = ['上海(SHA)', '北京(BJS)', '大连(DLC)', '赤峰(CIF)']
        self.date_list = [str(datetime.date.today() + datetime.timedelta(days=key)) for key in range(0, 30)]
        self.price_pannel_list = list()
        self.driver = webdriver.PhantomJS()
        self.driver.get(start_url)
    
    def GotoPage(self, depart_city, arrive_city, date):
        self.driver.find_element_by_id('DCityName1').send_keys(depart_city)
        self.driver.find_element_by_id('ACityName1').send_keys(arrive_city)
        self.driver.find_element_by_id('DDate1').send_keys(date)
        
        self.driver.find_element_by_id('btnReSearch').click()
        
    def DateParse(self, depart_city, arrive_city, date):
        self.GotoPage(depart_city, arrive_city, date)
        elements = self.driver.find_elements_by_class_name("J_header_row")
        for element in elements:
            price_pannel = PricePannel()
            price_pannel.air_route = depart_city + "-" + arrive_city
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
    
    def Run(self):         
        [self.DateParse(depart_city,arrive_city,date) \
                for depart_city in self.city_list \
                for arrive_city in self.city_list \
                for date in self.date_list \
                if depart_city != arrive_city]
        
    def Finish(self):
        self.driver.quit()