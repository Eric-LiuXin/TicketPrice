#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from PricePannel import PricePannel
import re

class Crawl:
    def __init__(self, air_route, departure_time, url):
        self.url = url
        self.air_route = air_route
        self.departure_time = departure_time
        self.driver = webdriver.PhantomJS()
    
    def start(self):
        try:
            self.driver.get(self.url)
            price_pannel_list = list()
            elements = self.driver.find_elements_by_class_name("J_header_row")
            for element in elements:
                price_pannel = PricePannel()
                price_pannel.air_route = self.air_route
                flight_company_element = element.find_element_by_class_name("logo")
                arr = flight_company_element.text.split('\n')
                price_pannel.company = arr[0]
                price_pannel.flight = arr[1]
                price_pannel.aircraft_type = arr[2]
                
                right_element = element.find_element_by_class_name("right")
                arr = right_element.text.split('\n')
                price_pannel.departure_time = self.departure_time
                price_pannel.takeoff_airport = arr[1]
                
                left_element = element.find_element_by_class_name("left")
                arr = left_element.text.split('\n')
                price_pannel.arrival_airport = arr[1]
                    
                price_element = element.find_element_by_class_name("price")
                price_pannel.price = re.sub(r'\D', "", price_element.text)
                
                price_pannel_list.append(price_pannel)
        finally:
            self.driver.quit()
            return price_pannel_list
