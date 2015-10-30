'''
Created on Aug 13, 2015

@author: sadhna01
'''

from validations import flight_booking_validation
from exceptions import CustomExceptions
''' 
positive test cases
'''
fare=flight_booking_validation.validate_flights('SP101','01-01-16',2,3,"GOPAL")
print(fare)
fare=flight_booking_validation.validate_flights('AI101','28-02-16',1,4,"GOPAL")
print(fare)
'''
negetive test cases
'''
try:
    fare=flight_booking_validation.validate_flights('SP10','01-01-16',2,3,"GOPAL")
except CustomExceptions.InvalidFlightIdException as e:
    print(e)
try:
    fare=flight_booking_validation.validate_flights('SP101','01-01-16',0,0,"GOPAL")  
except CustomExceptions.InvalidAdultsException as e:
    print(e)
try:
    fare=flight_booking_validation.validate_flights('SP101','01-01-16',5,4,"GOPAL") 
except CustomExceptions.InvalidChildrenException as e:
    print(e)
try:
    fare=flight_booking_validation.validate_flights('SP101','32-01-16',2,3,"GOPAL")
except CustomExceptions.InvalidDateException as e:
    print(e)
try:
    fare=flight_booking_validation.validate_flights('SP101','30-02-16',2,3,"GOPAL")
except CustomExceptions.InvalidDateException as e:
    print(e)
try:
    fare=flight_booking_validation.validate_flights('SP101','30-03-16',2,3,"")
except CustomExceptions.InvalidPrimaryPassenger as e:
    print(e)
try:
    fare=flight_booking_validation.validate_flights('SP101','30-03-11',2,3,"Gopal")
except CustomExceptions.InvalidDateException as e:
    print(e)
