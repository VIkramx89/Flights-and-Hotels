'''
Created on Aug 14, 2015

@author: sadhna01
'''
'''
positive test case
'''
from exceptions import CustomExceptions
from validations import hotel_booking_validation
result=hotel_booking_validation.validate_hotel('H010',2,3,2,"Gopal",2,3)
print("hotel fare",result)

'''
negetive test case
'''
try:
    result=hotel_booking_validation.validate_hotel('g010',2,3,2,"Gopal",2,3)
except CustomExceptions.InvalidHotelIdException as e:
    print(e)
try:
    result=hotel_booking_validation.validate_hotel('H010',5,0,2,"Gopal",2,3)
except CustomExceptions.InvalidAdultExecutiveRoomsException as e:
    print(e)
try:
    result=hotel_booking_validation.validate_hotel('H010',2,4,2,"Gopal",2,3)
except CustomExceptions.InvalidNoOfRoomsException as e:
    print(e)
try:
    result=hotel_booking_validation.validate_hotel('H010',2,3,2,"",2,3)
except CustomExceptions.InvalidBookingNameException as e:
    print(e)
try:
    result=hotel_booking_validation.validate_hotel('H010',2,6,2,"Gopal",5,3)
except CustomExceptions.InvalidChildrenException as e:
    print(e)
try:
    result=hotel_booking_validation.validate_hotel('H010',0,3,2,"Gopal",3,0)
except CustomExceptions.InvalidAdultsException as e:
    print(e)
