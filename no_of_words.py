#Programs to dislpay no. of words in a sentence 

#Asking For Input String
string = str(input("Please Enter A String: "))

#Defining Function to count no. of word

def countw(x):
    #Initialsing count variable
    count = 1
    for i in range(0,len(x)):
        if x[i]==' ' and x[i+1]!=' ':
            count += 1
            
    return count

#Output

print(countw(string))
                      
