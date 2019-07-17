import time

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
    print('\n')
    print('\t Welcome to NOMBRE')
    print('\t Hello', name)
    print('\n')

def one():
    print("Who would you like to add?" )
    new_name = input(">>> ")
    add_new_name(new_name)
    print("\n")
    print("You have added", new_name)
    print("\n")
    program_text()

def three():
    print( get_all_faker() )
    program_text()

def program_text():
    print('\t What would you care to do? Type: ')
    print('\n')
    print("\t 1: Load a new name")
    print("\t 2: Add to an old name")
    print("\t 3: See you entire memory book")
    print("\t Keyword: To bring up a list of possible names" )
    print("\t Q: To quit" )
    print('\n')

def update_name(name, new_info):
    faker_db[name].append(new_info)
    return faker_db[name]

def main(name):
    load(name)
    program_text()

    while True:
        choice = input(">>> ")

        if choice == "1":
            one()

        elif choice == "2":
            print("Who would you like to update?" )
            a_name = input(">>> ")
            # check if name is in the db
            # multiple entries

            print("What memory would you like to associate with that person?" )
            a_memory = input(">>> ")
            update_name(a_name, a_memory)
            print("\n")
            print("You have updated,", a_name)
            print("\n")
            program_text()

        elif choice == "3":
            three()

        elif choice == "Q":
            print('Thank you for using Nombre.  See you later.')
            print('\n')
            break

        else:
            print("That is an invalid choice.  Try again or Hit 'Q' to exit")
            print('\n')
            program_text()

    # print("0: What is this app?")

    # add_new_name('bruce')
    # print('here is who is in your db', get_all_faker() )
    # update_name('bruce', 'nyu')
    # update_name('bruce', 'john')
    # print(get_all_faker())

main('steven')

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