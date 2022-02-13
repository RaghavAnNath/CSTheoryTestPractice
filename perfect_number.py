####Program to check if the number is a perfect number

#Asking For Number
num = int(input("Asking For Input: "))

##Defining Factor Function

#Defining An Empty List
fact = []

#Defining the Factor Function
def fac(x):
    for i in range(1,x+1):
        if x%i==0:
            fact.append(i)
    return fact

#Defining Perfect Number Function
def per(x):
    num_sum = 0

    for i in fac(x):
        if i!=x:
            num_sum += i
    print(num_sum)
    if num_sum==x:
        return "Its a perfect number."
    else:
        return "Its not a perfect number."

#Driver Code
print(per(num))
                      
