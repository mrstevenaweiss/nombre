
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

faker_db = {}

def update_name(name, new_info):
    faker_db[name].append(new_info)
    
    return faker_db[name]

def get_all_faker():
    return faker_db

def add_new_name(name):
    faker_db[name] = []

def main(name):
    print('starting program...')
    print('hello', name)
    print('welcome to your name memory', name)
    add_new_name('bruce')
    print('here is who is in your db', get_all_faker() )
    update_name('bruce', 'nyu')
    update_name('bruce', 'john')

main('steven')