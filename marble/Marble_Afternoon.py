#Dictionaries

#Used to store data values in key:value pairs
#Dictionaries

myDict ={
    "phone": "iphone",
    "iphone model": "iphone 15",
    "Year": "2023",
}

print(myDict)

#Length of a dictionary
print(len(myDict))
#Data type
print(type(myDict))
#Access a dictionary data items
z= myDict["Year"]
print(z)

y= myDict.get("iphone model")
print(y)

m=myDict.keys()
print(m)

#Exercise One: Use the values() method to return a list of all values in the dictionary
#Exercise Two: To check if a key does exist in your dictionary
#Exercise three: Give an example on how to change dictionary items, how to update
#Exercise four: Give an example on how to add dictionary items, how to remove dictionary items
#Exercise five: Give an example on how you can loop thru a dictionary and also how to nest dictionaries

#Using the values() to return a list of all values
print(myDict.values())

#Checking if a key exists in a dictionary
print(myDict.get('Make', 'Not Found'))

#Changing a dictionary item
myDict['iphone model']= 'iphone 13'
print(myDict)

#Updating a dictionary 
myDict.update({"phone": "Samsung", "Samsung model": "Note20 Ultra", "Year":"2021"})
print(myDict)

#Adding an item to the dictionary
myDict['Make']= 'USA'
print(myDict)

#Removing an item from the dictionary
del myDict['Make']  
print(myDict)

#Alternative can be using the pop method as follows.
popped= myDict.pop('Year')
print(myDict)
print(popped)

#Looping through a dictionary
for keys, values in myDict.items():
    print(keys, values)


#Numbers(integers, floats, complex)
w=10 #int
r= 3.9 #float
s= 2j #Complex

print(type(s))

#Integers

a=2
b= 5624378963
c= -56375

print(type(a))
print(type(b))
print(type(c))

#floats
g= 2.89
z=3.3
e= -76.903
print(type(e))

#Complex Numbers
w= 6 + 10j
t= 4j
h= -2j

print(type(h))

#Type conversions
w= 10 #int
r= 3.9 #float
s= 2j #complex

#Convert from int to complex

z= complex(w)
print(z)
print(type(z))

# convert from int to float
# convert from float to complex
# convert from complex to float(Gives a type error if you try to convert using the float())

p= float(w)
print(p)
print(type(p))

q= complex(3.9)
print(q)
print(type(q))

k=int(s)
print(k)
print(type(k))

#Casting
#Works mostly when you want to specify a variable type

# h= int(20) #h is 20 
# y= int(30000000) #y is 30000000
# a= int("8") #a is 8

# #Strings 
# print("Afternoon")
# print('Afternoon')

# #Assign string to a variable
# w= "Afternoon"
# print(w)

# #multiline strings
# q= """I am offering BSSE Year three
# Currently doing recess in python,
# Data Science, Django
# """
# print(q)

# #Strings as arrays

a="Afternoon"
print(a[0])

#Exercise: Use the len() function to determine the length of your string
#Exercise2: Use a for loop in a string
#Exercise3: Give an example of slicing in strings

#len() function on string
print(len(a))

#for loop on string
for item in a:
    print(item)

#slicing in strings
print(a[2:8])


#format string
#Works when one wants to combine a string to a number
#We need to use the format() method
#The format () takes the passed parameters, formats them and places them in the string where the place holders{} are

age= 23

name= "My name is Livingstone, I am " + age#(Gives an error so we use the format())
print(name)

name= "My name is Livingstone and I am {}"
print(name.format(age))



# #Booleans
# #These evaluate to a true or false

print(20 < 10)
print(bool(15))

#Exercise:Use a conditional statement to show how to use boolean
if 20<10:
    print("It is a very wrong assumption")
elif 20>10:
    print("It is a right assumption for this and we agree")
else:
    print("None of the two")

#Alternative two with a variable
y=20
if y<20:
    print("This is right boss")
elif y>20:
    print("Can also be right if we change initial value of y")
else:
    print("Then y is equal to 20")

