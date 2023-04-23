#import necesery modules
from get_word import *
import random
import colorama
import string
import functions
import os

#define necesery variables
ANSWER = random.choice(get_common_word())
grey = list(string.ascii_lowercase)
green = []
yellow = []
red = []
color = []
display = ''

#call the function from functions.py to display
functions.help()
functions.word_bank(grey,red,yellow,green)

#set up a for loop that run for 6 times, as there are 6 tries.
for x in range(6):
    #take an input from the player
    guess = input('Input a 5 letter word: ').lower()
    #this while loop checks if the input is valid (5 letter and a real word in the list)
    while len(guess) != 5 or not any(guess in x for x in get_word()):
        #this if statement check if the word is a command
        if guess[0] == '/':
            #this if statement check if the word is '/help'
            if guess.lower() == '/help':
                #call the help function
                functions.help()
                functions.word_bank(grey,red,yellow,green)
                print(display)
            #this if statement check if the word is '/search'
            if str(guess.split()[0]).lower() == '/search':
                #make sure that there are an argument for /search
                try:
                    #call search() from functions.py to run a search, which will return all valid word with the string matched, and print it out.
                    print(functions.search(str(guess.split()[1].lower())))
                    functions.word_bank(grey,red,yellow,green)
                    print(display)
                #catch if there are no argument for /search
                except IndexError:
                    print('Please put the string you are trying to search behind /search with a space.')
        #if the word input is not a command, thus is not a 5 character string nor a real word, hint the player to enter a valid word.
        if guess[0] != '/':
            print("Please enter a valid word.")
        #prompt player to input again
        guess = input('Input a 5 letter word: ').lower()
    #reset the colour
    color = []
    #iterate through the player's guess string
    for y in range(5):
        #check if the word is in the correct position
        if guess[y] == ANSWER[y]:
            #mark the position as green, thus correct
            color.append('GREEN')
            #make sure that the letter is removed from the list if it still exist
            try:
                grey.remove(guess[y])
                yellow.remove(guess[y])
            #if the letter is already removed, do nothing
            except:
                pass
            #append the letter into the correct/green letter list
            green.append(guess[y])
            #sort and remove duplicate
            green = sorted(list(dict.fromkeys(green)))
        else:
            #iterate the letter though the string, and see if it exist in any other position
            for z in range(5):
                #check if if it exist in other position
                if guess[y] == ANSWER[z]:
                    #add the letter into the yellow/other position list
                    color.append('YELLOW')
                    #remove the letter from grey/unknown letter list
                    try:
                        grey.remove(guess[y])
                    #if the letter is already removed, do nothing
                    except:
                        pass
                    #make sure that the letter is not already in the green, which is the correct list
                    if not guess[y] in green:
                        #add the letter to the yellow/different position list
                        yellow.append(guess[y])
                    #remove duplicate and sort the yellow list
                    yellow = sorted(list(dict.fromkeys(yellow)))
                    break
        #if the letter doesn't exist in any position of the word, then it is not in the word, thus will be added to red/incorrect list
        if len(color) != y + 1:
            #add letter to the red/incorrect list (color)
            color.append('RED')
            #remove the letter from the grey/unknown list
            try:
                grey.remove(guess[y])
            #do nothing if it is already removed
            except:
                pass
            #add the letter in the red word list
            red.append(guess[y])
            #sort and remove duplicates
            red = sorted(list(dict.fromkeys(red)))
        #build up the list letter by letter
        display = display + f'{getattr(colorama.Fore,color[y])}{guess[y]}{colorama.Style.RESET_ALL}'
    display = display + "\n"
    os.system('cls||clear')
    functions.word_bank(grey,red,yellow,green)
    print(display)
    if guess == ANSWER:
        print(f'Wow! The word is {colorama.Fore.GREEN}{ANSWER}{colorama.Style.RESET_ALL} indeed!')
        break
    elif guess != ANSWER and x == 5:
        print(f'Too bad! The word is {colorama.Fore.RED}{ANSWER}{colorama.Style.RESET_ALL}!')
