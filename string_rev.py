#### Program To Reverse a String

#Asking For Input
string = str(input("Please enter a string: "))

#Defining Reverse Function

def rev(x):
    #Initiating an empty string
    rev = ''
    #Starting Loop to get all char in string
    for i in range(0, len(x)):
        #Adding chars in rev order
        rev = string[i] + rev
    return rev

#Output

print(rev(string))

#### Program to Reverse A String Using For String Methods

#Ask for input

string = str(input("Please Enter A String: "))

#Reverse String
print(string[::-1])

