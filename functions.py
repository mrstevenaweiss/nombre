import time
import os

def load(name):
    print('Starting program...')
    time.sleep(2) 
    os.system('clear')
    print('\n')
    print('\t Welcome to NOMBRE')
    print('\t Hello', name)
    print('\n')
        
def menu_text():
    print('\t What would you care to do? Type: ')
    print('\n')
    print("\t 1: Load a new name")
    print("\t 2: Add to an old name")
    print("\t 3: See your entire memory book")
    print("\t Keyword: To bring up a list of possible names" )
    print("\t Q: To quit" )
    print('\n')
