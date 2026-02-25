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
