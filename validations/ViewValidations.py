'''
Created on Aug 12, 2015

@author: sahil.singla01
'''
from database import ViewDB
from exceptions.CustomExceptions import NoFlightFoundException,InvalidSourceException,InvalidDestinationException,InvalidTimeException

def validate_view(source,destination,time):
    try:
        if(validate_source(source)):
            if(validate_destination(destination)):
                if(validate_time(time)):
                    list_of_flights=ViewDB.get_flight(source,destination,time)
                    if(len(list_of_flights)==0):
                        raise NoFlightFoundException()
                else:
                    raise  InvalidTimeException()
            else:
                raise InvalidDestinationException()
        else:
            raise InvalidSourceException()
        return list_of_flights
    except Exception as e:
        print(e)
        
def validate_source(source): 
    if(source.isalpha()):
        return True
    else:
        raise InvalidSourceException()
def validate_destination(destination):
    if(destination.isalpha()):
        return True
    else:
        raise InvalidDestinationException()
def validate_time(time):
    if(len(time)==5):
        t1=time[0:2]
        t2=time[3:]
        if(int(t1)>=0 and int(t1)<=24 and int(t2)>=0 and int(t2)<=60):
            return True
        else:
            return False
                
    
