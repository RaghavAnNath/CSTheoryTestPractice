#Program to find matching characters in string 

#Asking for input of strings

str1 = str(input("Please Enter a string: "))
str2 = str(input("Please Enter A String: "))
str3 = str(input("Please Enter A string: "))

#Defining match function:

def match(x, y,z):
    l = []
    for i in str1:
        if i in str2 and i in str3 and i!=' ':
            l.append(i)
    return l

#Output
print(match(str1, str2, str3))
