#import all the modules needed
import os
import colorama
from get_word import *
#the utilisation of RegEx would be more effeicient to match strings however, the rubric require the code to iterate through string
import re

#define a function of help() that display a certain set of word whenever called.
def help():
    os.system('cls||clear')
    print(f'''Welcome to Words and Letters, a word guessing game that try to guess a 5 letter word.
here is the procesure:
1. You have 6 tries to guess a randomly chosen word.
2. Each guess must be a valid 5 letter word. Press enter to submit.
3. After the submission, the letter will be colour-coded to show how close the guess is to the chosen word.
{colorama.Fore.GREEN}Green{colorama.Style.RESET_ALL} letter: the letter is in the word and is in the right position.
{colorama.Fore.YELLOW}Yellow{colorama.Style.RESET_ALL} letter: the letter is in the word but in another position.
{colorama.Fore.RED}Red{colorama.Style.RESET_ALL} letter: the letter is not in the word.

    Example:
    a is in the word and the correct position, while the rest is not
    {colorama.Fore.GREEN}a{colorama.Style.RESET_ALL}{colorama.Fore.RED}egis{colorama.Style.RESET_ALL}

    i is in the word but in another position, while the rest of the letter isn't in the word
    {colorama.Fore.RED}cum{colorama.Style.RESET_ALL}{colorama.Fore.YELLOW}i{colorama.Style.RESET_ALL}{colorama.Fore.RED}n{colorama.Style.RESET_ALL}

    none of the letters are in the word
    {colorama.Fore.RED}xerox{colorama.Style.RESET_ALL}

commands:
/help: bring up this menu again
/search: return words that have the string inputted
    example: /search po''')
    input('Press Enter to continue...')
    os.system('cls||clear')

#define the function of search() that matc the argument string to the word bank and return a list of all words that matches
def search(arg):
    os.system('cls||clear')
    length = 5 - len(arg)
    return re.findall(f"[a-z]{{0,{str(length)}}}{arg}[a-z]{{0,{str(length)}}}",", ".join(get_word()))
    #the regex above is a more efficient way to achieve the same goal, however I opted to use a iteration in order to satisfy the rubric point here
    #I iterate through the the list of words in order to check if the string matches or not
    '''
    list = []
    for i in range(len(get_word())):
        if str(get_word()[i]).__contains__(arg):
            list.append(get_word()[i])
    return(list)
    '''

#display the current letters' status
def word_bank(grey,red,yellow,green):
    print(f'''Unknown Letters: {grey}
Red Letters: {colorama.Fore.RED}{red}{colorama.Style.RESET_ALL}
Yellow Letters: {colorama.Fore.YELLOW}{yellow}{colorama.Style.RESET_ALL}
Green Letters: {colorama.Fore.GREEN}{green}{colorama.Style.RESET_ALL}
''')
