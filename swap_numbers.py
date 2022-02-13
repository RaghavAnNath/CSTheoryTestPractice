#### Program to Swap Numbers With 3rd Variable ####

#Asking For Input
n = int(input("Please Enter A Number"))
m = int(input("PLease Enter A Number"))
 
#Printing Original Sequence
print("The original sequence was", n, m)
 
#Driver Code 
#Shifting Variable Values
temp = n
n = m
m = temp

#Printing New Sequence
print("The new sequence is", n, m)
                                                                                                                                                                                                                
                                        
#Program to Swap Numbers Without 3rd Variable ####

#Asking For Input
x = int(input("PLease Enter A Number"))
y = int(input("PLease Enter A Number"))

#Printing Origninal Sequence 
print("The original sequence was", x, y)

#Driver Code
x, y = y, x

#New Sequence
print("The new sequence is", x, y)


#### Program To Swap Numbers Using Multiplication

#Asking For Input
x = int(input("PLease Enter A Number"))
y = int(input("PLease Enter A Number"))

#Printing Origninal Sequence 
print("The original sequence was", x, y)

#Driver Code
x = x*y
y = x/y
x = x/y

#New Sequence
print("The new sequence is", int(x),int( y))


#### Program To Swap Numbers Using Addition

#Asking For Input
x = int(input("PLease Enter A Number"))
y = int(input("PLease Enter A Number"))

#Printing Origninal Sequence 
print("The original sequence was", x, y)

#Driver Code
x = x+y
y = x-y
x = x-y

#New Sequence
print("The new sequence is", int(x),int( y))
