'''
Created on Aug 12, 2015

@author: sadhna01
'''
class InvalidFlightIdException(Exception):
    def __init__(self):
        super().__init__("The flight is invalid")
class InvalidAdultsException(Exception):
    def __init__(self):
        super().__init__("Number of adults should be between 1 and 4")
class InvalidChildrenException(Exception):
    def __init__(self):
        super().__init__("Number of children should be between 0 and 4")
class InvalidDateException(Exception):
    def __init__(self):
        super().__init__("Date is invalid")
class InvalidPrimaryPassenger(Exception):
    def __init__(self):
        super().__init__("primary passenger can  not be null")
#         
#############module 3 exceptions
class InvalidBookedFlightException(Exception):
    def __init__(self):
        super().__init__("The Booked flight you entered is wrong")
        
class InvalidHotelLocationException(Exception):
    def __init__(self):
        super().__init__("The hotel location you entered is not present in our service")
class InvalidAdultExecutiveRoomsException(Exception):
    def __init__(self):
        super().__init__("The adults vs executive rooms you selected is invalid")
class InvalidNoOfRoomsException(Exception):
    def __init__(self):
        super().__init__("The total no of rooms you entered is invalid")
        

'''
Created on Aug 12, 2015

@author: sahil.singla01
'''
'''
This file has all the custom exceptions needed for the project
'''
class InvalidSourceException(Exception):
    def __init__(self):
        super().__init__("The source is invalid")
            
class InvalidDestinationException(Exception):
    def __init__(self):
        super().__init__("The destination is invalid")
        
class InvalidTimeException(Exception):
    def __init__(self):
        super().__init__("The time invalid")        
   
class NoFlightFoundException(Exception):
    def __init__(self):
        super().__init__("No flight found for the given search conditions. Try different search values")        
        
        
'''
Created on Aug 13, 2015

@author: sadhna01
'''
class InvalidHotelIdException(Exception):
    def __init__(self):
        super().__init__("The Hotel is invalid")
class InvalidDaysOfStayException(Exception):
    def __init__(self):
        super().__init__("Days of stay should be greater than 0")
class InvalidBookingNameException(Exception):
    def __init__(self):
        super().__init__("please provide a booking name")
########################################################

####cancel module
class InvalidFlightBookingIdException(Exception):
    def __init__(self):
        super().__init__("The flight booking id  is invalid")
        
class InvalidHotelBookingIdException(Exception):
    def __init__(self):
        super().__init__("The hotel booking id  is invalid")
    
    
