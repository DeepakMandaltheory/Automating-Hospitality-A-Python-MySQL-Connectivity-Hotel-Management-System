# Install the Necessary Packages

# pip install mysql-connector-python

import os
import platform
import mysql.connector
import pandas as pd
import datetime

mydb = mysql.connector.connect(
    user='root',
    password='admin@000', # My password for MySQL is 'admin@000' you might have 'root' or else .
    host='localhost',
    database='hotel'
)
mycursor = mydb.cursor()
# Function Register the New Cosumers
def register_cust():
    try:
        name = input("Enter name: ")
        addr = input("Enter address: ")
        indate = input("Enter check-in date (YYYY-MM-DD): ")
        outdate = input("Enter check-out date (YYYY-MM-DD): ")
        
        sql = "INSERT INTO custdata (custname, addr, indate, outdate) VALUES (%s, %s, %s, %s)"
        val = (name, addr, indate, outdate)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Customer registered successfully!")
    except Exception as e:
        print("Error:", e)
# Function to view room types
def room_type_view():
    try:
        choice = int(input("Do you want to see room type available? Enter 1 for yes: "))
        if choice == 1:
            sql = "SELECT * FROM roomtype"
            mycursor.execute(sql)
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)
# Function to calculate room rent
def room_rent():
    try:
        print("We have the following rooms for you:")
        print("1. Type A ----> Rs 1000 PN")
        print("2. Type B ----> Rs 2000 PN")
        print("3. Type C ----> Rs 3000 PN")
        print("4. Type D ----> Rs 4000 PN")
        
        choice = int(input("Enter your choice: "))
        nights = int(input("For how many nights did you stay: "))
        
        room_rates = {1: 1000, 2: 2000, 3: 3000, 4: 4000}
        
        if choice in room_rates:
            rent = room_rates[choice] * nights
            print(f"You have opted for room type {chr(64 + choice)}")
            print(f"Your room rent is: Rs {rent}")
        else:
            print("Invalid choice, please choose a valid room type.")
    except Exception as e:
        print("Error:", e)

# Function to view restaurant menu
def restaurant_menu_view():
    try:
        choice = int(input("Do you want to see the menu available? Enter 1 for yes: "))
        if choice == 1:
            sql = "SELECT * FROM restaurant"
            mycursor.execute(sql)
            rows = mycursor.fetchall()
            if not rows:
                print("No menu items found.")
            else:
                print("Restaurant Menu:")
                print("ID  | Item         | Price")
                print("--------------------------")
                for row in rows:
                    print(f"{row[0]:<3} | {row[1]:<12} | {row[2]}")
    except Exception as e:
        print("Error:", e)

# Function to order items from the restaurant
def order_item():
    try:
        choice = int(input("Do you want to see the menu available? Enter 1 for yes: "))
        if choice == 1:
            sql = "SELECT * FROM restaurant"
            mycursor.execute(sql)
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
        
        order_choice = int(input("Do you want to purchase from the above list? Enter your choice: "))
        items = {
            1: ("tea", 10),
            2: ("coffee", 10),
            3: ("colddrink", 20),
            4: ("samosa", 10),
            5: ("sandwich", 50),
            6: ("dhokla", 30),
            7: ("kachori", 10),
            8: ("milk", 20),
            9: ("noodles", 50),
            10: ("pasta", 50),
            11:("Vada pav",20)
        }
        
        if order_choice in items:
            item_name, item_price = items[order_choice]
            quantity = int(input(f"Enter quantity of {item_name}: "))
            total = item_price * quantity
            print(f"Your amount for {item_name} is: Rs {total}")
        else:
            print("Invalid choice, please choose from the menu.")
    except Exception as e:
        print("Error:", e)

# Function to calculate laundry bill
def laundry_bill():
    try:
        choice = int(input("Do you want to see the rate for laundry ? Enter 1 for yes: "))
        if choice == 1:
            sql = "SELECT * FROM laundry"
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
            print("{:<5} | {:<20} | {:<30} | {:<12} | {:<12}".format("ID", "Name", "Address", "Check-in", "Check-out"))
            print("-" * 85)
            for row in rows:
                # Extracting date fields from row
                cust_id = row[0]
                cust_name = row[1]
                cust_addr = row[2]
                check_in = row[3].strftime("%Y-%m-%d")  # Formatting check-in date
                check_out = row[4].strftime("%Y-%m-%d")  # Formatting check-out date
                
                print("{:<5} | {:<20} | {:<30} | {:<12} | {:<12}".format(cust_id, cust_name, cust_addr, check_in, check_out))
    except Exception as e:
        print("Error:", e)

# Function to Display the MENU and execute selected options
def menu_set():
    while True:
        print("                       ")
        print("1. Enter customer data")
        print("2. View room types")
        print("3. Calculate room bill")
        print("4. View restaurant menu")
        print("5. Calculate restaurant bill")
        print("6. Calculate laundry bill")
        print("7. View all customers")
        print("8. Exit")
        print("                       ")
        
        try:
            user_input = int(input("Please select an option: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        if user_input == 1:
            register_cust()
        elif user_input == 2:
            room_type_view()
        elif user_input == 3:
            room_rent()
        elif user_input == 4:
            restaurant_menu_view()
        elif user_input == 5:
            order_item()
        elif user_input == 6:
            laundry_bill()
        elif user_input == 7:
            view_all_customers()
        elif user_input == 8:
            print("Thanks for visiting!")
            break
        else:
            print("Invalid choice, please try again.")

def run_again():
    while True:
        menu_set()
        run_agn = input("Do you want to run again? (y/n): ").lower()
        if run_agn != 'y':
            break

run_again()
