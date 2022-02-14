# Program to replace elements at even postition at "##"

#Defining the replace function

def rep(x):
    #Initialising an empty string
    out = ""

    #Settign up for loop until len(string)
    for i in range(0, len(x)):  
        #Replacing the values t even positions with ##
        if i%2==0:
            out =  out+ "##"
        #Inputting original values at odd positions
        else:
            out = out + x[i]
    #Returning output string
    return out

#Driver Code

string = str(input("Please Enter A String: "))
assert len(string)>=1
print(rep(string))
~                       
