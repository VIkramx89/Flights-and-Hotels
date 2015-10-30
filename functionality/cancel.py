'''
Created on Aug 14, 2015

@author: sadhna01
'''
from exceptions.CustomExceptions import InvalidFlightBookingIdException
from exceptions.CustomExceptions import InvalidHotelBookingIdException
from validations import validate_booking
from _sqlite3 import DatabaseError, InterfaceError
def cancellation(flag):
    try:
        c=False
        if(flag==1):
            print("Enter flight booking id")
            fbookingid=input()
        else:
            print("Enter hotel booking id")
            hbookingid=input()
        if(flag==1):
            c=validate_booking.check_flightbooking(fbookingid)
        else:                         
            c=validate_booking.check_hotelbooking(hbookingid)   
    except InvalidFlightBookingIdException as e:
        print(e)
    except InvalidHotelBookingIdException as e:
        print(e)
    except DatabaseError as e:
        print(e)
    except InterfaceError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if(c==True and flag==1):
            print("Flight booking cancelled successfully")
        elif(c==True and flag==2):
            print("Hotel booking cancelled successfully")
