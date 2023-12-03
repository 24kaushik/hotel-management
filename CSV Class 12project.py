import csv
from os import remove, rename

def createcsv():
    csv_fobj = open("hotel.csv", "w", newline="")
    wtr_obj = csv.writer(csv_fobj)
    rec = []
    wtr_obj.writerow(["Hotel Number", "Hotel Name", "Contact Number", "Owner", "Address", "City", "State", "Landmark",
                     "Rating", "Number Of Rooms", "CAT", "price", "type of food", "Reviews"])
    while True:
        Hno = int(input("Enter Hotel Number:-"))
        hname = input("Enter Hotel Name:-")
        Cno = int(input("Enter Contact Number:-"))
        Owner = input("Enter Owner's Name:-")
        Address = input("Enter address of Hotel:-")
        City = input("Enter city of location:-")
        State = input("Enter state of location:-")
        Landmark = input("Enter Landmark near Hotel:-")
        Rating = input("Enter rating of the hotel:-")
        NoRo = int(input("Enter Number of Rooms:-"))
        CoRo = int(input("Enter CAT:-"))
        price = int(input("Enter price of rooms:-"))
        Type_of_food = input("Enter type of food:-")
        Reviews = input("Enter Reviews:-")
        rec += [[Hno, hname, Cno, Owner, Address, City, State, Landmark, Rating, NoRo, CoRo, price, Type_of_food, Reviews]]
        ans = input("Do you want to input more hotels?(y/n)")
        if ans == "n":
            break
    wtr_obj.writerows(rec)
    csv_fobj.close()

def append():
    csv_fobj = open("hotel.csv", "a", newline="")
    wtr_obj = csv.writer(csv_fobj)
    rec = []
    while True:
        Hno = int(input("Enter Hotel Number:-"))
        hname = input("Enter Hotel Name:-")
        Cno = int(input("Enter Contact Number:-"))
        Owner = input("Enter Owner's Name:-")
        Address = input("Enter address of Hotel:-")
        City = input("Enter city of location:-")
        State = input("Enter state of location:-")
        Landmark = input("Enter Landmark near Hotel:-")
        Rating = input("Enter rating of the hotel:-")
        NoRo = int(input("Enter Number of Rooms:-"))
        CoRo = int(input("Enter CAT:-"))
        price = int(input("Enter price of rooms:-"))
        Type_of_food = input("Enter type of food:-")
        Reviews = input("Enter Reviews:-")
        rec += [[Hno, hname, Cno, Owner, Address, City, State, Landmark, Rating, NoRo, CoRo, price, Type_of_food, Reviews]]
        ans = input("Do you want to input more hotels?(y/n)")
        if ans == "n":
            break
    wtr_obj.writerows(rec)
    csv_fobj.close()

def displaydetails():
    csv_fobj = open("hotel.csv", "r")
    rdrobj = csv.reader(csv_fobj)
    for rec in rdrobj:
        print(rec)
    csv_fobj.close()

def searchhno():
    csv_fobj = open("hotel.csv", "r")
    hno = int(input("Enter hotel number to search:-"))
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if int(rec[0]) == hno:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchanme():
    csv_fobj = open("hotel.csv", "r")
    hname = input("Enter hotel name to search:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[1] == hname:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchcity():
    csv_fobj = open("hotel.csv", "r")
    city = input("Enter city in which hotel to be searched is located:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[5] == city:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchstate():
    csv_fobj = open("hotel.csv", "r")
    state = input("Enter state in which hotel to be searched is located:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[6] == state:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchonrating():
    csv_fobj = open("hotel.csv", "r")
    rating = input("Enter the rating of the hotel:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[8] == rating:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchnor():
    csv_fobj = open("hotel.csv", "r")
    nor = input("Enter number of rooms in the hotel:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[9] == nor:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchcat():
    csv_fobj = open("hotel.csv", "r")
    cat = input("Enter CAT of the hotel to be searched:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[10] == cat:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchprice():
    csv_fobj = open("hotel.csv", "r")
    price = input("Enter price of the hotel:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[11] == price:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def searchtypeoffood():
    csv_fobj = open("hotel.csv", "r")
    type_of_food = input("Enter Type of food:-")
    rdrobj = csv.reader(csv_fobj)
    found = False
    for rec in rdrobj:
        if rec[12] == type_of_food:
            print(rec)
            found = True
            break
    if not found:
        print("Record not found.")
    csv_fobj.close()

def edithno():
    csv_fobj = open("hotel.csv", "r")
    temp = open("temp.csv", "w", newline="")
    hno = int(input("Enter Hotel number you want to edit: "))
    l1 = []
    Hno = int(input("Enter Hotel Number:-"))
    hname = input("Enter Hotel Name:-")
    Cno = int(input("Enter Contact Number:-"))
    Owner = input("Enter Owner's Name:-")
    Address = input("Enter address of Hotel:-")
    City = input("Enter city of location:-")
    State = input("Enter state of location:-")
    Landmark = input("Enter Landmark near Hotel:-")
    Rating = input("Enter rating of the hotel:-")
    NoRo = int(input("Enter Number of Rooms:-"))
    CoRo = int(input("Enter CAT:-"))
    price = int(input("Enter price of rooms:-"))
    Type_of_food = input("Enter type of food:-")
    Games = input("Enter games played in the room:-")
    Reviews = input("Enter Reviews:-")
    l1 = [[Hno, hname, Cno, Owner, Address, City, State, Landmark, Rating, NoRo, CoRo, price, Type_of_food, Reviews]]
    rdrobj = csv.reader(csv_fobj)
    wtrobj = csv.writer(temp)
    for rec in rdrobj:
        if int(rec[0]) == hno:
            rec = l1[0]
        wtrobj.writerow(rec)
    csv_fobj.close()
    temp.close()
    remove("hotel.csv")
    rename("temp.csv", "hotel.csv")

def edithname():
    csv_fobj = open("hotel.csv", "r")
    temp = open("temp.csv", "w", newline="")
    hname = input("Enter Hotel name you want to edit: ")
    l1 = []
    Hno = int(input("Enter Hotel Number:-"))
    hname = input("Enter Hotel Name:-")
    Cno = int(input("Enter Contact Number:-"))
    Owner = input("Enter Owner's Name:-")
    Address = input("Enter address of Hotel:-")
    City = input("Enter city of location:-")
    State = input("Enter state of location:-")
    Landmark = input("Enter Landmark near Hotel:-")
    Rating = input("Enter rating of the hotel:-")
    NoRo = int(input("Enter Number of Rooms:-"))
    CoRo = int(input("Enter CAT:-"))
    price = int(input("Enter price of rooms:-"))
    Type_of_food = input("Enter type of food:-")
    Games = input("Enter games played in the room:-")
    Reviews = input("Enter Reviews:-")
    l1 = [[Hno, hname, Cno, Owner, Address, City, State, Landmark, Rating, NoRo, CoRo, price, Type_of_food, Reviews]]
    rdrobj = csv.reader(csv_fobj)
    wtrobj = csv.writer(temp)
    for rec in rdrobj:
        if rec[1] == hname:
            rec = l1[0]
        wtrobj.writerow(rec)
    csv_fobj.close()
    temp.close()
    remove("hotel.csv")
    rename("temp.csv", "hotel.csv")

def countall():
    f1 = open("hotel.csv", "r")
    robj = csv.reader(f1)
    totrec = 0
    next(robj)
    for rec in robj:
        totrec += 1
    f1.close()
    print("Total hotel records:", totrec)

def countcity():
    f1 = open("hotel.csv", "r")
    robj = csv.reader(f1)
    next(robj)
    ctr = 0
    City = input("Enter City:")
    for rec in robj:
        if rec[5] == City:
            ctr += 1
    f1.close()
    print("Cities:", ctr)

def countstate():
    f1 = open("hotel.csv", "r")
    robj = csv.reader(f1)
    next(robj)
    ctr = 0
    State = input("Enter state:")
    for rec in robj:
        if rec[6] == State:
            ctr += 1
    f1.close()
    print("States:", ctr)

def countfood():
    f1 = open("hotel.csv", "r")
    robj = csv.reader(f1)
    next(robj)
    ctr = 0
    Type_of_food = input("veg or Non-veg:")
    for rec in robj:
        if rec[12] == Type_of_food:
            ctr += 1
    f1.close()
    print("Types of food are:", ctr)

def countrat():
    f1 = open("hotel.csv", "r")
    robj = csv.reader(f1)
    next(robj)
    ctr = 0
    Rating = input("Enter us a rating:")
    for rec in robj:
        if int(rec[8]) == int(Rating):
            ctr += 1
    f1.close()
    print("Total ratings:", ctr)

def inserthno():
    f1 = open("hotel.csv", "r")
    temp = open("temp.csv", "w", newline="")
    hno = int(input("Enter Hotel no to insert: "))
    ctr, newrec = 0, []
    rdrobj = csv.reader(f1)
    wtr_obj = csv.writer(temp)
    next(f1)
    wtr_obj.writerows([[Hno, hname, Cno, Owner, Address, City, State, Landmark, Rating, NoRo, CoRo, price, Type_of_food, Reviews]])
    for rec in rdrobj:
        if int(rec[0]) == hno:
            print("Enter new record details")
            Hno = int(input("Enter Hotel Number:-"))
            hname = input("Enter Hotel Name:-")
            Cno = int(input("Enter Contact Number:-"))
            Owner = input("Enter Owner's Name:-")
            Address = input("Enter address of Hotel:-")
            City = input("Enter city of location:-")
            State = input("Enter state of location:-")
            Landmark = input("Enter Landmark near Hotel:-")
            Rating = input("Enter rating of the hotel:-")
            NoRo = int(input("Enter Number of Rooms:-"))
            CoRo = int(input("Enter CAT:-"))
            price = int(input("Enter price of rooms:-"))
            Type_of_food = input("Enter type of food:-")
            Reviews = input("Enter Reviews:-")
            newrec = [[Hno, hname, Cno, Owner, Address, City, State, Landmark, Rating, NoRo, CoRo, price, Type_of_food, Reviews]]
            wtr_obj.writerow(newrec)
            ctr += 1
        wtr_obj.writerow(rec)
    if ctr == 0:
        print("record not found")
    f1.close()
    temp.close()
    remove("hotel.csv")
    rename("temp.csv", "hotel.csv")

def delhno():
    f1 = open
    f1 = open("hotel.csv", "r")
    temp = open("temp.csv", "w", newline="")
    ctr = 0
    hno = int(input("Enter Hotel no to delete: "))
    rdrobj = csv.reader(f1)
    wtr_obj = csv.writer(temp)
    next(rdrobj)
    for rec in rdrobj:
        if int(rec[0]) == hno:
            print("Deleted record details:")
            print(rec)
        else:
            wtr_obj.writerow(rec)
        ctr += 1
    if ctr == 0:
        print("Record not found")
    f1.close()
    temp.close()
    remove("hotel.csv")
    rename("temp.csv", "hotel.csv")

ans = 'y'
while ans.lower() == 'y':
    print("\n1. Create the Hotel directory csv file\n2. Append the details\n3. Display the records"
          "\n4. Search on basis of hotel no\n5. Search on hotel name\n6. Search on the basis of city"
          "\n7. Search on the basis of state\n8. Search on the basis of rating\n9. Search on the basis of number of rooms"
          "\n10. Search on the basis of category of rooms\n11. Search on the basis of price"
          "\n12. Search on the basis of types of food\n13. Edit record on the basis of hotel number"
          "\n14. Edit record on the basis of Hotel name\n15. Insert on Hotel Number\n16. Delete on Hotel Number")

    ch = int(input("\nEnter choice: "))
    if ch == 1:
        createcsv()
    elif ch == 2:
        append()
    elif ch == 3:
        displaydetails()
    elif ch == 4:
        searchhno()
    elif ch == 5:
        searchanme()
    elif ch == 6:
        searchcity()
    elif ch == 7:
        searchstate()
    elif ch == 8:
        searchonrating()
    elif ch == 9:
        searchnor()
    elif ch == 10:
        searchcat()
    elif ch == 11:
        searchprice()
    elif ch == 12:
        searchtypeoffood()
    elif ch == 13:
        edithno()
    elif ch == 14:
        edithname()
    elif ch == 15:
        inserthno()
    elif ch == 16:
        delhno()
    else:
        print("Wrong choice")

    ans = input("\nWant to continue? (y/n): ")
