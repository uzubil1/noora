"""_summary_
In this Python Program, we are learning how to return 
a value and save it in a persistent storage variable
and access the value from the storageVariable
anywhere outside the function
We can use the results from one function in 
another arithmetic calculation
"""

def add(num1, num2):  
    sum= num1+ num2
    return sum    # return the sum which is 12


def main():
    num1= int(input("enter first num: "))
    num2= int(input("enter second num: "))
       
    addResult=add(num1, num2)# receive the result of add() and save
    print(addResult)

   
main()

