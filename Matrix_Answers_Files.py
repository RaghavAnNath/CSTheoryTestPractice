#### Program to check dimension of matrix for addition and subtraction

def check_add_sub(x,y):
  #Checking if the number of rows are equal

      #Initiating conditonal variable of while loop to false
      i = False

      #Initiating While Loop
      while i != True:

          #Checking length of the list which represents number of rows
          if len(x)==len(y):
              print("The rows of the matrix are okay.")

              #If the condition is satisfied, stopping the while loop by changing the condtional variable
              i = True

          #Else condition which will will prompt to reenter the output
          else:
              print("These matrices cannot be added, Enter Valid Input: ")
              x =eval(input("Please Enter A Matrix: "))
              y =eval(input("Please Enter A 2nd Matrix."))

      #Checking if number of columns are equal

      #The reasoning is same as the row checking
      j = False
      while j != True:
          if len(x[0])==len(y[0]):
              print("The columns of the matrix are okay.")
              j = True
          else:
              print("These matrices cannot be added, Enter Valid Input: ")
              x =eval(input("Please Enter A Matrix: "))
              y =eval(input("Please Enter A 2nd Matrix."))


#### Function To Add Two Matrices

def matrix_add(x,y):

    #Initiating an empty output list
    result_add = []

    #Initiating list to append result rows
    appen_row = []

    #Initiating Loop for each element(row)
    for i in range(0, len(x)):

        #Initiating Loop for each column
        for j in range(0, len(x[0])):

            #Adding Values at same i-j positions
            v = x[i][j] + y[i][j]

            #Appending them to empty list
            appen_row.append(v)

        #Appending that list into the Result list as a row
        result_add.append(appen_row)

        #Resetting the intermediatary list to zero so as not append twice
        appen_row=[]

    #Returning the final output list

    return result_add


#### Function To Subtract Two Matrices

def matrix_sub(x,y):

    #Initiating an empty output list
    result_sub = []

    #Initiating list to append result rows
    appen_row2 = []

    #Initiating Loop for each element(row)
    for i in range(0, len(x)):

        #Initiating Loop for each column
        for j in range(0, len(x[0])):

            #Adding Values at same i-j positions
            v = x[i][j] - y[i][j]

            #Appending them to empty list
            appen_row2.append(v)

        #Appending that list into the Result list as a row
        result_sub.append(appen_row2)

        #Resetting the intermediatary list to zero so as not append twice
        appen_row2=[]

    #Returning the final output list

    return result_sub


# Defining The Function


def strings(y):

    # Asking For Input File Directory

    #Setting the inputted file as the file to read through
    with open(y,'r') as file:
      #Checking each line in file
        for line in file:
          #Reading Each Word 
          for word in line:
            #Splitting strings after every space in file 
              wordlist = line.split()
              return wordlist




#Defining File Write Function

def file_write(x,y):
    #Initilaising Varible To Print The Question Number Every Iteration
    z = 1

    #Starting the loop for every 2 places
    for i in range(0,len(x),2):
        
        #Opening the input file using the directory given
        with open(y,'a') as file:
            
            #Writing The Question Number And Answer Parts In File
            file.write("\n The Answer for Question "+ str(z)+": \n")

            #Evaluating individual matrices and using functions to add and subtract them 
            matrix1 = eval(x[i])
            matrix2 = eval(x[i+1])
            check_add_sub(matrix1,matrix2)
            addi = matrix_add(matrix1,matrix2)
            subt = matrix_sub(matrix1,matrix2)

            #Writing the added matrix 
            file.write(" Add:\n ")           
            #Writing the of individual entries in the addition column and separating them by space
            for i in range(0, len(addi)):
              for j in range(0, len(addi[i])):
                row  = str(addi[i][j])
                file.write(row+" ")
                #Adding A Line When Reaching the end of the row to move to next row
                if j == len(addi[i])-1:
                  file.write("\n")
              print()



            #Writing the subtracted matrix(The Logic is same as above. I tried making it into a function but it wasn't syncing well and values were being printed out of place)
            file.write("Subtract: \n")
            
            for i in range(0, len(subt)):
              for j in range(0, len(subt[i])):
                row  = str(subt[i][j])
                file.write(row)
                file.write(" ")  
                if j == len(subt[i])-1:
                  file.write("\n")
              print()

        #Incrementing the question counter
        z +=1

### Main Code

file_directory = eval(input("Please Enter The File Directory: "))
x = strings(file_directory)
file_write(x, file_directory)
                                  
