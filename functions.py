import time
import os

def load(name):
    print('Starting program...')
    # time.sleep(2) 
    os.system('clear')
    print('\n')
    print('\t Welcome to NOMBRE')
    print('\t Hello', name)
    print('\n')
        
def menu_text():
    print('\t What would you care to do? Type: ')
    print('\n')
    print("\t 0: What is NOMBRE")
    print("\t 1: Load a new name")
    print("\t 2: Add to an old name")
    print("\t 3: See your entire memory book")
    print("\t Keyword: To bring up a list of possible names" )
    print("\t Q: To quit" )
    print('\n')

def instructions():
    print('\t NOMBRE is a name memory program ')
    print('\n')
    print("\t You know how you run into someone and their name is always at the tip of your tongue?")
    print("\t Well, instead of straining yourself, trying typing in the memories you associate with them.")
    print("\t We'll give you back a list of possibles")

