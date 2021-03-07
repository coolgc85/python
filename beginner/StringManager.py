__author__ = 'galo javier'


def concat(*args, sep="/"):
    return sep.join(args)

p = concat("hi", "1")
print(p)

for i in range(1,5):
    print(i)

'''
n = int(input("enter a number of words: "))
print("Word to enter: ",n)

words = []

for i in range(n):
    word = str(input("enter a word: "))
    words.insert(i,word)

for w in words:
    print(w,len(w))

print(words.__len__())

wordToFind = str(input("enter a word to find: "))
print(words.__contains__(wordToFind))

'''

