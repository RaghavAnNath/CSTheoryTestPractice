#### Program to find the factors of the numbers inputted by the user

#Asking for the number

num = int(input("Please Enter A Number: "))

#Defining An Empty List
fact = []
#Defining the Factor Function

def fac(x):
    for i in range(1,x+1):
        if x%i==0:
            fact.append(i)
    return fact

#Printing Output
print(fac(num))
