__author__ = 'galo javier'


def anti_vowel(text):
    vowels = ['A', 'E', 'I', 'O', 'U']
    text2 = text
    for letter in text:
        if letter.upper() in vowels:
            text2 = text2.replace(letter,'')
    return text2

#print(anti_vowel("mundo"))


def censor(text, word):
     if text.find(word) >= 0:
         star = len(word) * "*"
         text = text.replace(word,star)
         print(text)
     return text


##censor("hello hello","hello")


def remove_duplicates(numbers):

    control_list = list(numbers)

    for number in numbers:
        if control_list.count(number) > 1:
            control_list.remove(number)
            print("removing ", number)
            print(len(control_list))
    return control_list

##print(remove_duplicates([2, 5, 6,2,5,4,9,0,1,4,6,9]))


def median(l):
    l.sort()
    lth = len(l)
    if lth % 2 == 1:
        return (l[int((lth/2) + .5)])
    else:
        return ((l[int(lth/2)] + l[int(lth/2 - 1)]) / 2.0)


#print (median([4, 5, 5, 4]))
#print(median([1]))

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
grades1 = [76, 42, 88]

def grades_sum(scores):
    result = 0
    for grade in scores:
        print(grade)
        result += grade
    return result

#print(grades_sum(grades1))