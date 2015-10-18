'''
'''
from validations import hotel_booking_validation
from validations import hotel_validation
from classes.booking_hotel import HotelBooking
from database import book_hotelDB
from exceptions import CustomExceptions
def hotel_booking(hotelid=None,flightid=None,children=None,adult=None,eroom=None,droom=None):
    try:
        totalfare=0
        flag=0
        if(hotelid==None):
            ch=input("Do you have a Flight Booking? Enter 'Y' or 'N'")
            if(ch=='Y'):
                flightid=input("Enter flight id:")
                flag=1;
            else:
                children=int(input("Enter number of children"))
                adult=int(input("Enter number of adults"))
                hotel_validation.validate_no_of_children(children);
                hotel_validation.validate_no_of_adult(adult)
            eroom=int(input("Enter number of executive room:"))
            droom=input("Enter number of delux room:")
            droom=int(droom)
            hotelid=input("Enter Hotel id:")
        days_of_stay=int(input("Enter the number of days of stay"))
        booking_name=input("Enter the name under which booking has to be made")
        if(flag==1):
            list_of_members = hotel_validation.validate_booked_flight(flightid)
            children=list_of_members[0]
            adult=list_of_members[1]
        totalfare=hotel_booking_validation.validate_hotel(hotelid,eroom,droom,days_of_stay,booking_name,children,adult)
        print("Total Fare",totalfare)
        count=book_hotelDB.retrieve_count()
        bookingid=count+1
        booking=HotelBooking()
        booking.set_bookingid(bookingid)
        booking.set_flight_id(flightid)
        booking.set_hotel_id(hotelid)
        booking.set_no_of_children(children)
        booking.set_no_of_adults(adult)
        booking.set_primary_passenger(booking_name)
        booking.set_fare(totalfare)
        booking.set_eroom(eroom)
        booking.set_droom(droom)
        booking.set_days_of_stay(days_of_stay)
        book_hotelDB.bookHotel(booking)
        print("Your accomodation is successfully booked with booking id",bookingid)
    except CustomExceptions.InvalidHotelIdException as e:
        print(e)
    except CustomExceptions.InvalidDaysOfStayException as e:
        print(e)
    except CustomExceptions.InvalidBookingNameException as e:
        print(e)
    except CustomExceptions.InvalidBookedFlightException as e:
        print(e)
    except CustomExceptions.InvalidHotelLocationException as e:
        print(e)
    except CustomExceptions.InvalidAdultExecutiveRoomsException as e:
        print(e)
    except CustomExceptions.InvalidNoOfRoomsException as e:
        print(e)
    except CustomExceptions.InvalidFlightIdException as e:
        print(e)
    except CustomExceptions.InvalidAdultsException as e:
        print(e)
    except CustomExceptions.InvalidChildrenException as e:
        print(e)
    except CustomExceptions.InvalidDateException as e:
        print(e)
    finally:
        pass
        if(totalfare==0):
            hotel_booking()
         
    
    
