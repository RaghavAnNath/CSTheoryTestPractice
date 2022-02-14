####Program To Print Out Fibonacchi Numbers

#Asking for input to get get the no. of numbers to be printed
num = int(input("Please Enter A Number: "))

#Defining Fibonacchi Function

def fib(x):
    #Define An Initial List With 0 and 1
    fib = [0, 1]
    for i in range(1, x+1):
        a = fib[i]+fib[i-1]
        fib.append(a)
    return fib

#Driver Code

print(fib(num))
                  
