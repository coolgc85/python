__author__ = 'galo javier'

'''
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
So "Python" becomes "ythonpay."
To write a Pig Latin translator in Python, here are the steps we'll need to take:
'''

word = input("Enter a word ")
substring_word=""

if len(word) > 0 and word.isalpha():
    print("valid word")
    sufix = "ay"
    first_word = word[0]
    substring_word = word[1:]
    substring_word = substring_word + first_word + sufix

else:
    print("empty or numbers")
print (substring_word)
