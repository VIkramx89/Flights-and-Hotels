'''
Created on Aug 12, 2015

@author: sadhna01
'''
from classes.flight_booking import FlightBooking
from validations import flight_booking_validation
from database import book_flightDB
from functionality import search_hotel
from exceptions import CustomExceptions
def flight_booking(flightid=None):
    try:
        if(flightid==None):
            print("Enter Flight Id:")
            flightid=input()
        print("Enter date of travel:")
        date_of_travel=input()
        print("Enter number of children:")
        no_of_children=input()
        print("Enter number of adults")
        no_of_adults=input()
        print("Enter name of primary passenger")
        primary_passenger=input()
        fare=0
        fare=flight_booking_validation.validate_flights(flightid,date_of_travel,no_of_children,no_of_adults,primary_passenger)
        print("Total fare:",fare)
        count=book_flightDB.retrieve_count();
        bookingid="F"+str(count+1)
        booking=FlightBooking()
        booking.set_bookingid(bookingid)
        booking.set_flight_id(flightid)
        booking.set_date_of_travel(date_of_travel)
        booking.set_no_of_children(no_of_children)
        booking.set_no_of_adults(no_of_adults)
        booking.set_primary_passenger(primary_passenger)
        booking.set_fare(fare)
        book_flightDB.bookFlight(booking)
        print("Your ticket is successfully booked with booking id",bookingid)
        print("Do you wish to search a hotel? Enter 'Y'or 'N'")
        ch=input()
        if(ch=='Y'):
            search_hotel.search_hotel(bookingid);      
    except CustomExceptions.InvalidDateException as e:
        print(e)
    except CustomExceptions.InvalidFlightIdException as e:
        print(e)
    except CustomExceptions.InvalidChildrenException as e:
        print(e) 
    except CustomExceptions.InvalidAdultsException as e:
        print(e)     
    except CustomExceptions.InvalidPrimaryPassenger as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        if(fare==0):
            flight_booking()
        
