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
