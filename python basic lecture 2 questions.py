STR1="SAMBHAV"
len1= len(STR1)
STR2="SHUKLA"
len2= len(STR2)
print(STR1 + STR2)
print(len1 + len2)

print(STR1[0])


# COMTANINATION
STRING1="`Hello"
STRING2=" World`" 
FINAL_STRING= STRING1 + STRING2
print(FINAL_STRING)
len1=len(STRING1)
len2=len(STRING2)
TOTAL_LENGTH=len1 + len2
print(TOTAL_LENGTH)     


# INDEXING
number_1="god morning"
print(str(number_1[9]))
# slicing
print(str(number_1[0:3]))


# string functions
poppp="i am a coder"
print(poppp.endswith("der"))

# capitalize
print(poppp.capitalize())

# replace
print(poppp.replace("coder","developer"))

# find 
print(poppp.find("coder"))


# count
print(poppp.count("er"))


LECTURE 2 QUESTIONS - STRINGS

# question - 1
input_name = input("Enter your name: ")
length = len(input_name)
print("the length of the string is: ", length)\

# question - 2
variable1 = "@#$#$%^^&^%$#!!@##$%^&*(*&^%TGBFDERTYHGFDERTYHGF"
count = str.count(variable1,"$")
print(count)

contionaional functions
question - 3
age=21
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")   


light =="red"
    if (light == "green"): 
        print("you can cross the road")
    elif (light == "yellow"):
        print("get ready to cross the road")
    else:
        print("stop! do not cross the road")

marks=int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:    
    print("Grade D")
else:    print("Grade F") 

# nesting
if age >= 18:
    if age >= 60:
       if age >= 80:
           print("You cannot drive")
       else:
              print("You can drive but be careful")
              else:
              print("You cannot drive")

# question - 5
input_number = int(input("Enter a number: "))
if input_number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#  question - 6
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if A >= B and A >= C:
    print("A is the greatest number")
elif B >= A and B >= C:
    print("B is the greatest number")
else:
    print("C is the greatest number")



   # lists and turbles
marks = [90.4, 80.5, 70.9, 60.1, 50.2]
print(type(marks[0])) # 90.4
print(type(marks[1])) # 80.5
print(type(marks[2])) # 70.9  
print(type(marks[3])) # 60.1
print(type(marks[4])) # 50.2


# lists slicing 
    marks = [90.4, 80.5, 70.9, 60.1, 50.2]
print(marks[0:3]) # [90.4, 80.5, 70.9]
print(marks[1:4]) # [80.5, 70.9, 60.1]
print(marks[2:5]) # [70.9, 60.1, 50.2]  


list1 = [1, 2, 3, 4, 5]
list.append(6)
print(list1) # [1, 2, 3, 4, 5, 6]


list1 = [1, 2, 3, 4, 5]
list1.sort()
print(list1) # [1, 2, 3, 4, 5]
list1.sort(reverse=True)
print(list1) # [5, 4, 3, 2, 1]
list1.reverse()
print(list1) # [5, 4, 3, 2, 1]
list1 = [1, 2, 3, 4, 5]
list1.remove(3)
print(list1)
list1.pop(4)
print(list1)



# question - 1    

movies =[]
movie1 = input("Enter the name of movie 1: ")
movie2 = input("Enter the name of movie 2: ")
movie3 = input("Enter the name of movie 3: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


# question - 2
palindrome =['r','a','d','a','r']
palindrome_copy = palindrome.copy()
palindrome_copy.reverse()
if palindrome == palindrome_copy:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

# QUSTION 3

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))
print(sorted(grade))

#dictionarys

info = {
    "key1": "value1",
    "name": "John",
    "Learning": "python" ,    
}
print(info)
info["name"] ="sambhav"
print(info)

# NESTED DICTIONARIES
students = {
    "NAME": "John",
    "NAMES": ["AXEL", "MARIO", "LUIS"],
    "SUBJECTS": {
        "MATHS": 90,
        "ENGLISH": 85,
        "SCIENCE": 92
    },
    "AGES": [20, 21, 23, 34]
}
print(students)

# directory methods

students.keys()
students.values()
students.items() 
students.get("NAME")
students.update({"NAME": "AXEL"})
print(students.keys())
print(students.values())
print(students.items())             
print(students.get("NAME")) 
print(students.update({"NAME": "AXEL"}))

# SET
collections = (1,2,3,4)
print(collections)
print(type(collections))
collections = (1,2,3,4)
print(collections)
print(type(collections))

collections = (1,2,3,4)
collections.__add__((5,6,7,8))
print(collections.__add__((5,6,7,8)))
print(collections.pop())

set1= {1,2,3,4}
set2= {5,6,7,8}
print(set1.union(set2)) 
print(set1.intersection(set2))

# question2

set1 ={"python", "java", "c++", "javascript", "python","python", "java", "c++", "c"}
print(len(set1))

#  questoin3
subjects = set()
subjects.add(input("Enter the first subject: "))
subjects.add(input("Enter the second subject: "))         
subjects.add(input("Enter the third subject: "))
print(subjects)


# question4
marks = {}

x=int(input("input phy marks: "))
marks.update({"phy": x})

y=int(input("input chem marks: "))
marks.update({"chem": y})               

z=int(input("input math marks: "))
marks.update({"math": z})

print(marks)

# lecture5   loopss
counter = 0
while counter < 5:
    print("This is an infinite loop")
    counter += 1     



i=1
while i <= 100000:
        print("Sambhav Shukla",i)
        i += 2

a=1
while a <= 100:
    print(a)
    a += 1

  
a=100
while a >= 1:
    print(a)
    a -= 1

  
i=1
while i <= 10:
    print(2**i)
    i += 1

umbser = [1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(numbser):
    print(numbser[i])
    i += 1 

umbser = (1,4,9,16,25,36,49,64,81,100)
x=36 
i=0
while i < len(numbser):
    if numbser[i] == x:
        print("Found")
        break
    i += 1 


i=0
while i < 5:
    if i == 3:
      continue
    print(i)
    i += 1

i=0
while i < 5:
    if i == 3:
      i += 1
      continue
    print(i)
    i += 1

total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print(f"Total sum: {total}")

i = 2
while i <= 10:
    print(i)
    i += 2

user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type something (or 'exit' to quit): ")

password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access Granted!")

val = 1
while val < 50:
    print(val)
    val *= 2

i = 1
while i <= 5:
    print(f"3 x {i} = {3 * i}")
    i += 1
]

n = 1
while n < 100:
    if n == 4:
        break
    print(n)
    n += 1


x = 1
while x < 3:
    print(f"Value: {x}")
    x += 1
else:
    print("Loop finished successfully.")



# for loop

  list1 = [1,2,3,4,5]
for value in list1:
     print(value)

tuple1 = (1,2,3,4,5)
for value in tuple1:
            print(value) 

# stri
str= "Hello, World!"
for char in str:
    print(char)



list2 = [1,4,9,16,25,36,49,64,81,100]
x=49
for value in list2:
   if value == x:
      print("Found the value:", x)
      break
   print(value) 

seq= range(5)
for i in seq:
    print(i)

while counter < 5:
    print("This is an infinite loop")
    counter += 1

i=1
while i <= 100000:
        print("Sambhav Shukla",i)
        i += 2

i=1
while i <= 10:
    print(2**i)
    i += 1

numbser = [1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(numbser):
    print(numbser[i])
    i += 1 

numbser = (1,4,9,16,25,36,49,64,81,100)
x=36 
i=0
while i < len(numbser):
    if numbser[i] == x:
        print("Found")
        break
    i += 1 

     
def calc_sunm(a, b):
    sum = a + b
    return sum  
result = calc_sunm(5, 10)
print(result)

def inputnumber():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:        print("Odd")
inputnumber()   

def cal_factorial(n):
   fact =1 
for i in range(1, n+1):
         fact *= i
print(fact)
cal_factorial(5)


def converter(usd_value):
     inr_value = usd_value * 82.5
     print(usd_value,"USD is equal to", inr_value, "INR")
converter(100)

# RECURSION
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print (factorial(5))    

def print_list(lst,index=0):
    if index >= len(lst):
        return
    else:
        print(lst[index])
        print_list(lst,index+1)

ef sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
print(sum_of_natural_numbers(10))   

 fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print_list(fruits)


#  lecture 7   files io 
f=open("file.txt", "w")
data=f.read()
print(data)
print (type(data))
f.close()


xef sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
print(sum_of_natural_numbers(10))   

 fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print_list(fruits)

def inputnumber():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:        print("Odd")
inputnumber()   

def cal_factorial(n):
   fact =1 
for i in range(1, n+1):
         fact *= i
print(fact)
cal_factorial(5)

# RECURSION
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print (factorial(5)) 

list2 = [1,4,9,16,25,36,49,64,81,100]
x=49
for value in list2:
   if value == x:
      print("Found the value:", x)
      break
   print(value

         i=0
while i < 5:
    if i == 3:
      continue
    print(i)
    i += 1

ef print_list(lst,index=0):
    if index >= len(lst):
        return
    else:
        print(lst[index])
        print_list(lst,index+1)

ef sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
print(sum_of_natural_numbers(10))   

with open("note.txt", "w") as f:
    f.write("This is the first line.\n")

with open("note.txt", "a") as f:
    f.write("This line was added later.\n")

with open("note.txt", "r") as f:
    content = f.read()
    print(content)

with open("note.txt", "r") as f:
    lines = f.readlines()
    print(f"The file has {len(lines)} lines.")

lines_to_add = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("list_data.txt", "w") as f:
    f.writelines(lines_to_add)

import os

if os.path.exists("note.txt"):
    print("File found!")
else:
    print("File is missing.")

import json

user_data = {"id": 1, "name": "Gemini", "active": True}

# Save to file
with open("user.json", "w") as f:
    json.dump(user_data, f)

# Read from file
with open("user.json", "r") as f:
    data = json.load(f)
    print(data["name"])

with open("input_image.jpg", "rb") as original:
    data = original.read()

with open("copy_image.jpg", "wb") as copy:
    copy.write(data)

from pathlib import Path

path = Path("documents") / "work" / "report.txt"
path.parent.mkdir(parents=True, exist_ok=True) # Create folders if missing
path.write_text("Professional report content.")

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the world of AI.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The total sum is: {num1 + num2}")

price = float(input("Enter item price: "))
quantity = int(input("How many? "))
print(f"Total Cost: ${price * quantity}")

# User enters: 10 20 30
a, b, c = input("Enter three numbers: ").split()
print(f"Values received: {a}, {b}, and {c}")

age = int(input("Your age: "))
years_to_100 = 100 - age
print(f"You will be 100 years old in {years_to_100} years.")

# Enter fruits separated by commas
data = input("Enter 3 fruits (comma separated): ")
fruit_list = data.split(",")
print(f"First fruit in your list: {fruit_list[0].strip()}")

radius = float(input("Enter radius: "))
area = 3.14159 * (radius ** 2)
print(f"The area of the circle is: {area:.2f}") # Rounds to 2 decimal places

password = input("Enter password: ")
if password == "python123":
    print("Access Granted.")
else:
    print("Access Denied.")

word = input("Enter a word: ")
repeats = int(input("How many times? "))
print((word + " ") * repeats)

class Dog:
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed

# Creating an object
my_dog = Dog("Buddy", "Golden Retriever")
print(f"{my_dog.name} is a {my_dog.breed}.")

class Circle:
    pi = 3.14159 # Class-level attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

my_circle = Circle(5)
print(f"Area: {my_circle.area()}")


class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal): # Inherits from Animal
    def speak(self):
        print("Meow!")

my_cat = Cat()
my_cat.speak()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary) # Pulls name and salary from Employee
        self.department = department

boss = Manager("Alice", 90000, "IT")
print(f"{boss.name} manages {boss.department}.")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Balance updated: {self.__balance}")

account = BankAccount(1000)
account.deposit(500)
# print(account.__balance)  # This would raise an AttributeError

class Bird:
    def fly(self):
        print("Most birds can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins swim instead of flying.")

def make_it_fly(bird_obj):
    bird_obj.fly()

make_it_fly(Bird())
make_it_fly(Penguin())

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def info(cls):
        return f"This is the {cls.__name__} class."

print(Calculator.add(10, 5))
print(Calculator.info())

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature below absolute zero is impossible!")
        else:
            self._celsius = value

temp = Temperature(25)
temp.celsius = -300 # Triggers the setter logic

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self): # Controls what print() shows
        return f"'{self.title}' is {self.pages} pages long."

    def __len__(self): # Allows len(book_obj)
        return self.pages

my_book = Book("Python 101", 250)
print(my_book)
print(len(my_book))


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self): # Must implement this or Python will throw an error
        return self.side * self.side

sq = Square(4)
print(f"Square area: {sq.area()}")

nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])

x = 5
y = 10
print(not (x > 3 and y < 10))

for i in range(2, 10, 3):
    print("Hello")

for i in range(2, 10, 3):
    print("Hello")

def add_item(item, box=[]):
    box.append(item)
    return box

add_item("apple")
print(add_item("banana"))

val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")

squares = []
for x in range(5):
    squares.append(x * x)

def add_item(item, box=[]):
    box.append(item)
    return box

add_item("apple")
print(add_item("banana"))

def add_item(item, box=[]):
    box.append(item)
    return box

add_item("apple")
print(add_item("banana"))

def add_item(item, box=[]):
    box.append(item)
    return box

add_item("apple")
print(add_item("banana"))

val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")

squares = []
for x in range(5):
    squares.append(x * x)
val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")

data = {
    "fruits": ["apple", "banana", "cherry"],
    "colors": {"red": 1, "yellow": 2}
}

# COMTANINATION
STRING1="`Hello"
STRING2=" World`" 
FINAL_STRING= STRING1 + STRING2
print(FINAL_STRING)
len1=len(STRING1)
len2=len(STRING2)
TOTAL_LENGTH=len1 + len2
print(TOTAL_LENGTH)     


# INDEXING


val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")


val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")

val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")

val = 15
if val % 3 == 0:
    print("Fizz", end="")
if val % 5 == 0:
    print("Buzz", end="")

a, b = 5, 10
a, b = b, a
print(f"a: {a}, b: {b}") # a: 10, b: 5

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

def is_palindrome(s):
    clean_s = s.lower()
    return clean_s == clean_s[::-1]

print(is_palindrome("Radar")) # True

nums = [10, 20, 30, 40, 50]
reversed_nums = nums[::-1]
print(reversed_nums)

scores = {"Alice": 88, "Bob": 95, "Charlie": 92}
top_student = max(scores, key=scores.get)
print(f"Top Student: {top_student} with {scores[top_student]}")

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17)) # True

squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)

try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    print(f"Result: {num1 / num2}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers.")


# Writing
with open("test.txt", "w") as f:
    f.write("Hello Python")

# Reading
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

print("Hello, Python world!")

length = 5
width = 10
area = length * width
print(f"The area of the rectangle is: {area}")

name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # Adds to the list
print(fruits[0])        # Prints the first item: apple

colors = ["red", "green", "blue"]
for color in colors:
    print("I like " + color)

count = 1
while count <= 5:
    print("Number:", count)
    count += 1

def greet_user(username):
    print(f"Welcome back, {username}!")

greet_user("Alex")

student = {
    "name": "Sarah",
    "grade": "A",
    "subject": "Physics"
}
print(student["subject"])

student = {
    "name": "Sarah",
    "grade": "A",
    "subject": "Physics"
}
print(student["subject"])

import random

secret_number = random.randint(1, 10)
print(f"Your lucky number today is: {secret_number}")

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

numbers = {1, 2, 2, 3, 4, 4}
print(numbers)  # Output: {1, 2, 3, 4}

with open("test.txt", "w") as f:
    f.write("Hello, I am writing to a file!")

text = "PythonProgramming"
print(text[0:6])  # Output: Python
print(text[-11:]) # Output: Programming

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(merged) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

point = (10, 20)
x, y = point
print(f"X: {x}, Y: {y}")

user = {"name": "Alice", "role": "Admin"}
for key, value in user.items():
    print(f"{key}: {value}")
a = 5
b = 10
a, b = b, a
print(f"a is {a}, b is {b}")

from collections import Counter

data = ["apple", "apple", "orange", "banana", "apple"]
count = Counter(data)
print(count.most_common(1)) # [('apple', 3)]

letters = ["a", "b", "c", "d", "e"]
print(letters[:3])   # First three: ['a', 'b', 'c']
print(letters[::-1])  # Reverse the list!

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence) # "Python is awesome"

students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
# Sort by the second item in the tuple (the score)
students.sort(key=lambda x: x[1])
print(students)

tasks = ["Write code", "Test code", "Ship code"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

import sys

nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
print(flat) # [1, 2, 3, 4, 5, 6]

my_list = [i for i in range(1000)]
print(f"Memory used: {sys.getsizeof(my_list)} bytes")

import time

start_time = time.time()
# Simulating a task
time.sleep(1) 
end_time = time.time()

print(f"Task took {end_time - start_time:.2f} seconds")

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

# Find items in A but not in B
unique = set(list_a) - set(list_b)
print(unique) # {1, 2}

names = ["Alice", "Bob", "Charlie"]
# Create a dictionary of name lengths
name_lengths = {name: len(name) for name in names}
print(name_lengths) # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

score = 85
status = "Pass" if score >= 50 else "Fail"
print(status)

first, *middle, last = [1, 2, 3, 4, 5]
print(first)  # 1
print(middle) # [2, 3, 4]
print(last)   # 5

bool_list = [True, False, True]

print(any(bool_list)) # True (at least one is True)
print(all(bool_list)) # False (not all are True)

salary = 100_000_000 
print(f"Salary: {salary:,}") # Output: 100,000,000

import os

# Get a variable named 'USER_NAME' from your system
user = os.getenv("USER", "Guest")
print(f"Hello, {user}")

word = "Python"
reversed_word = word[::-1]
print(reversed_word) # nohtyP

multiply = lambda x, y: x * y
print(multiply(5, 6)) # 30

def future_function():
    # I'll write this later!
    pass

print("Program finished without crashing.")

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(1000000)
print(next(counter)) # Only calculates the next value when asked

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args)
    return wrapper

@debug
def greet(name):
    return f"Hello, {name}!"

greet("Bob")

prices = [10, 25, 50, 100]
# Apply a 10% tax to every item
taxed_prices = list(map(lambda x: x * 1.1, prices))
print(taxed_prices)

class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def charge(self):
        self.battery = 100
        print(f"{self.name} is fully charged!")

bot = Robot("Sparky", 45)
bot.charge()

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

def make_pizza(size, *toppings, **details):
    print(f"Making a {size} inch pizza with {toppings}")
    print(f"Delivery notes: {details.get('notes', 'None')}")

make_pizza(12, "mushrooms", "peppers", notes="Leave at front door")

class DatabaseConnection:
    def __enter__(self):
        print("Connected to DB")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closed DB connection")

with DatabaseConnection() as db:
    print("Doing work...")

required_skills = {"Python", "SQL", "Linux"}
my_skills = {"Python", "Java"}

missing = required_skills - my_skills
common = required_skills & my_skills
print(f"You need to learn: {missing}")

import re

text = "Contact us at support@company.com or sales@web.org"
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(emails)

from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float

item = Product(1, "Laptop", 999.99)
print(item) # Output is nicely formatted automatically

import asyncio

async def fetch_data():
    print("Start fetching...")
    await asyncio.sleep(2)  # Simulates an I/O bound task
    print("Done fetching!")
    return {"data": 123}

async def main():
    # Runs the coroutine
    result = await fetch_data()
    print(result)

asyncio.run(main())

from multiprocessing import Process

def heavy_computation(name):
    print(f"Task {name} is processing millions of numbers...")

if __name__ == "__main__":
    processes = [Process(target=heavy_computation, args=(i,)) for i in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2

# s = Shape()  <-- This would throw an error!

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return f"${self._salary:,}"

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

emp = Employee(50000)
emp.salary = 60000  # Sets via the setter
print(emp.salary)   # Gets via the property

from collections import deque

queue = deque(["task1", "task2", "task3"])
queue.append("task4")      # Add to right
queue.appendleft("critical") # Add to left
queue.popleft()            # Remove from left
print(queue)

from contextlib import contextmanager

@contextmanager
def simple_timer(label):
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{label}: {end - start:.4f}s")

with simple_timer("My Loop"):
    sum(range(1000000))

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True: Both are the exact same instance

import itertools

# Get all combinations of 2 items
items = ['A', 'B', 'C']
combos = list(itertools.combinations(items, 2))
print(combos) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

def handle_command(command):
    match command.split():
        case ["quit"]:
            print("Goodbye!")
        case ["load", filename]:
            print(f"Loading {filename}...")
        case ["move", x, y] if int(y) > 0:
            print(f"Moving to {x}, {y}")
        case _:
            print("Unknown command")

handle_command("move 10 20")

from functools import singledispatch

@singledispatch
def report(value):
    print(f"Generic report: {value}")

@report.register(int)
def _(value):
    print(f"Integer report: {value * 10}")

@report.register(list)
def _(value):
    print(f"List report: Items = {len(value)}")

report(5)       # Triggers integer version
report([1,2,3]) # Triggers list version

import os
from contextlib import contextmanager

@contextmanager
def working_directory(path):
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

with working_directory("/tmp"):
    # Do something in /tmp
    print(f"Current dir: {os.getcwd()}")

class Point:
    __slots__ = ('x', 'y') # No __dict__ created for these instances
    def __init__(self, x, y):
        self.x = x
        self.y = y

import time

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed. Retrying...")
                    time.sleep(1)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry(times=3)
def unstable_api():
    raise ConnectionError("Server down")

import numpy as np

arr = np.array([1, 2, 3, 4])
# Vectorized operation: multiplies every element by 10 simultaneously
result = arr * 10 
print(result)

import pickle

data = {"scores": [90, 80, 70], "user": "Admin"}

# Save to file
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load from file
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

import os

db_password = os.getenv("DB_PASSWORD", "default_guest_password")
if not db_password:
    print("Warning: Security key not found!")

# Run this in your terminal/command prompt
python -m http.server 8000


import inspect

class MyClass:
    def secret_method(self): pass

# Get all methods of the class
methods = inspect.getmembers(MyClass, predicate=inspect.isfunction)
print(methods)

import os

db_password = os.getenv("DB_PASSWORD", "default_guest_password")
if not db_password:
    print("Warning: Security key not found!")

from apple_concurrent.futures import ThreadPoolExecutor
import requests

urls = ["https://google.com", "https://python.org", "https://github.com"]

def fetch(url):
    return requests.get(url).status_code

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch, urls))
print(results)

# Writing to a file
with open("note.txt", "w") as f:
    f.write("Hello from Python!")

# Reading from a file
with open("note.txt", "r") as f:
    content = f.read()
    print(content)

tasks = ["Clean", "Code", "Sleep"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

multiply = lambda x, y: x * y
print(multiply(5, 6)) # Outputs: 30

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers) # [1, 2, 3, 4, 5]

names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

user = {"name": "Alex"}
# Returns 'Guest' because 'email' isn't in the dict
email = user.get("email", "Guest") 
print(email)

text = "Python"
print(text[:2])   # Py (First two)
print(text[::-1]) # nohtyP (Reversed)

import time

print("Starting...")
time.sleep(2) # Pauses for 2 seconds
print("Done!")

stats = [True, True, False]
print(any(stats)) # True (at least one is True)
print(all(stats)) # False (not all are True)

prices = {'apple': 1.0, 'banana': 0.5, 'cherry': 2.5}
# Increase all prices by 10%
expensive_prices = {k: v * 1.1 for k, v in prices.items() if v > 0.5}
print(expensive_prices)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.string)

data = [(1, 'bread'), (3, 'apple'), (2, 'cheese')]
# Sort by the second element in the tuple (the name)
data.sort(key=lambda x: x[1])
print(data)

def timer_decorator(func):
    def wrapper():
        print("Starting task...")
        func()
        print("Task finished.")
    return wrapper

@timer_decorator
def run_process():
    print("Processing data...")

run_process()

import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()
print(f"Task Title: {data['title']}")

# Use parentheses instead of brackets
squares_gen = (x**2 for x in range(1000000))

print(next(squares_gen)) # 0
print(next(squares_gen)) # 1

def make_pizza(size, *toppings):
    print(f"Making a {size} inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, "mushrooms", "peppers", "extra cheese")

import re

text = "Contact us at support@example.com or sales@biz.org"
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
print(emails)

class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def greet(self):
        return f"System Online. I am {self.name} v{self.version}."

bot = Robot("Gemini-Bot", 3.0)
print(bot.greet())

print("Hello, World!")

a, b = 5, 10
a, b = b, a
print(f"a: {a}, b: {b}") # a: 10, b: 5


squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) # [0, 4, 16, 36, 64]

text = "Python"
reversed_text = text[::-1]
print(reversed_text) # nohtyP

word = "racecar"
is_palindrome = word == word[::-1]
print(is_palindrome) # True

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(merged) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

import time

start_time = time.time()
# Add the code you want to measure here
time.sleep(1) 
end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")

import random

friends = ["Alice", "Bob", "Charlie", "Diana"]
winner = random.choice(friends)
print(f"The winner is: {winner}")

# Assuming 'test.txt' exists
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

import random

friends = ["Alice", "Bob", "Charlie", "Diana"]
winner = random.choice(friends)
print(f"The winner is: {winner}")

# Assuming 'test.txt' exists
with open("test.txt", "r") as file:
    content = file.read()
    print(content)
\
import random

friends = ["Alice", "Bob", "Charlie", "Diana"]
winner = random.choice(friends)
print(f"The winner is: {winner}")

name = "Gemini"
version = 3
print(f"I am {name} version {version}.")

fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # Adds to the end
print(fruits[1])        # Outputs: banana (index starts at 0)

for i in range(5):
    print(f"Number: {i}")

age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

def greet(user):
    return f"Hello, {user}! How can I help you today?"

print(greet("Alice"))

user_info = {
    "name": "Alex",
    "role": "Developer",
    "language": "Python"
}
print(user_info["role"])

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) # [1, 4, 9, 16, 25]

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")

# Assuming 'example.txt' exists in your folder
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Assuming 'example.txt' exists in your folder
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

multiply = lambda x, y: x * y
print(multiply(5, 6)) # Outputs: 30

import json

json_data = '{"name": "TechBot", "active": true}'
data = json.loads(json_data)
print(data["name"])
