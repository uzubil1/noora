def add(number1, number2):
    result=number1+ number2
    return result

def subtract(number1, number2):
    result=number1- number2
    return result


def multiply(number1, number2):
    result=number1* number2
    return result


def divide(number1, number2):
    result=number1/ number2
    return result
    
def main():
    num1= int(input("enter first numeric value: "))
    num2= int(input("enter second numeric value: "))
    
    addVar=add(num1,num2 )
    SubtVar=subtract(num1,num2)
    multipVar=multiply(num1,num2)
    divVar= divide(num1,num2)
    
    print(addVar)
    print(SubtVar)
    print(multipVar)
    print(divVar)
    
main()
    