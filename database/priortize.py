'''
Created on Aug 14, 2015

@author: vkmguy
'''
from utility import DBConnectivity
from classes.hotel_detail import Hotel
def arrange_hotel(list_of_hotels):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        hotel_list={}
        final_list=[]
        for i in range(0,len(list_of_hotels)):
            flag=0
            hotelid=list_of_hotels[i].get_hotelid()
            cur.execute("select hotelid,count(hotelid)from hotel_booking where hotelid=:hid group by hotelid",{"hid":hotelid})
            for row in cur:
                flag=1
                if(row[0]==hotelid):
                    hotel_list.update({list_of_hotels[i]:(row[1]+1)})
                else:
                    hotel_list.update({list_of_hotels[i]:1})
            if(flag==0):
                hotel_list.update({list_of_hotels[i]:1}) 
        if(hotel_list=={}):
            return list_of_hotels
        max1=0
        l=len(hotel_list)
        hotel=Hotel()
        while(l!=0):
            max1=0
            for key,value in hotel_list.items():
                if(max1<value):
                    max1=value
                    hotel=key
            final_list.append(hotel)
            for key,value in hotel_list.items():
                if(key.get_hotelid()==hotel.get_hotelid()):
                    hotel_list.update({hotel:-1})
            l=l-1;
        return final_list
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()

