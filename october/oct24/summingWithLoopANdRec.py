'''this python code will end up with numbers til 5 using loop and then recursion'''

def sum_with_loop(number):

    sum = 0
    for i in range(1, number +1):
        sum = sum +1 
    return sum

def sum_with_rec(number):
    if number==1:
        return 1
    else:
        return number + sum_with_rec(number +1)
def main():
    user_input = int(input('enter the number:'))
    result = sum_with_loop(user_input)
    print(result)
    rec_result=sum_with_rec(user_input)
    print(rec_result)

if __name__=="__main__":
    main()