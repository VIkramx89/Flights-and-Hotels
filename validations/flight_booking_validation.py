'''
Created on Aug 12, 2015

@author: sadhna01
'''
from database import book_flightDB
def validate_flights(flightid,date_of_travel,no_of_children,no_of_adults,primary_passenger):
    return book_flightDB.check_flight(flightid,date_of_travel,no_of_children,no_of_adults,primary_passenger);
