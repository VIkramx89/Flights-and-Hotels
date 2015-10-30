'''


'''
from utility import DBConnectivity
from exceptions.CustomExceptions import InvalidHotelIdException
from exceptions.CustomExceptions import InvalidAdultExecutiveRoomsException
from exceptions.CustomExceptions import InvalidNoOfRoomsException
from exceptions.CustomExceptions import InvalidDaysOfStayException 
from exceptions.CustomExceptions import InvalidBookingNameException
from validations import hotel_validation
def check_hotel(p_hotelid,eroom,droom,days_of_stay,booking_name,children,adult):
    try:
        totalfare=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select efare,dfare from hotel where hotelid=:hotel_id",{"hotel_id":p_hotelid})
        flag=0
        check =False
        for row in cur:
            flag=1
            if(row[0]==None):
                raise InvalidHotelIdException();
            else:
                check=hotel_validation.validate_member(eroom,adult)
                if(check):
                    raise InvalidAdultExecutiveRoomsException()
                check=hotel_validation.validate_room_members(eroom,droom,children,adult);
                if(check):
                    raise InvalidNoOfRoomsException()
                check=hotel_validation.validate_days_of_stay(days_of_stay)
                if(check):
                    raise InvalidDaysOfStayException()
                check=hotel_validation.validate_booking_name(booking_name)
                if(check):
                    raise InvalidBookingNameException()
                hotel_validation.validate_no_of_children(children)
                hotel_validation.validate_no_of_adult(adult)
                if(booking_name==""):
                    raise InvalidBookingNameException()
                totalfare=(row[0]*eroom+row[1]*droom)*days_of_stay
                return totalfare
        if(flag==0):
            raise InvalidHotelIdException()
        
        for row in cur:
            totalfare=(row[0]*eroom+row[1]*droom)*days_of_stay
            return totalfare
    finally:
        cur.close()
        con.close()
        
def retrieve_count():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select count(*) from hotel_booking")
        for row in cur:
            return row[0];
    finally:
        cur.close()
        con.close()
def bookHotel(booking):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into hotel_booking values(:bookingid,:hotelid,:flightid,:stayduration,:totalfare,:noofchildren,:noofadults,:eroom,:droom,:primarypassenger)",{"bookingid":booking.get_bookingid(),"hotelid":booking.get_hotel_id(),"flightid":booking.get_flight_id(),"stayduration":booking.get_days_of_stay(),"totalfare":booking.get_fare(),"noofchildren":booking.get_no_of_children(),"noofadults":booking.get_no_of_adults(),"eroom":booking.get_eroom(),"droom":booking.get_droom(),"primarypassenger":booking.get_primary_passenger()})
        con.commit()
    finally:
        cur.close()
        con.close()  
                     
