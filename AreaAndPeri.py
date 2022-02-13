####Program to Calcuate Area and Perimeter of Different Figures

#Asking For Figure
figure = str(input("What do you want to calculate the area for: "))

#Defining Functions For Rectangle
def RArea(x,y):
    a = x*y
    return a
def RPeri(x,y):
    p = 2*(x+y)
    return p

#Defining Functions For Circle
def CArea(r):
    a = 3.14*r**2
def CPeri(r):
    p = 2*3.14*r
    
#Defining Functions For Square

def SArea(x):
    a =x**2
def SPeri(x):
    p = 4*x
    
#Asking For Input For Dimensions

if figure == "Rectangle" or figure == "Rec" or figure == "r":
    x = int(input("Enter dimensiion of one side: "))
    y = int(input("Enter dimension of other side: "))
    
    print("Area is: ",RArea(x,y))
    print("Perimeter is: ",RPeri(x,y))
    
if figure  == "Circle" or figure  == "C" or figure == "c":
    r = int(input("Enter the radius: "))
    print("Area is: ",CArea(r))
    print("Perimeter is: ",CPeri(r))
    
if figure == "Square" or figure == "s" or figure == "S":
    x = int(input("Enter The Side: "))
    print("Area is: ",SArea(x))
    print("Perimeter is: ",SPeri(x))
    
~                                              
