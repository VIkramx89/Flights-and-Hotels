
from validations import hotel_validation
from exceptions.CustomExceptions import InvalidAdultExecutiveRoomsException
from exceptions.CustomExceptions import InvalidNoOfRoomsException
from functionality import book_hotel
from exceptions import CustomExceptions
from database import priortize
def search_hotel(fbookid = None):
    try:
        list_of_flights=[]
        list_of_hotels=[]
        flag=0
        if fbookid == None:
            choice=input("Do you have a flight booking Id? Enter 'Y' or 'N' ")
            if(choice == "Y"):
                fbookid=input("Enter the booking Id")
                list_of_flights = hotel_validation.validate_booked_flight(fbookid)
                children=list_of_flights[0]
                adult=list_of_flights[1]
            elif(choice == "N"):
                children = input("Enter the number of children")
                adult = input("Enter number of adults")
                children=int(children)
                adult=int(adult)
                hotel_validation.validate_no_of_children(children);
                hotel_validation.validate_no_of_adult(adult)
        else:
            list_of_flights = hotel_validation.validate_booked_flight(fbookid)
            children=list_of_flights[0]
            adult=list_of_flights[1]  
        drooms = input("Enter number of deluxe rooms")
        erooms = input("Enter number of executive rooms")
        drooms=int(drooms)
        erooms=int(erooms)
        location = input("Enter location")
        if ((drooms+erooms) == (children+adult)):
            if(adult>=erooms):
                list_of_hotel_unsorted = hotel_validation.validate_location(location)
                flag=1
                list_of_hotels=priortize.arrange_hotel(list_of_hotel_unsorted)
                #list_of_hotels=list_of_hotel_unsorted
                print("The hotels in order of popularity are-")
                print("Hotelid Hotel Name        Executive Fare  Deluxe Fare")
                print("-----------------------------------------------")
                for i in range(0,len(list_of_hotels)):
                    hotels=list_of_hotels[i]
                    print(hotels.get_hotelid()," ",hotels.get_hotelname(),"         ",hotels.get_efare(),"        ",hotels.get_dfare())
                    print()
                print("Do you wish to enter a Hotel? Enter 'Y' or 'N'")
                ch=input()
                if(ch=='Y'):
                    hotelid=input("Enter Hotel id:")
                    book_hotel.hotel_booking(hotelid,fbookid,children,adult,erooms,drooms)
            else:
                raise InvalidAdultExecutiveRoomsException()
                
        else:
            raise InvalidNoOfRoomsException()
    except InvalidAdultExecutiveRoomsException as e:
        print(e)
    except InvalidNoOfRoomsException as e1:
        print(e1)
    except CustomExceptions.InvalidHotelLocationException as e:
        print(e)        
    except Exception as e2:
        print(e2)          
    except CustomExceptions.InvalidChildrenException as e:
        print(e)
    except CustomExceptions.InvalidAdultsException as e:
        print(e)            
    except Exception  as e:
        print(e)
    finally:
        if(len(list_of_hotels)==0 or flag==0):
            search_hotel()
        else:
            pass
