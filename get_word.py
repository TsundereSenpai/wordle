#Words compiled by Standford University (https://www-cs-faculty.stanford.edu/~knuth/sgb.html)
def get_word():
    return open('words.txt', 'r').read().splitlines()

def get_common_word():
    return open('common-words.txt', 'r').read().splitlines()
