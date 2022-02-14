####Program to check if a number is a palindrome

#Asking For Input of number from user
num = int(input("Please Enter A Number: "))

#First Defining Reverse Number Function

#Defining Function for Sum of digits entered by user

def rev_no(x):
    a = 0
    while x!=0:
        rev = x%10
        a = a*10+rev
        x = x//10
    return a

#Now defining palindrome function

def pal(x):
    if rev_no(x)==x:
        return "Its A Palindrome"
    else:
        return "Its Not A Palindrome."

#Driver Code

print(pal(num))
                      
