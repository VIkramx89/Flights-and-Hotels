'''
Created on Aug 13, 2015
'''
class HotelBooking:
    def __init__(self):
        self.__bookingid=0
        self.__flight_id=None
        self.__hotel_id=None
        self.__no_of_children=0
        self.__no_of_adults=0
        self.__primary_passenger=None
        self.__fare=0
        self.__eroom=0
        self.__droom=0
        self.__days_of_stay=0
    def get_bookingid(self):
        return self.__bookingid


    def get_flight_id(self):
        return self.__flight_id


    def get_hotel_id(self):
        return self.__hotel_id


    def get_no_of_children(self):
        return self.__no_of_children


    def get_no_of_adults(self):
        return self.__no_of_adults


    def get_primary_passenger(self):
        return self.__primary_passenger


    def get_fare(self):
        return self.__fare


    def get_eroom(self):
        return self.__eroom


    def get_droom(self):
        return self.__droom


    def get_days_of_stay(self):
        return self.__days_of_stay


    def set_bookingid(self, value):
        self.__bookingid = value


    def set_flight_id(self, value):
        self.__flight_id = value


    def set_hotel_id(self, value):
        self.__hotel_id = value


    def set_no_of_children(self, value):
        self.__no_of_children = value


    def set_no_of_adults(self, value):
        self.__no_of_adults = value


    def set_primary_passenger(self, value):
        self.__primary_passenger = value


    def set_fare(self, value):
        self.__fare = value


    def set_eroom(self, value):
        self.__eroom = value


    def set_droom(self, value):
        self.__droom = value


    def set_days_of_stay(self, value):
        self.__days_of_stay = value

