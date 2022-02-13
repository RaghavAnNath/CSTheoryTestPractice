#### Program to check if a number is prime number

#Asking For Input
num = int(input("Please Enter A Number: "))

#Defining the prime function

def prime(x):
    e =0
    for i in range(1, x):
        if x%i==0:
            e = e+1
        if e>1:
            break
    if e==1:
        return "Its a prime number."
    else:
        return "Its not a prime number."

#Driver Code


print(prime(num))
print("Its factors are", 1 , num)         
