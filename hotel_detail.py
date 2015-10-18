'''
Created on Aug 12, 2015

@author: vikram.mandal
'''
class Hotel:
    def __init__(self):
        self.__hotelid = None
        self.__hotelname = None
        self.__location = None
        self.__efare =  None
        self.__dfare = None
    
    def set_hotelid(self,hotelid):
        self.__hotelid = hotelid
    def set_hotelname(self,hotelname):
        self.__hotelname = hotelname
    def set_location(self,location):
        self.__location = location
    def set_efare(self,efare):
        self.__efare = efare
    def set_dfare(self,dfare):
        self.__dfare = dfare
    
    def get_hotelid(self):
        return self.__hotelid
    def get_hotelname(self):
        return self.__hotelname
    def get_location(self):
        return self.__location
    def get_efare(self):
        return self.__efare
    def get_dfare(self):
        return self.__dfare 
