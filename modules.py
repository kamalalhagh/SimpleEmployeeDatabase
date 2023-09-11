from os import system, name
from time import sleep
from tabulate import tabulate
import json


def create_db():
    with open("db.json", "w") as fp:
        print("Deleting every things")
        sleep(1)
        print("Creating database...")
        sleep(1)
        json.dump({}, fp)
        print("Created!")
        print("Now you can start in 3 seconds...")
        sleep(3)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def header(options):
    clear()
    i = 1
    for option in options:
        print(f"{i}. {option}", end="\t\t")
        i += 1
    print("")


def add_person(database):
    clear()
    person_id = len(database) + 1
    uid = input("Please enter UID: ")
    firstname = input("Please enter First Name: ")
    lastname = input("Please enter Last Name: ")
    phone = input("Please enter Phone Number: ")
    email = input("Please enter Email: ")
    address = input("Please enter Address: ")
    database[person_id] = dict({'UID': uid, 'FirstName': firstname, 'LastName': lastname, 'PhoneNumber': phone,
                                'Email': email, 'Address': address})


def edit_person(database):
    show_all(database, menu="0")
    edit = input("Which UID do you want to edit (0 for cancel): ")

    if edit == "0":
        return True
    for person in database:
        if edit == database[person]['UID']:
            db = database[person]
            tmp_firstname = input("Edit First Name or leave it empty: ")
            if tmp_firstname != '':
                db["FirstName"] = tmp_firstname
            tmp_lastname = input("Edit Last Name or leave it empty: ")
            if tmp_lastname != '':
                db["LastName"] = tmp_lastname
            tmp_phone = input("Edit Phone Number or leave it empty: ")
            if tmp_phone != '':
                db["PhoneNumber"] = tmp_phone
            tmp_email = input("Edit Email or leave it empty: ")
            if tmp_email != '':
                db["Email"] = tmp_email
            tmp_address = input("Edit Address or leave it empty: ")
            if tmp_address != '':
                db["Address"] = tmp_address
            print("All the changes applied!")
            sleep(3)
            break
    else:
        print("UID not found in database")
        print("You will redirect to main menu in 3 seconds ...")
        sleep(3)
        return True


def delete_person(database):
    show_all(database, menu="0")
    delete = input("Which UID do you want to delete (0 for cancel): ")
    if delete == "0":
        return True
    for person in database:
        if delete == database[person]['UID']:
            print("Deleting person...")
            database.pop(person)
            sleep(1)
            print("Deleted!")
            print("You will redirect to main menu in 3 seconds ...")
            sleep(3)
            break
    else:
        print("UID not found in database")
        print("You will redirect to main menu in 3 seconds ...")
        sleep(3)
        return True


def show_all(dic, menu=""):
    clear()
    table = dic.values()
    headers = {1: "UID", 2: "First Name", 3: "Last Name", 4: "Phone Number", 5: "Email", 6: "Address"}
    print(tabulate(table, headers=headers))
    print("------------------------------------------------------------------------------------")
    while menu != "0":
        menu = input("press 0 to go back")
    return True


def read_database():
    with open("db.json", "r") as fp:
        database = json.load(fp)
    return database


def save(database):
    with open("db.json", "w") as fp:
        print("Saving to database...")
        sleep(1)
        json.dump(database, fp)
        print("Saved!")
        print("You will redirect to main menu in 3 seconds ...")
        sleep(3)
    return True
