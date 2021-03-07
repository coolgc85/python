__author__ = 'galo javier'
'''
Your challenge is to write a program, that outputs the color of a given square from the chessboard.

'''

print('dlairgkh t'[sum(map(ord,input()))%2::2])

def check_color(square_position):
    letter = square_position[0]
    number = square_position[1]

    if (ord(letter) + ord(number)) % 2 == 0:
        return "DARK"
    else:
        return "LIGHT"

print(check_color(input("Square location")))
print(ord("1"))



