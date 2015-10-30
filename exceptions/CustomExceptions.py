'''
Created on Aug 12, 2015

@author: vikram.mandal
'''
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
class InvalidAdultsException(Exception):
    def __init__(self):
        super().__init__("Number of adults should be between 1 and 4")
class InvalidChildrenException(Exception):
    def __init__(self):
        super().__init__("Number of children should be between 0 and 4")     
