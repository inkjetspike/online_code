#First I'm going to do a little string manipulation
#Super awesome time with strings
first_string = "Durell Hart"

#print the length of the string
print("The first string is %d characters long." % len(first_string))

#Make the string upper case
print(first_string.upper())

#Make the sting lower case
print(first_string.lower())

#I'm going to find the position(index) of a letter within the string
print("The position of 'u' is %d." %first_string.index('u'))
#I'm going to find the position(index) of a capitalized letter by changing the string to upper case
print("The position of capital 'r' is %d." % first_string.upper().index('R'))

#Now I'm going to count the number of r's
print("There are %d letter r's in %s" %(first_string.count("r"),first_string))
#Now I'm going to count the number of capital L's
print("There are %d letter L's in %s" %(first_string.upper().count("L"),first_string))

#Now I'm going to do some slicing a.k.a. slice the string
print(first_string[3])#print the 3rd character only
print(first_string[1:8])#print out the characters 1-8
print(first_string[1:len(first_string)])


#Split the string (very useful)
name= "Durell Hart"
print(name.split(" "))
# OR
name1 = "Kimberly Hart"
myList=name1.split(" ")
print(myList)
print("My first name is %s and my last name is %s" %(myList[0], myList[1]))