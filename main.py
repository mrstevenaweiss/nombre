
def load_memory():
    """
    Returns a list of all names.
    """
    
    # print("Loading word list from file...")
    # # inFile: file
    # inFile = open(WORDLIST_FILENAME, 'r')
    # # wordlist: list of strings
    # wordlist = []
    # for line in inFile:
    #     wordlist.append(line.strip().lower())
    # print("  ", len(wordlist), "words loaded.")
    # return wordlist


def main(name):
    print('starting program...')
    print('hello', name)
    print('welcome to your name memory', name)

main('steven')