#This function takes the input from user but it always take input in string data type 

#if we want any arithmetic operation to be done on that input then we need to type cast that input into either int or float data type.

a = int(input("Enter any number: "))
name = int(input("Enter any name: "))
print(type(a))
print(a)
print(type(name))
print(name)


#Modules in Python are Python files which contain some pre-written code(functions, classes, variables, etc.). Modules are free to use, and we can use them by using an import statement.

# To create a module just save the code you want in a file with the file extension .py:

# Example
# Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)

# Now we can use the module we just created, by using the import statement:

# Example
# Import the module named mymodule, and call the greeting function:

#import mymodule

# mymodule.greeting("Bhawna")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Example
# Create an alias for mymodule called mx:

# import mymodule as mx

# a = mx.person1["age"]
# print(a)



#import mymodule

#a = mymodule.person1["age"]
print(a)


#Built-in Modules

import platform

x = platform.system()
print(x)
#output: windows


#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
x = dir(platform)
print(x)


def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#We can choose to import only parts from a module, by using the from keyword.
# from mymodule import person1

# print (person1["age"])



#A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



#Python does not have built-in support for Arrays, but Python Lists can be used instead.

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

x = len(cars)
print(x)

cars.append("Honda")

y = cars.pop(1)
print(y)

cars.remove("Volvo")

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


