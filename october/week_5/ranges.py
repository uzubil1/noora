

def rangeVal(start,stop): # 1 as start and 10 as stop

    index = 0 #index pointer

    a_range = range(start,stop + 1) #or we can put 11 in the main

    length = len(a_range)


    while index < length:
        print(a_range[index])  #if we want this in one line 

        index = index +1
    



    

def main():
    rangeVal(0,10)
    rangeVal(0,20)
    rangeVal(5,15)

if __name__ == "__main__":
    main()