__author__ = 'galo javier'


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6


shopping_list = ["banana", "orange", "apple","banana"]
print(shopping_list[2])

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for item in prices:
        if item == food:
            total += prices[item]
    return total

def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    return total




def distance_from_zero(x):
    print(type(x))
    if type(x) == int or type(x) == float:
        print("OK")
        return abs(x)
    else:
        return "Nope"

print(distance_from_zero(-10))


def cube(number):
    return number ** 3


def by_three(number):
   if number % 3 == 0:
       return cube(3)
   else:
       return False

def by_three2(number):
   if number % 3 == 0:
       return cube(number)
   else:
        return False


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


#
# (a * Xn + c )* M

def seed_increment(seed, a=7, c=501, maximum=5000):
    """

    :rtype : float
    """
    total = (a * seed) + c
    index = 0
    total_temp = 0

    while total < maximum:
        print(total)
        seed = total
        total_temp = total
        total = (a * seed) + c

        index += 1

    print("Iteraciones ", index)
    print("Valor Cercano ", total_temp)
    print("Valor maximo ", maximum)
    return total_temp


# f = seed_increment(0)


def check_margin(calculated, maximum, percent=10):
    margin = (maximum * percent) / 100
    print("Margin", margin)

    if calculated < margin:
        return False
    else:
        return True


# valid = check_margin(f,5000)
# print(valid)

# f = ask_ok('N',2,'yes or no ponte pilas')


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch",
           keydict="valuedict")


def make_incrementor(n):
    return lambda x: x + n


resp = make_incrementor(42)
print(resp(0))
print(resp(1))


def lambda_test(string_input):
    return lambda x: string_input.split(x)


lambda_var = lambda_test("hola")
print(lambda_var("l"))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print("2: ", pairs)


def factorial(x):
    factor = 1

    if x == 1:
        return 1
    else:
        for i in range(x):
            factor *= i+1
    return factor


#print(factorial(2))

def is_prime(x):

    if x < 1:
        return False

    prime_flag = True
    i = 2

    for n in range (i,x-1):
       if x % n == 0:
          prime_flag = False

    return prime_flag


#print(is_prime(0))




def reverse(text):
    new_text = ""
    for i in range(len(text)-1,-1,-1):
        new_text += text[i]
    return new_text
print("----------------------")
print(reverse("hola"))