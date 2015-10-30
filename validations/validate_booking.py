'''
Created on Aug 14, 2015

@author: sadhna01
'''
from database import cancel_bookingDB
def check_flightbooking(fbookingid):
    c=cancel_bookingDB.cancelFBooking(fbookingid)
    print("c",c)
    return c
    
def check_hotelbooking(hbookingid):
    return cancel_bookingDB.cancelHBooking(hbookingid)
