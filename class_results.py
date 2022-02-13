#### Program To get Marks of students in 3 subjects and do operations on them

#No. of Students In Class
s = int(input("Please enter the number of students in your class: "))

#Initialsing Varibles

stu_total = 0
stu_max = 0
stu_min = 1000
total,max_name, min_name = 0, 0, 0

#Driver Code

#Initiating Loop For All Students

for i in range(1, s+1):

    math, phy, chem = -1, -1 ,-1

    #Asking For Student Name 
    name = str(input("Please Enter The Student's Name: "))

    #Asking marks from each student
    while math<0 or math>100:
        math = int(input("Please Enter Marks in Mathematics Between 0 and 100: "))
    while chem<0 or phy>100:
        chem = int(input("Please Enter Marks in  Chemistry Between 0 and 100: "))
    while phy<0 or phy>100:
        phy = int(input("Please Enter Marks in Physics Between 0 and 100: "))

    #Printing Original Marks
    print("The marks you entered are:\nMathematics: ",math,"\nPhysics: ", phy,"\nChemistry: ", chem)

    #Student Average Marks
    stu_avg = (math+chem+phy)/3
    print("The student's average marks are: ", stu_avg)


    #Assigning Total Variable to Add mark in loop:
    total +=math+chem +phy

    #Maximum Marks
    stu_total = math+chem+phy
    if stu_total>stu_max:
        stu_max = stu_total
        max_name = name

    #Minimum Marks 
    if stu_total<stu_min:
        stu_min = stu_total
        min_name = name

#Calculating Class Average and Printing Final Results

class_avg = total/s
print("The Class Average is: ")
print("The Maximuum marks are", stu_max, ", scored by", max_name)
print("The minimum marks are", stu_min ,",scored by", min_name)


