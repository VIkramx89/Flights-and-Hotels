'''
Created on Aug 12, 2015
'''
class FlightBooking:
    
    def __init__(self):
        self.__flight_id=None
        self.__date_of_travel=None
        self.__no_of_children=0
        self.__no_of_adults=0
        self.__fare=0
        self.__primary_passenger=None
        self.__bookingid=None
    def get_bookingid(self):
        return self.__bookingid


    def get_flight_id(self):
        return self.__flight_id


    def get_date_of_travel(self):
        return self.__date_of_travel


    def get_no_of_children(self):
        return self.__no_of_children


    def get_no_of_adults(self):
        return self.__no_of_adults


    def get_fare(self):
        return self.__fare


    def get_primary_passenger(self):
        return self.__primary_passenger


    def set_bookingid(self,value):
        self.__bookingid = value


    def set_flight_id(self, value):
        self.__flight_id = value


    def set_date_of_travel(self, value):
        self.__date_of_travel = value


    def set_no_of_children(self, value):
        self.__no_of_children = value


    def set_no_of_adults(self, value):
        self.__no_of_adults = value


    def set_fare(self, value):
        self.__fare = value


    def set_primary_passenger(self, value):
        self.__primary_passenger = value
