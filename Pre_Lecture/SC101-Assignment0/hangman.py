"""
File: hangman.py
Name: sheng-hao wu
-------------------------------
This file demonstrates a Python Console hangman game.
At the beginning of the game, users are asked to input
one letter at a time to guess out a dashed vocabulary (answer).
If the letter is in the answer, the Console updates the
dashed word to its current status. 7 wrong guesses end the game.
"""

import random
import requests

# Constant
N_TURNS = 7

def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"

#fetch content (JSON object) from vocabulary database URL, return as uppercase random word
def get_random_word():
    response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    data = response.json()
    random_word = random.choice(data)
    return random_word.upper()

def showWord(str, str_list2):
    print(str, end='')
    for i in range(len(str_list2)):
        if i == len(str_list2) - 1:
            print(str_list2[i])
        else:
            print(str_list2[i], end='')

def main():
    remained_chance = N_TURNS
    word_answer = []
    # get random from 9 words
    for c in random_word(): # get random from 9 words
    # get more random word from 9 database
    # for c in get_random_word():
        word_answer.append(c)
    # know what's the word for testing
    print('the words is ', word_answer)
    word_guess = ['-'] * len(word_answer)

    # user input character
    while (remained_chance > 0):
        showWord('The word looks like: ', word_guess)
        print('You have', remained_chance, 'guesses left')
        guess_char = input('Your guess: ')
        guess_char = guess_char.upper()

        # input is valid only if it's single alphabat
        if (guess_char.isalpha() == True) & (len(guess_char) == 1):
            # if match with answer, update word_guess
            if (guess_char in word_answer):
                for i in range(len(word_answer)):
                    if guess_char == word_answer[i]:
                        word_guess[i] = guess_char
                print('You are correct!')
            # show message when no match
            else:
                print('There is no', guess_char, '\'s in the word')
                remained_chance -= 1
        # show illegal message when data invalid
        else:
            print('illegal format.')
            remained_chance -= 1
        # if no '-' in word_guess, means every character had been guessed out and word is known
        if '-' not in word_guess:
            print('You win!!')
            showWord("The word was: ", word_guess)
            break
        # would only reach here in final loop when word remains unknown
        if remained_chance == 0:
            print("You are completely hang :(")
            showWord("The word was: ", word_answer)

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
