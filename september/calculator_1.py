"""This program is to code ACtivity 3.2.2
Return results from the functions to the calling place
print the results"""

pi= 3.14

def circumference(radius):
    circumf= 2 * pi * radius
    return circumf

def area_of_circle(radius):
    area_of_circle= pi * radius **2
    return area_of_circle




def addNumbers(x, y):
    add= x+y
    return add

# You just need to define 3 more functions and call them in main()
    
def subtractNumbers(x, y):
    subtract= x-y
    return subtract

def multipNumbers(x, y):
    multipResult= x*y
    return multipResult

def divNumbers(x, y):
    divResult= x/y
    return divResult
    
def main():    
    num1=int(input("enter first number: "))
    num2= int(input("enter second number: "))
    
    addResult= addNumbers(num1, num2)
    print("addition:" ,addResult)
    
    result2= subtractNumbers(num1, num2)
    print("subtraction: ", result2)
    
    result3= multipNumbers(num1, num2)
    print("Multiplication: ", result3)
    
    divResult= divNumbers(num1, num2)
    print("Division ", divResult)
    
    
    '''
    Calling of the function in main()
    In the code below, I need to call circumference function to calculate circum of circle
    For that I need to pass radius
    SO I take the value of radius from user and pass it to circumference function
    I get the results back and save it in a variable circumfResult
    '''
    radius= int(input("enter the value of radius: "))
    circumfResult= circumference(radius)
    print(circumfResult)
    
    circleArea= area_of_circle(radius)
    print(circleArea)
    
    
   
     
main()