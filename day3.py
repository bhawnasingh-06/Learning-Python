a = "Hello"

print(a)
print("\n")

#This function converts all the characters in lower case of a string.
print(a.lower())

#This function converts all the characters in upper case of a string.
print(a.upper())

#This function replaces char1 by char2 in a string.
print(a.replace('ello', 'i'))

#e can simply add two or more strings by using ‘+’ operator between two variables.
a = "Hello"
b = "Bye"
print(a+b)


#It means we can easily format string by using .format function.
a = "Demo"
b = "Format"
print("This is the {} string".format(a,b))
print("This is the {0} string".format(a,b))
print("This is the {1} string".format(a,b))

#In placeholders we can pass values such as 0,1 etc.
print(f"This is a {a} of {b} string")


'''In Python there are some built-in or core data types :

Lists
Tuples
Sets
Dictionaries'''

#A List in Python represents a list of comma-separated values of any data type between square brackets.
lst = [8,5,2,9,7]

print(lst)
print(type(lst))

print(lst[0])
print(lst[1])
print(lst[2: 5])


#This function adds a new value or element in the end of the list.
lst.append(99)      #append runction
print(lst)


#This function adds a new element at any index no. in the list.
lst.insert(0,99)        #insert runction
print(lst)

#This function removes an element from the list.
lst.remove(2)       #remove runction
print(lst)


#This function removes one element from the end of the list.
lst.pop()       #remove one element from list
print(lst)

#This keywords allows us to remove or delete any particular element from the list by using it’s index no.
del lst[2]       #remove the element at index 2
print(lst)


#del variable(list) – This is used to delete whole list from the program.
#Variable(list).clear – This function removes all the elements of the list.
lst.clear()       #clears the list
print(lst)




#TUPLES
#These are those lists which cannot be changed i.e., are not modifiable. Tuples are represented as list of comma-separated values of any date type within parentheses.

tup = ('Demo', 'Hello', 54, 'Guys')
print(tup)
print(type(tup)) 
tup = list(tup)
tup[1] = 99
print(tup)


#Sets in python are a data type equivalent to sets in mathematics. It may consist various elements and the order is undefined.

set1 = {1,2,3,4,5,1,2,3}
print(set1)
print(type(set1))

#This function is used to add one element in the Set.
set1.add(99)
print(set1)

#This function allows us to add many elements in the set.
set1 = {1,2,3,4,5,1,2,3}
print(set1)
print(type(set1))
set1.update([5,6,99,109,199])
print(set1)

