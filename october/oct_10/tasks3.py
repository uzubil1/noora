


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age< 18:
        raise ValueError("u must be at least 18 y.o")
    else:
        print("Age is valid. u are allowed to proceed")
try:
    user_age = int(input("enter your age:"))
    check_age(user_age)
except ValueError as e:
    print(e)