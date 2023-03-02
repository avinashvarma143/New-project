from datetime import datetime

name=input("Enter your name:")
#Lists of items
lists='''
rice     Rs 20/kg
sugar    Rs 30/kg
salt     Rs 20/kg
oil      Rs 80/litre
panner   Rs 110/kg
maggi    Rs 50/each
boost    Rs 10/each
colgate  Rs 85/each
'''

#declaration
price=0
totalprice=0
finalprice=0
pricelist=[]
ilist=[]#item list
qlist=[]#quatity list
plist=[]#price list

#Rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'panner':110,'maggi':50,'boost':10,'colgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    input1=int(input("if you want to buy press 1 or press 2 for exist:"))
    if input1==2:
        break
    if input1==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("sorry you entered item is not avaiable")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalprice!=0:
            print(25*"=","AVIANSH SUPERMARKET",25*"=")
            print(30*" ","Chennai")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*" ","Quantity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,10*" ",ilist[i],10*" ",qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ","Totalprice:","Rs",totalprice)
            print(50*" ","gst amount:","Rs",gst)
            print(75*"-")
            print(50*" ","Finalprice:","Rs",finalprice)
            print(75*"-")
            print(15*" ",3*"*","Thank you , Please Visit Again",3*"*")
    




