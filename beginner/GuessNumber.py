from random import randint

__author__ = 'galo javier'

def generate_number():
    return randint(1,10)


def check_number(number, secret_number):
    if (number == secret_number):
      return ("That's the number")
    elif (number < secret_number):
        return ("too low")
    elif (number > secret_number):
        return ("too high")


def guess():
    secret_number = generate_number()
    number = int(input("guess the number "))
    print(check_number(number, secret_number))

guess()

