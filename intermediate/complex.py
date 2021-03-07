__author__ = 'galo javier'
import json
import datetime

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (list(filter(lambda x: x=='Python',languages)))

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print (movies.items())

threes_and_fives = [x for x in range(1,16) if x % 3==0 or x % 5 == 0]
print (threes_and_fives)

str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
print(str[start:end:stride])

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[len(garbled)-1::-2]
print(message)

"""
Create a new variable called message.
Set it to the result of calling filter() with the appropriate lambda
 that will filter out the "X"s. The second argument will be garbled.
Finally, print your message to the console.
"""

garbled2 = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = list(filter(lambda x: x!='X', garbled2))
print (message)

print("--------------------TODAY")
print(datetime.datetime.today())
print("-------------------- Construct")
print(datetime.datetime(2017,12,12,12,12,50))
print("-------------------- String to datetime")
print(datetime.datetime.strptime("10-may-2018","%d-%b-%Y"))
print("-------------------- add time ")
print( datetime.datetime.today()+ datetime.timedelta(days=30))

credential_dict = {"username": "gcolomav", "password": "123"}
json_str = json.dumps(credential_dict,ensure_ascii=False)
print(json_str)
print(credential_dict)
print(credential_dict["username"])