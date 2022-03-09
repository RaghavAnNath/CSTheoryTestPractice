#Defining The Stack

class Stack:

    #Initialising and empty stack
    def __init__(self):
        self.list = []

    #Push Methods
    def push(self, element):
        self.list.append(element)

    #Get Method 
    def get(self):
        return self.list[-1]

    #Pop Method 
    def pop(self):
        while len(self.list)!=0:
            return self.list.pop()

    #Size Method 
    def size(self):
      return len(self.list)

#Function To Read The Input From a String

def strtolist(input):
  return list(input)

#Making A Precendece Order Dictionary 
dict = {"+":1,"-":1,"*":2,"/":2,"//":2,"%":2,"**":3}

#Creating A Stack Object 

stack = Stack()

#Post Fix Function

def postfix(inputlist, stack):
  
  #Starting An Empty Output List
  outlist = []
  #Starting Loop For The Elements In The String List
  for i in range(0, len(inputlist)):
 
    #Since the operators cannot be present at the start and at the end it means that all the even indexes in the string are numbers
    if i%2==0:
      outlist.append(int(inputlist[i]))
    #Popping Out All Elements In Stack At The End
      if i == (len(inputlist)-1):
        while stack.size()!=0:
          outlist.append(stack.pop())



    #Pushing The First Operator In the Stack  
    elif i==1:
      stack.push(inputlist[i])

    #Checking For Other Operators

    else:
      oper = dict.get(inputlist[i])
      while oper <= dict.get(stack.get()):
        outlist.append(stack.pop())
        if stack.size()==0:
          break
      stack.push(inputlist[i])

      if oper > dict.get(stack.get()):
        stack.push(inputlist[i])

  #Returning Output List  
  return outlist


#Asking For Input
inputstr= input("Please Enter The Operation")
a = strtolist(inputstr)
print(a)
print(postfix(a,stack))


