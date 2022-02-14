####Program to get sum of digits entered by user

#Asking For Input of number from user
num = int(input("Please Enter A Number: "))

#Defining Function for Sum of digits entered by user

def sum_digit(x):
    a = 0
    while x!=0:
        rev = x%10
        a = a+rev
        x = x//10
    return a

#Driver Code

print(sum_digit(num))
