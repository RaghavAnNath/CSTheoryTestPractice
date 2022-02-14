#### Program to output occurances of substring in a string

#Ask for Input String
string = str(input("PLease Enter A String: "))
char = str(input("Please enter a char or string which you want to check: "))

#Driver Code
a = string.count(char)

#Output 

print("Total No. Of Occurances Of Substring: ",a)



#### Program to Count Occurances of Vowel in A String

string = str(input("PLease Enter A String: "))
string = string.lower()

vowels = ['a', 'e', 'i', 'o', 'u']
#Driver Code
p = 0
for i in string:
    if i in vowels:
        p += 1 
        
#Output
print(p)



#### Program to count vowels using for conditions

#Asking for input string
string = str(input("PLease Enter A String: "))
string = string.lower()

vowel ='aeiou'
count = 0

for i in string:
    if i in vowel:
        count += 1

#Output
print(count)
                                                                                                                           
