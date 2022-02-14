####Program to get reverse of a number  entered by user

#Asking For Input of number from user
num = int(input("Please Enter A Number: "))

#Defining Function for Sum of digits entered by user

def rev_no(x):
    a = 0
    while x!=0:
        rev = x%10
        a = a*10+rev
        x = x//10
    return a

#Driver Code

print(rev_no(num))


                                                        
              
