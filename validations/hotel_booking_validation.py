'''
Created on Aug 13, 2015

@author: sadhna01
'''
from database import book_hotelDB
def validate_hotel(hotelid,eroom,droom,days_of_stay,booking_name,children,adult):
    return book_hotelDB.check_hotel(hotelid,eroom,droom,days_of_stay,booking_name,children,adult);
