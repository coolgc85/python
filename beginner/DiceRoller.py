from random import randint

__author__ = 'galo javier'


def generate_number():
    return randint(1, 6)


def play():
    dice_number = generate_number()
    print(dice_number)


def init():
    retry = True

    while retry:
        play()
        retry = bool((input("retry?") == "Y"))
    print("End Game")

init()