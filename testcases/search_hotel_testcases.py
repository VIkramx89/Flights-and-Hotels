from validations.hotel_validation import validate_booked_flight
from validations.hotel_validation import validate_location
from validations.hotel_validation import validate_room_members
from validations.hotel_validation import validate_member
from exceptions.CustomExceptions import InvalidBookedFlightException
from exceptions.CustomExceptions import InvalidHotelLocationException
from exceptions.CustomExceptions import InvalidNoOfRoomsException
from exceptions.CustomExceptions import InvalidAdultExecutiveRoomsException

'''
positive test cases
'''
drooms = 2
erooms = 4
children = 2
adult = 4
c = validate_room_members(erooms,drooms,children,adult)
if(not c):
    print('valid no of rooms')

d = validate_member(erooms,adult)
if not d:
    print('Valid adult vs executive rooms')
    
'''
negative test cases
'''
try:
    list_of_flights=validate_booked_flight('000')
except InvalidBookedFlightException as e:
    print(e)
    
try:
    list_of_hotels = validate_location('laddakh')
except InvalidHotelLocationException as e:
    print(e)
try:
    drooms = 2
    erooms = 4
    children =3
    adult = 4
    f = validate_room_members(erooms,drooms,children,adult)
    if(f):
        raise InvalidNoOfRoomsException()
except InvalidNoOfRoomsException as e1:
    print(e1)

try:
    adult = 3
    erooms = 4
    g = validate_member(erooms,adult)
    if(g):
        raise InvalidAdultExecutiveRoomsException()
except InvalidAdultExecutiveRoomsException as e:
    print(e)
