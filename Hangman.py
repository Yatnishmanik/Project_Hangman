#   HANGMAN PROJECT
#   BY - ADARSH GAUR

import random

hanger = ['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''', '''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']

word_list = '''cricket mechanic apple bananna couch cardio office walking dead oak dog
            nut nuts peanut dayman hangman horse independnce butterfly tree barn chicken
            television phone chair table cat brooklyn nine cannibal jerry kilogram instagram
            pyhton woods wolf africa loser winner twitter'''.split()

def get_word():
    the_word = random.choice(word_list)
    return the_word

while True:
    guessed_letters = []

    word = get_word()
    word = word.upper()
    blanks = '-' * len(word)
    wrong = -1
    right = []


    def get_guess():
        print()
        print()
        guess = input("             Guess A Letter - ")
        guess = guess.upper()
        print()
        if guess in guessed_letters:
            print("   " + guess + " Has Already Been Chosen, Try Again")
            get_guess()
        elif len(guess) != 1:
            print("         Pick One Letter At A Time")
            get_guess()
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print("            Only Pick Letters")
            get_guess()
        else:
            guessed_letters.append(guess)
        return guess


    running = True
    while running == True:
        right = []
        for i in range(len(word)):
            if word[i] in guessed_letters:
                blanks = blanks[:i] + word[i] + blanks[i + 1:]
                right.append(i)

        print("\n" * 5)
        last = True
        x = 0

        if len(right) == len(word):
            print()
            print("       YOU SAVED HIM :) ")
            print()
            print("       The word is :  ", end='')
            print(word)
            print()
            print(hanger[7])
            print()
            print()
            x=int(input(" FOR RESTARTING THE GAME PRESS : 1\n OR PRESS ANY OTHER NUMBER FOR EXIT :- "))
            break
        
        if wrong < 5:
            print(hanger[wrong + 1])
        else:
            print(hanger[wrong + 1])
            print()
            print("        LOSER ! YOU KILLED HIM :( ")
            print()
            print()
            print("        The word is :  ", end='')
            print(word)
            print()
            print()
            x=int(input(" FOR RESTARTING THE GAME PRESS : 1\n OR PRESS ANY OTHER NUMBER FOR EXTI :- "))
            running = False
            last = False

        if last==True:
            print()
            print()
            print("                " + blanks + "")
            print()
            print()
            print("         ", end=' ')
            for i in range(len(guessed_letters)):
                print("", end='')
                print(guessed_letters[i], end='')
            guess = get_guess()
            if not guess in word:
                wrong = wrong + 1


    if x!=1:
        break


# END OF PROGRAM
