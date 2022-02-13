#### Program to print sum of series

#Asking for Input until which to continue the series
n = int(input("Please Enter a Number: "))

#Defining Series Function

#1/2+ 1/4 + 1/n series

def series1(x):
    t = 0
    for i in range(1, n+1):
        t += 1/(2*i)
    return t

#Driver Code

print(series1(n))
