'''
Created on Aug 12, 2015

@author: sadhna01
'''
'''
Created on Aug 12, 2015

@author: sahil.singla01
'''

class Flight:
    def __init__(self):
        self.__flight_id=None
        self.__flight_name=None
        self.__source=None
        self.__destination=None
        self.__departure_time=None
        self.__arrival_time=None
        self.__duration=0
        self.__adult_fare=0
        self.__child_fare=0

    
    def get_flight_id(self):
        return self.__flight_id


    def get_flight_name(self):
        return self.__flight_name


    def get_source(self):
        return self.__source


    def get_destination(self):
        return self.__destination


    def get_departure_time(self):
        return self.__departure_time


    def get_arrival_time(self):
        return self.__arrival_time


    def get_duration(self):
        return self.__duration
    
    def get_adult_fare(self):
        return self.__adult_fare


    def get_child_fare(self):
        return self.__child_fare


    def set_flight_id(self, value):
        self.__flight_id = value


    def set_flight_name(self, value):
        self.__flight_name = value


    def set_source(self, value):
        self.__source = value


    def set_destination(self, value):
        self.__destination = value


    def set_departure_time(self, value):
        self.__departure_time = value


    def set_arrival_time(self, value):
        self.__arrival_time = value


    def set_duration(self, value):
        self.__duration = value
        
        
    def set_adult_fare(self, value):
        self.__adult_fare = value


    def set_child_fare(self, value):
        self.__child_fare = value

 
        
        
        
