# Check pypi.org (Python Package Index)

from array import array
import math
import random
from models import person
from strings import string_capitalize
from files import file_exists, folder_create, file_list

name = input("What is your name? ")
colour = input("What is your favourite colour? ")
age = 20
is_existing = True

greet = f"Hello {name}, I know you like the colour {colour} and you are {age} years old."
print(greet)
print(greet[0:4])
print(greet[:4])
print(greet.upper())
print("know" in greet)
print(10 // 3) #floor division
print(10 ** 3) #power of
print(round(3.9))
print(abs(-3.9))
print(math.floor(3.9))
print(math.pi)

if name == "Adel" or name == "adel":
    print("You are the author!")
elif name == "a":
    print("Maybe you are the author")
else:
    print("You are a visitor...")

i = 0
while i < 5:
    print("#" * i)
    i += 1

for item in [101, 202, 303, 404, 505]:
    print(item)

for item in range(5, 10):
    print(item)

for item in [5, 2, 5, 2, 2]:
    print("x" * item)

# list
list = [5, 2, 5, 2, 3]
print(list.pop())
list.remove(5)
print(list)

# tuple
tuple_collection = (1, 2, 3)
print(tuple_collection.count(2))

x, y, z = tuple_collection #unpacking
print(x, y, z)

# dictionary
dictionary = {
    "name": "John",
    "age": 30,
    "is_verified": True,
    "emotion": "😊",
}

print(dictionary["name"])
print(dictionary["emotion"])
print(dictionary.get("Name", "Joe"))

dictionary["phone"] = 4122131
print(dictionary["phone"])

def function(message):
    return f"Heyy {message} 🍎"

print(function("Abel")) #positional argument
print(function(message="Abel")) #keyword argument

try:
    age = int("abc")
except ValueError:
    print("Value needs to be numeric")

man = person.Person(string_capitalize("abel"))
print(man.name)
print(man.walk())
print(man.run(30))
print(man.eat())

print(random.randint(1, 100))

print(file_exists())
file_list()
folder_create()

# Dunder methods
x = 10
print(x.__add__(x))
print(dir(x))

# variable-length arguments
def multiply(a, b, *arg):
   mul = a * b
   for num in arg:
       mul *= num
   return mul
print(multiply(1, 2, 3, 4, 5))

def arguments(**kwargs):
   for key, value in kwargs.items():
       print(key + ": " + value)
arguments(arg1="argument 1", arg2="argument 2", arg3="argument 3")

conclusion = '''
    I'm glad that you liked this
    program. It is my first one
    written in Python, and I hope
    it becomes a great product!
'''
print(conclusion)
