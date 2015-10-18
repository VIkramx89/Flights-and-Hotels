
from utility import DBConnectivity
from exceptions.CustomExceptions import InvalidFlightIdException
from exceptions.CustomExceptions import InvalidAdultsException
from exceptions.CustomExceptions import InvalidChildrenException
from exceptions.CustomExceptions import InvalidDateException
from exceptions.CustomExceptions import InvalidPrimaryPassenger
from datetime import datetime 
def check_flight(p_flightid,date_of_travel,p_no_of_children,p_no_of_adults,primary_passenger):
    try:
        
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        flag=0
        cur.execute("select adultfare,childfare from flight_details where flightid=:flight_id",{"flight_id":p_flightid})
        
        for row in cur:
            flag=1;
            if row[0]==None:
                raise InvalidFlightIdException()
            else:
                if(validate_date(date_of_travel)): 
                    if(int(p_no_of_children)>=0 and int(p_no_of_children)<=4):
                        if(int(p_no_of_adults)>=1 and int(p_no_of_adults)<=4):
                            if(primary_passenger!=""):   
                                fare=row[0]*int(p_no_of_adults)
                                fare+=row[1]*int(p_no_of_children)
                                return fare
                            else:
                                raise InvalidPrimaryPassenger()
                        else:
                            raise InvalidAdultsException()
                    else:
                        raise InvalidChildrenException()
                else:
                    raise InvalidDateException()
        if(flag==0):
            raise InvalidFlightIdException()
    finally:
        cur.close()
        con.close()
        
def retrieve_count():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select count(*) from flight_booking")
        for row in cur:
            return row[0];
    finally:
        cur.close()
        con.close()
    
def bookFlight(booking):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into flight_booking values(:bookingid,:flightid,:totalfare,:primarypassenger,:noofchildren,:noofadults,:dateoftravel)",{"bookingid":booking.get_bookingid(),"flightid":booking.get_flight_id(),"totalfare":booking.get_fare(),"primarypassenger":booking.get_primary_passenger(),"noofchildren":booking.get_no_of_children(),"noofadults": booking.get_no_of_adults(),"dateoftravel":booking.get_date_of_travel()})
        con.commit()
    finally:
        cur.close()
        con.close()
        
def validate_date(date_of_travel):
    try:
        p=datetime.strptime(date_of_travel,r'%d-%m-%y')
        yy=int(date_of_travel[6:])
        if(yy>=15):
            return True
        else:
            return False
    except ValueError:
        return False                                                                      
        
