'''
Created on Aug 12, 2015

@author: vikram.mandal
'''
from exceptions.CustomExceptions import InvalidBookedFlightException
from exceptions.CustomExceptions import InvalidHotelLocationException
from exceptions.CustomExceptions import InvalidAdultsException
from exceptions.CustomExceptions import InvalidChildrenException
from database import HotelDB


def validate_booked_flight(fbookid):
        list_of_flights=HotelDB.get_booked_flight(fbookid)
        if(len(list_of_flights) == 0 ):
            raise InvalidBookedFlightException()
        return list_of_flights
def validate_location(location):
    try:
        list_of_hotels=HotelDB.get_hotels(location)
        if(len(list_of_hotels)==0):
            raise InvalidHotelLocationException()
        else:
            return list_of_hotels
    finally:
        pass
def validate_no_of_children(children):
    try:
        if(children>=0 and children<=4):
            pass
        else:
            raise InvalidChildrenException()
    finally:
        pass    
def validate_no_of_adult(adult):
    try:
        if(adult>=1 and adult<=4):
            pass
        else:
            raise InvalidAdultsException()
    finally:
        pass    
    
def validate_no_of_rooms(drooms,erooms,children,adult):
    if((drooms+erooms) == (children+adult)):
        return True
    else:
        return False
def vadidate_adult_exRooms(adult,erooms):
    if(adult>=erooms):
        return True
    else:
        return False
