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


