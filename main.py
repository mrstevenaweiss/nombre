from functions import *
import json
import os.path
from os import path

def start_db():
    faker_db = {}
    
    db = path.exists("names.txt")
    if db == False:
        print("\t Creating a names DB for you...")
        with open('names.txt', 'w') as name_db:
            json.dump(faker_db, name_db)
    else: 
        print("\t Readying your names...")
        print("\n")

def get_all_names():
    # make the print better...
    with open("names.txt") as name_db:
        names_decoded = json.load(name_db)
        for name in names_decoded:
            print(name, "-->", names_decoded[name])

def all_address_book():
    get_all_names()
    menu_text()

def add_new_name(name):
    with open('names.txt') as name_db:
        names_decoded = json.load(name_db)
    
    names_decoded[name] = []

    with open('names.txt', 'w') as name_db:
        json.dump(names_decoded, name_db)
    
    with open('names.txt') as name_db:
        names_decoded = json.load(name_db)

def name_adder():
    print("Who would you like to add?" )
    new_name = input(">>> ")
    add_new_name(new_name)
    print("\n")
    print("You have added", new_name)
    print("\n")
    menu_text()

def update_name(name, new_info):
    with open('names.txt') as name_db:
        names_decoded = json.load(name_db)
    
    names_decoded[name].append(new_info)

    with open('names.txt', 'w') as name_db:
        json.dump(names_decoded, name_db)
    return names_decoded[name]

def name_updater(a_name):
    print("What memory would you like to associate with that person?" )
    a_memory = input(">>> ")
    update_name(a_name, a_memory)
    print("\n")
    print("You have updated,", a_name, "\n")
    menu_text()

def check_db(name):
    with open('names.txt') as name_db:
        names_decoded = json.load(name_db)    
    return name in names_decoded 

def return_possibles(word):
    term = word
    new_list = []

    with open('names.txt') as name_db:
        names_decoded = json.load(name_db)

    for key, value in names_decoded.items():
        if term in value:
            new_list.append(key)

    if len(new_list) == 0:
        print("There is no match for this criteria")
    else: 
        print(new_list)

def main(name):
    load(name)
    start_db()
    menu_text()

    while True:
        choice = input(">>> ")

        if choice == "1":
            name_adder()

        elif choice == "2":
            print("Who would you like to update?" )
            a_name = input(">>> ")
            
            if check_db(a_name) == True:
                name_updater(a_name)
            else:
                print("That person does not exist.  Try again. \n" )
                menu_text()

        elif choice == "3":
            all_address_book()

        elif choice == "Q":
            print('Thank you for using Nombre.  See you later.')
            print('\n')
            break

        elif choice == "0":
            instructions()
            menu_text()

        else:
            return_possibles(choice)

main('Mr Weiss')

