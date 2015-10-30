from utility import DBConnectivity
from classes.hotel_detail import Hotel
def get_hotels(location):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_hotels=[]
        cur.execute("select hotelid, hotelname, location, efare, dfare from hotel where location=:location",{"location":location})
        for hotelid,hotelname,location,efare,dfare in cur:
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            hotel=Hotel()
            hotel.set_hotelid(hotelid)
            hotel.set_hotelname(hotelname)
            hotel.set_location(location)
            hotel.set_efare(efare)
            hotel.set_dfare(dfare)
            list_of_hotels.append(hotel)
        return list_of_hotels
        
    finally:
        cur.close()
        con.close()

def get_booked_flight(fbookid):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_members=[]
        cur.execute("select no_of_children,no_of_adults from flight_booking where bookingid=:fbookid",{"fbookid":fbookid})
        for booking in cur:
            list_of_members.append(booking[0])
            list_of_members.append(booking[1])
        return list_of_members
    finally:
        cur.close()
        con.close() 
        
