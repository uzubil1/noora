def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
    

def main():
    number = 10
    x = factorial(number)
    print(f"The factorial is {x}")

main()