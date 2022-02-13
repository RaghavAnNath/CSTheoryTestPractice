#### Programs To Print Various Patterns Using For Loops

#Asking for input for a number
n = int(input("Please Enter A Number: "))

#Right Triangle Pattern 

def righttriangle(n):
  for i in range(1, n+1):
      for j in range(1, i+1):
          print('*', end='')
      print()


# Right Triangle With Numbers

def num_righttriangle(n):
  for i in range(1, n+1):
      for j in range(1, i+1):
          print(i, end='')
      print()


#Rectangle Pattern 

def rect(n):
    for i in range(n):
        print('*'*4)


# Right Triangles With Alphabets
def alpha_tri(n):
    for i in range(1, n+1):
        for j in range(65, 65+i):
            print(chr(j), end='')
        print()

#Driver Code
 
righttriangle(n)

num_righttriangle(n)

rect(n)

alpha_tri(n)
