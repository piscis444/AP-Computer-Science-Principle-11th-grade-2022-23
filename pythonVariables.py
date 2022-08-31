'''
#print command
x=5 
y="John"
print(x)
print(y)
# words in programming are called strings 
# 5 = integer => int
#"hello"= word => string
# booleans = 0,1 example true/false 

# variables are case sensitive 
a = 4 
A = "Bob"
print (a,A)
# A WILL NOT OVERWRITE a 
# - in programming means "assigned to" Example 5 is assigned to variables 

# LEGAL VARIABLE NAMES 
# variable must start w a letter or underscore character 
# CANNOT START WITH A NUMBER 
# must start with a lowercase 
# CASE SENSIIVE (AGE IS # age) AND CANNOT contain alpha-NUMERIC characters (a-z, 0-9) 
# python allows you to assign many values to multiple variable in one line
x,y,z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

# python allows you to assign 1 value to multiple variables \
x = y = z = "orange"
print(x)
print(y)
print(z)

#RANDOM NUMBER 
import random 
print(random.randrange(1,10))

#concatenation
#to concactonate or combine 2 strings you can use the + operator 
a="Hello"
B="Patricia"
c=a + B
print(c)
#add space between variables 
c = a + " " + B
#string format
age="36"
text="My name is Patricia, I am " + age 
print (text)
'''
#python boolean 
# it uses two values True or False, it evaluates any expression to True or to False, python then evaluates and returns a boolean answer 
print (10>9)
print (10==9)
print (10<9)

# Boolean in a condition (a if statement) 
a = 200 
b= 33
if b > a:
  print ("b is greater than a")
else:
  print ("a is greater than b")
  #evaluate values and variables 
#evaluate a string and a number, example function bool ()
print (bool("hello"))
print (bool(15))
# OPERATORS
# examples 
x = 15
y = 2 
print (x % y)
# print (x % y)
print (x//y) # the floor division // rounds the result down to the nearest number 
print (x**y) # same as 2*2*2*2*2

a = ("22")
b = ("17")
if a < b: 
  print ("hello")
else:
  print ("15")
