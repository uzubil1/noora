

def ForLoopUsingRange():


    #range function with one parameter,will start from 0 and will exclude the last number
    for i in range(10):
        print(i) #if i want same line (i, end = "")
    print()



    #range function can take 2 parameters, start and stop but will exclude the last number 
    for i in range(2,10):
        print(i)
    print()
    



    #range function can take 3 parameters,star,stop(exclude the last num) end
    for i in range(0,10,2):
        print(i)
    print()

#withoutloop
def rangeFtn():
    seqNumber= range(6)

    print(seqNumber[0])
    print(seqNumber[1])
    print(seqNumber[2])



def main():
    ForLoopUsingRange()
    rangeFtn()

if __name__=="__main__":
    main()
