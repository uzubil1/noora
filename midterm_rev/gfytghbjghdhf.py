"""import math
PI = math.pi


def cone_volume(radius,height):
    v = (PI * int(height) * int(radius) * int(radius))/3
    print("Volume if cone is:\t", v)


def main():
    radius = input("Enter the radius of the cone:")
    height = 4
    cone_volume(radius, height)

if __name__ == "__main__":
    main()
"""


'''import re
str = "GCIS-123 is so fun"
pattern = "[a-k]"
out = re.findall(pattern, str)
print(out)'''

'''x = 6
y = x % 3
print (y)
y = y ** 2
print (y)
d = 5 * y / 10
print (d)'''


def func(x,n):
    v = x**n 
    print(f"func is running: {x} ^ {n} = {v}")
    return v


v1 = func(1, 3)
v2 = func(2, 3)
v2 = func(2, -1)