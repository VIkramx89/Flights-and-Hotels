'''
'''
from validations import ViewValidations
from exceptions import CustomExceptions
from utility import DBConnectivity
list_of_flight=[]
def search_advance():
    try:
        p_source=input("Enter the source:")
        ViewValidations.validate_source(p_source)
        p_destination=input("Enter the Destination:")
        ViewValidations.validate_destination(p_destination)
        print("Available options are:\n")
        print("=====================")
        res1=get_flight_with1Hop(p_source,p_destination)
        res2=get_flight_with2Hop(p_source,p_destination)
        if(res1==False and res2==False):
            print("No option")
    except CustomExceptions.InvalidSourceException as e:
            print(e)
    except CustomExceptions.InvalidDestinationException as e:
            print(e)
def get_flight_with1Hop(p_source,p_destination):
    try: 
        flag=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select t1.flightid,t1.flightname,t1.source,t1.destination,t1.departuretime,t1.arrivaltime,t2.flightid,t2.flightname,t2.source,t2.destination,t2.departuretime,t2.arrivaltime from flight_details t1,flight_details t2 where t1.destination=t2.source and t1.source=:source and t2.destination=:destination",{"source":p_source,"destination":p_destination})
        for row in cur:
            flag=1
            arr1=row[5]
            dep2=row[10]
            if(validate_timing(arr1,dep2)):
                print_flight(row,1)
        if(flag==1):
            return True
        else:
            return False
    finally:
        cur.close()
        con.close()
def get_flight_with2Hop(p_source,p_destination):
    try:
        flag=0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select t1.flightid,t1.flightname,t1.source,t1.destination,t1.departuretime,t1.arrivaltime,t2.flightid,t2.flightname,t2.source,t2.destination,t2.departuretime,t2.arrivaltime,t3.flightid,t3.flightname,t3.source,t3.destination,t3.departuretime,t3.arrivaltime from flight_details t1,flight_details t2,flight_details t3 where t1.destination=t2.source and t2.destination=t3.source and t1.source=:source and t3.destination=:destination",{"source":p_source,"destination":p_destination})
        for row in cur:
            flag=1
            arr1=row[5]
            dep2=row[10]
            if(validate_timing(arr1,dep2)):
                arr2=row[11]
                dep3=row[16]
                if(validate_timing(arr2,dep3)):
                    print_flight(row,2)
        if(flag==1):
            return True
        else:
            return False
    finally:
        cur.close()
        con.close()
def validate_timing(arr1,dep2):
    dephr=int(dep2[0:2])
    depmin=int(dep2[3:])
    deptime=dephr*60+depmin
    arrhr=int(arr1[0:2])
    arrmin=int(arr1[3:])
    arrtime=arrhr*60+arrmin
    if(arrtime<deptime):
        return True
    else:
        return False     
def print_flight(row,flag):
    if(flag==1):
        dur1=cal_duration(row[4],row[5])
        dur2=cal_duration(row[10],row[11])
        print("Flightid   Dep Time   Duration   Source   Destination")
        print(row[0],"\t",row[4],"\t",dur1,"\t",row[2],"\t",row[3])
        print("\n")
        print(row[6],"\t",row[10],"\t",dur2,"\t",row[8],"\t",row[9])
        print("--------------------------------------------------------------------------------------------------")
    else:
        dur1=cal_duration(row[4],row[5])
        dur2=cal_duration(row[10],row[11])
        dur3=cal_duration(row[16],row[17])
        print("Flightid   Dep Time   Duration   Source   Destination")
        print(row[0],"\t",row[4],"\t",dur1,"\t",row[2],"\t",row[3])
        print("\n")
        print(row[6],"\t",row[10],"\t",dur2,"\t",row[8],"\t",row[9])
        print("\n")
        print(row[12],"\t",row[16],"\t",dur3,"\t",row[14],"\t",row[15])
        print("--------------------------------------------------------------------------------------------------")
def cal_duration(dep,arr):
    dephr=int(dep[0:2])
    depmin=int(dep[3:])
    arrhr=int(arr[0:2])
    arrmin=int(arr[3:])
    duration=(arrhr*60+arrmin)-(dephr*60+depmin)
    durhr=int(duration/60)
    durmin=duration%60
    if(int(durmin)!=0):
        duration1=str(durhr)+"hrs "+str(durmin)+"mins"
    else:
        duration1=str(durhr)+"hrs " 
    return duration1
