


"""Create a text file in your filesystem 
write 3 num in separete lines 
"""


def file_sum(filepath):
     try:
        with open(filepath) as f:
            try:
                sum1 = 0
                for i in f:
                    each_number = i.split()
                    print(each_number)
                    for y in each_number:
                     sum1 = sum1 + int(y)
                print(sum1)
            except ValueError:
                print(" file has other than int")
            except TypeError:
                print("file has invalid data")
     except FileNotFoundError:
         print("invlid file pth")
    


def main():
    filepath = "/Users/uzubil/noora/number.txt"
    file_sum(filepath)


if __name__=="__main__":
    main()