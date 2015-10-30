
from utility import DBConnectivity
from exceptions.CustomExceptions import InvalidFlightBookingIdException
from exceptions.CustomExceptions import InvalidHotelBookingIdException
from _sqlite3 import DatabaseError, InterfaceError
def cancelFBooking(fbookingid):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("delete from flight_booking where bookingid=:f_bookingid",{"f_bookingid":fbookingid})
        if(cur.rowcount==0):
            raise InvalidFlightBookingIdException()
        else:
            return True
    except InvalidFlightBookingIdException as e:
        print(e)
    except DatabaseError as e:
        print("Cancel you Hotel Booking first")
    except InterfaceError as e:
        print("Cancel you Hotel Booking first")
    except Exception as e:
        print("Cancel you Hotel Booking first")
    finally:
        con.close()
        cur.close()
        
def cancelHBooking(hbookingid):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("delete from hotel_booking where hotel_bookingid=:h_bookingid",{"h_bookingid":hbookingid})
        if(cur.rowcount==0):
            raise InvalidHotelBookingIdException()
        else:
            return True
    except InvalidFlightBookingIdException as e:
        print(e)
    except DatabaseError as e:
        print("Can not cancel the hotel booking")
    except Exception as e:
        print("Can not cancel hotel booking")
    finally:
        con.close()
        cur.close()
