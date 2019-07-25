from functions import *
# def instructions():
#     return
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
    with open("names.txt") as name_db:
        names_decoded = json.load(name_db)
        print(names_decoded)

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
        print(names_decoded[name])
    
    # faker_db[name].append(new_info)
    # return faker_db[name]

def name_updater(a_name):
    print("What memory would you like to associate with that person?" )
    a_memory = input(">>> ")
    update_name(a_name, a_memory)
    print("\n")
    print("You have updated,", a_name)
    print("\n")
    menu_text()

def return_possibles(word):
    term = input('Give me a word: ')
    new_list = []

    for key, value in fake.items():
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
            
            # multiple entries
            if check_db(a_name) == True:
                name_updater(a_name)
            else:
                print("That person does not exist.  Try again." )
                menu_text()

        elif choice == "3":
            all_address_book()

        elif choice == "Q":
            print('Thank you for using Nombre.  See you later.')
            print('\n')
            break
        
        elif choice == "4":
            load_memory()

        # else:
            # this will be the memory recall 
            # return_possibles(word)

    # print("0: What is this app?")

main('Mr Weiss')

