#Program to find odd or even numbber 

#Defining ODE function:

def ode(x):
    if x%2==0:
        return "Its Even"
    else:
        return "Its Odd"
    
#Asking For Input
x = int(input("Please Enter A Number: "))

#GettingOutput
print(ode(x))                                                                                                                                                                                                                
                                        
