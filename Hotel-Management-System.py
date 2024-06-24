# pip install mysql-connector-python

import os
import platform
import mysql.connector
import pandas as pd
import datetime
mydb = mysql.connector.connect(user='root', password='admin@000',
                               host='localhost',
                               database='hotel')
mycursor=mydb.cursor()

def registercust():
    name=input("enter name:")
    addr=input("enter address:")
    indate = input("Enter check-in date (YYYY-MM-DD): ")
    outdate = input("Enter check-out date (YYYY-MM-DD): ")
    sql="insert into custdata(custname,addr,indate,outdate)values('{}','{}','{}','{}')".format(name,addr,indate,outdate)
    mycursor.execute(sql)
    mydb.commit()
def roomtypeview():
    print("Do yoy want to see room type available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def roomrent():
    print ("We have the following rooms for you:-")
    print ("1. type A---->rs 1000 PN\-")
    print ("2. type B---->rs 2000 PN\-")

    print ("3. type C---->rs 3000 PN\-")
    print ("4. type D---->rs 4000 PN\-")
    x=int(input("Enter Your Choice Please->"))
    n=int(input("For How Many Nights Did You Stay:"))
    if(x==1):
        print ("you have opted room type A")
        s=1000*n
    elif (x==2):
        print ("you have opted room type B")
        s=2000*n
    elif (x==3):
        print ("you have opted room type C")
        s=3000*n
    elif (x==4):
        print ("you have opted room type D")
        s=4000*n
    else:
        print ("please choose a room")
    print ("your room rent is =",s,"\n")
def restaurentmenuview():
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
       sql="select * from restaurent"
       mycursor.execute(sql)
       rows=mycursor.fetchall()
       for x in rows:
           print(x)
def orderitem():
    
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    print("do you want to purchase from above list:enter your choice:")
    d=int(input("enter your choice:"))
    if(d==1):
        print("you have ordered tea")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for tea is :",s,"\n")
    elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for coffee is :",s,"\n")
    elif(d==3):
        print("you have ordered colddrink")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for colddrink is :",s,"\n")
    elif(d==4):
        print("you have ordered samosa")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount fopr samosa is :",s,"\n")
    elif(d==5):
        print("you have ordered sandwich")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for sandwich is :",s,"\n")
    elif(d==6):
        print("you have ordered dhokla")
        a=int(input("enter quantity"))
        s=30*a
        print("your amount for dhokla is :",s,"\n")
    elif(d==7):
        print("you have ordered kachori")
        a=int(input("enter quantity"))
        s=10*a
        print("your amount for kachori is :",s,"\n")
    elif(d==8):
        print("you have ordered milk")
        a=int(input("enter quantity"))
        s=20*a
        print("your amount for kachori is :",s,"\n")
    elif(d==9):
        print("you have ordered noodles")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for noodles is :",s,"\n")
    elif(d==10):
        print("you have ordered pasta")
        a=int(input("enter quantity"))
        s=50*a
        print("your amount for pasta is :",s,"\n")
    else:
        print("please enter your choice from the menu")
# def laundarybill():
#     global z
#     print("Do yoy want to see rate for laundary : Enter 1 for yes :")
#     ch=int(input("enter your choice:"))
#     if ch==1:
#         sql="select * from laundary"
#         mycursor.execute(sql)
#         rows=mycursor.fetchall()
#         for x in rows:
#              print(x)
#     y=int(input("Enter Your number of clothes->"))
#     z=y*10
#     print("your laundary bill:",z,"\n")
#     return z
# Function to calculate laundry bill
def laundarybill():
    try:
        choice = int(input("Do you want to see the rate for laundry? Enter 1 for yes: "))
        if choice == 1:
            sql = "SELECT * FROM laundary"
            mycursor.execute(sql)
            rows = mycursor.fetchall()
            if not rows:
                print("No laundry rates found.")
            else:
                print("Laundry Rates:")
                print("ID   | Item        | Rate")
                print("------------------------")
                for row in rows:
                    print(f"{row[0]:<4} | {row[1]:<10} | {row[2]}")
            
            num_clothes = int(input("Enter the number of clothes: "))
            bill = num_clothes * 10
            print(f"Your laundry bill is: Rs {bill}")
            return bill
    except Exception as e:
        print("Error:", e)
        return 0

# Function to view all customers
def view_all_customers():
    try:
        sql = "SELECT * FROM custdata"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        
        if not rows:
            print("No customers found.")
        else:
            print("Customer Data:")
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)

def Menuset():
        
    print("1. Enter customer data")
    print("2. View room types")
    print("3. Calculate room bill")
    print("4. View restaurant menu")
    print("5. Calculate restaurant bill")
    print("6. Calculate laundry bill")
    print("7. View all customers")
    print("8. Exit")
    try:
        userinput=int(input("please select an above option:"))
    except ValueError:
        exit("\n Hey thats not a number")

    
    if(userinput==1):
        registercust()
    elif(userinput==2):
        roomtypeview()
    elif(userinput==3):
        roomrent()
    elif(userinput==4):
        restaurentmenuview()
    elif(userinput==5):
        orderitem()
    elif(userinput==6):
        laundarybill()
    elif(userinput==7):
        view_all_customers()
    elif(userinput==8):
        print('Thanks for visiting')
        quit()
    else:
        print("enter correct choice")
Menuset()
def runagain():
    runagn=input("\n want to run again Y/N:")
    while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
            p=0
            
        else:
            li=0
        Menuset()
        runagn=input("\n want to run again Y/N:")
runagain()
