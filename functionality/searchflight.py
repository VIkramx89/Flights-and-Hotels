'''
Created on Aug 12, 2015

@author: sahil.singla01

'''

from validations import ViewValidations
from functionality import flight_booking
from exceptions import CustomExceptions
def search_flights():
        FLAG=0
        try:
            source=input("Enter the source:")
            ViewValidations.validate_source(source)
            destination=input("Enter the destination:")
            ViewValidations.validate_destination(destination)
            time=input("Enter the time")
            list_of_flights=ViewValidations.validate_view(source,destination,time)
            if(list_of_flights!=None):
                FLAG=1;
                for flight in list_of_flights:
                    print(flight.get_flight_id()," ",flight.get_flight_name()," ",
                          flight.get_departure_time()," ", flight.get_adult_fare()," ",flight.get_child_fare(),
                          flight.get_duration())
                print()   
                choice=input("Do you wish to continue booking? Enter 'Y' or 'N' ")
                if(choice=="Y"):
                    flightid=input("Enter the flight Id")
                    flight_booking.flight_booking(flightid)
        except CustomExceptions.InvalidSourceException as e:
            print(e)
        except CustomExceptions.InvalidDestinationException as e:
            print(e)
        except CustomExceptions.InvalidTimeException as e:
            print(e)
        except CustomExceptions.NoFlightFoundException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            if(FLAG==0):
                search_flights()        
                                                        
