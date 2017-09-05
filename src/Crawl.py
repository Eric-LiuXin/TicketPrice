from selenium import webdriver
from PricePannel import PricePannel
import re

class Crawl:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.PhantomJS()
    
    def start(self):
        try:
            self.driver.get(self.url)
            price_pannel_list = list()
            elements = self.driver.find_elements_by_class_name("J_header_row")
            for element in elements:
                price_pannel = PricePannel()
                flight_company_element = element.find_element_by_class_name("logo")
                arr = flight_company_element.text.split('\n')
                price_pannel.company = arr[0]
                price_pannel.flight = arr[1]
                price_pannel.aircraft_type = arr[2]
                
                right_city_element = element.find_element_by_class_name("right")
                arr = right_city_element.text.split('\n')
                price_pannel.departure_time = arr[0]
                price_pannel.takeoff_city = arr[1]
                
                left_city_element = element.find_element_by_class_name("left")
                arr = left_city_element.text.split('\n')
                price_pannel.arrival_city = arr[1]
                    
                price_element = element.find_element_by_class_name("price")
                price_pannel.price = re.sub(r'\D', "", price_element.text)
                
                price_pannel_list.append(price_pannel)
            print(len(price_pannel_list))
        finally:
            self.driver.quit()
            return price_pannel_list
