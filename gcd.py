#### Program to print GCD of numbers using while loop

#Asking for the number

num1 = int(input("Please Enter A Number: "))
num2 = int(input("Please Enter A Number: "))

#Defining An Empty List
fact = []
#Defining the Factor Function

def fac(x,y):
    i= 1
    while i<=min(x,y):
        if y%i==0 and x%i==0:
            fact.append(i)
        i += 1
    return fact

#Output
print(fac(num1, num2))
         
  
  
  
#### Program to print factor of a number using lists 
#Asking for the number

num1 = int(input("Please Enter A Number: "))
num2 = int(input("Please Enter A Number: "))

#Defining An Empty List
fact = []
#Defining the Factor Function

def fac(x,y):
    for i in range(1,min(x,y)+1):
        if y%i==0 and x%i==0:
            fact.append(i)
    return fact

#Output

print(fac(num1, num2))
                             
                           
