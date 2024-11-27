def square(num):
    return num * num

def sum(num1,num2):
    res1= square(num1)
    res2=square(num2)
    return res1 + res2

def main():
    num1= int(input("enter the number:"))
    num2 = int(input("enter the number:"))
    result = sum(num1,num2)
    print(result)  

main()
