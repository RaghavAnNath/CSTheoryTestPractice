#### Program to change a given temperature into other units

#Defining Function For  Celsius Temperatures
def celsius(x):

    #Output in Kelvin
    a = x - 273
    #Output in Farenheit
    b = 1.8*x+32

    return "The output in farenheit is", b, " The output in Kelvin is", a

def kelvin(x):
    
    #Output in celsius 
    a = x+273
    #Output in fareheit
    b = (x-273)*1.8+32
    
    return "Output in Farenheit is" ,b , " Output in Celcius is", a


def farenheit(x):
    #Output in Celsius
    a = (x-32)/1.8
    #Output in kelvin
    b = (x-32)/1.8+273
   
    return "Output in Kelvin is", b," Output in Celsius is ",a


#Asking For Input 

x = int(input("Please Enter the temperature: "))
y = str(input("Please Enter the unit of the temperature given: "))
y = y.lower()

#Output According to the type of temp in input
if y=="celsius" or y== "c" or y== "cel":
    print(celsius(x))
elif y=="kelvin" or y== "k" or y== "kel":
    print(kelvin(x))
elif y=="farenheit" or y=="f"or y== "far":
    print(farenheit(x))
