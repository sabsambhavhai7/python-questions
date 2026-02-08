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
