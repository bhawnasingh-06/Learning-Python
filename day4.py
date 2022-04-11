#The dictionary is an unordered set of comma-separated key: value pairs, within {},with the requirement that within a dictionary, no two keys can be the same (i.e., there are unique keys within a dictionary).

dictionary1 = {
    "Play" : "Doing some activity",
    "Food" : "Something eatable",
    "Python" : "Language",
}

print(dictionary1)
print(len(dictionary1))

#Conditional statements
print("\t Conditional Statements \n")

age = int(input("Enter your age: "))

if (age>=18):
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")






    x = int(input("Enter any number: "))

if (x>50):
    print("Number is greater than 50")
elif (x>25):
    print("No. entered is b/w 25-50")
elif (x>0):
    print("Number entered is between 0-25")
else:
    print("Enter valid number")



#Loops
num = 5
for a in range(1, 11 ):
    print(num, 'x ', a, '=', num* a)


x = 1
while(x<=100):      #while loop
    print(x)
    x = x+1



#Functions
def demo():     #Derining a runction
    print("Hlo Guys")
    print("It's my First Function")
    print(" : )")

demo()      # Calling a runction

def add(a,b):        #Derining Function
    c = a+b
    return c

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

z = add(x,y)        #Calling Function
print("The Sum is", z)


