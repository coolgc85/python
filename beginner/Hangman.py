from random import randint

__author__ = 'galo javier'

words = {1: "guess", 2: "kitchen", 3: "dog", 4: "cat"}


def select_word():
    print(words.__len__())
    index = randint(1, words.__len__())
    return words.get(index)

def play():
    word = select_word()
    word2 = word
    historical = {}
    print(word)
    count = 0
    turn = 1
    max_turn = len(word) + 3

    while turn <= max_turn:
        alreadyFlag = False
        letter = input("enter a letter: ")

        if len(historical)>0:

           if historical.get(letter, "") != "":
               print("already entered")
               alreadyFlag = True
           else:
               historical[letter]=letter
               if letter in word:
                   word.index()
        else:
            historical[letter]=letter

        if not alreadyFlag and letter in word:
           count += 1

        turn += 1

play()

