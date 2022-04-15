#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

#Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)


#Create a class named Person, use the __init__() function to assign values for name and age:
###The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.----IMPORTANT###
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Bhawna", 22)

print(p1.name)
print(p1.age)


#The __init__() function is called automatically every time the class is being used to create a new object.
#Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bhawna", 22)
p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Bhawna", 22)
p1.myfunc()

#We can modify the properties of an object like this
p1.age = 40

#We can delete properties on objects by using the del keyword:
del p1.age

#We can delete objects by using the del keyword:
del p1

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.


class Person:
  pass