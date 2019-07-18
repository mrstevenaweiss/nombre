# from functions import *
import time
import os

# def instructions():
#     return

faker_db = {}

def get_all_faker():
    return faker_db

def add_new_name(name):
    faker_db[name] = []

def load(name):
    print('Starting program...')
    time.sleep(2) 
    os.system('clear')
    print('\n')
    print('\t Welcome to NOMBRE')
    print('\t Hello', name)
    print('\n')

def name_adder():
    print("Who would you like to add?" )
    new_name = input(">>> ")
    add_new_name(new_name)
    print("\n")
    print("You have added", new_name)
    print("\n")
    menu_text()

def name_updater(a_name):
    print("What memory would you like to associate with that person?" )
    a_memory = input(">>> ")
    update_name(a_name, a_memory)
    print("\n")
    print("You have updated,", a_name)
    print("\n")
    menu_text()

def all_address_book():
    print( get_all_faker() )
    menu_text()

def menu_text():
    print('\t What would you care to do? Type: ')
    print('\n')
    print("\t 1: Load a new name")
    print("\t 2: Add to an old name")
    print("\t 3: See your entire memory book")
    print("\t Keyword: To bring up a list of possible names" )
    print("\t Q: To quit" )
    print('\n')

def update_name(name, new_info):
    faker_db[name].append(new_info)
    return faker_db[name]

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
    menu_text()

    while True:
        choice = input(">>> ")

        if choice == "1":
            name_adder()

        elif choice == "2":
            print("Who would you like to update?" )
            a_name = input(">>> ")
            
            # multiple entries
            if a_name in faker_db:
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

        else:
            # this will be the memory recall 
            return_possibles(word)

    # print("0: What is this app?")

main('Mr Weiss')

# def load_memory():
#     """
#     Returns a list of all names.
#     """
    
#     # print("Loading word list from file...")
#     # # inFile: file
#     # inFile = open(WORDLIST_FILENAME, 'r')
#     # # wordlist: list of strings
#     # wordlist = []
#     # for line in inFile:
#     #     wordlist.append(line.strip().lower())
#     # print("  ", len(wordlist), "words loaded.")
#     # return wordlist