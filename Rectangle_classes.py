#### Write A Program To Implement A Class For Finding Area an Perimeter Of A Rectangle. Wrtie Constructor, Destructor and Functions For Calculating Area and Perimeter.


#Defining A Class
class Rectangle:
    #Initiating Varible For Counting No. Of Objects of the Class
    count = 0

    #Constructor
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1

    #Area Function
    def area(self):
        return self.length*self.breadth
    
    #Perimeter Function
    def perimeter(self):
        return 2*(self.length*self.breadth)
    
    #Destructor
    def __del__(self):
        Rectangle.count -= 1
    
    #Str Function
    def __str__(self):
        return "Length: "+ str(self.length)+ "Breadth: "+ str(self.breadth)
    
    #Function To Get Count 
    def getcount(self):
        return Rectangle.count

#Creating Objects

r1 = Rectangle(12, 24)
r2 = Rectangle(23,23)
r3 = Rectangle(45, 46)

#Using The Class Functions

print("Area: ",r1.area())
print("Perimeter:", r1.perimeter())
print("Count", r2.getcount())

#Asking which rectangle to delele
a
d = input("Please Enter A String Which is To Be Deleted: ")  
if d == "r1":
  del r1
  print("You deleted: " + d)
elif d =="r2":
  del r2
  print("You deleted: " + d)
elif d == "r3":
  del r3
  print("You deleted: " + d)
else:
  print("You have entered an invalid input")  
