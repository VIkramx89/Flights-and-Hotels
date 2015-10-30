
'''
Created on Aug 13, 2015

@author: sahil.singla01
'''
from validations.ViewValidations import validate_view
from exceptions.CustomExceptions import InvalidSourceException,\
    InvalidDestinationException, NoFlightFoundException, InvalidTimeException
list_of_flights=validate_view('Delhi','Bangalore','08:00')
list_of_flights=validate_view('Chandigarh','Kolkatta','07:00')
list_of_flights=validate_view('Chandigarh','Lucknow','16:00')
list_of_flights=validate_view('Delhi','Mumbai','09:00')


try:
    list_of_flights=validate_view('Delh','Banglore','08:00')
    list_of_flights=validate_view('Chandigarh','Banglore','08:00')
    list_of_flights=validate_view('Delhi','Mumbai','11:00')
    list_of_flights=validate_view('123','Banglore','08:00')
    list_of_flights=validate_view('Delh','567','08:00')
    list_of_flights=validate_view('Mumbai','Bangalore1','08:00')
    
except InvalidSourceException as e:
    print(e)
except InvalidDestinationException as e :
    print(e)
except InvalidTimeException as e:
    print(e)    
except NoFlightFoundException as e:
    print(e)
