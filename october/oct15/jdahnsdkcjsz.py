
def func_1(x, n):
    result = 1
    if n > 0:
        for _ in range(n):
            result *= x
    elif n < 0:
        for _ in range(-n):
            result /= x
    else:
        result = 1  
    print(f"func_1 is running: {x}^{n} = {result}")
    return result


def func_2(a, b):
    result = a**b+b**a
    print(f"func_2 is running: {a}^{b} + {b}^{a} = {result}")


func_1(2,3)
func_1(3,2)
func_2(2, 3)  