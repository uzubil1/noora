def forLoop():
    for i in range(0,11):
        print(i,end=" ")
    print()

    for i in range(0,21):
        if i%2==0:
            print(i,end=" ")
    print()

    for i in range(5,16):
        if i%2!=0:
            print(i,end=" ")
        print()
    
    for i in range(10,-1,-1):
        print(i,end=" ")
    print()


def lent(): #!
    a_range = range(1, 10 ,3)

    print(len(a_range))

def rangeFct(rangeAmount):
    lenght = len(rangeAmount)
    for i in range(lenght):
        print(rangeAmount[i])



def main():
    rangeFct(range(0,11))
    rangeFct(range(10,-1,-1))

if __name__ == "__main__":
    main()
    

