def hashing_func(setA):
    print(f"the set we r getting is {setA}")


    for i in setA:
        print(f"the hash for {i} is {hash(i)}")


    index_size = 10

    for i in setA:
        index = hash(i) % index_size
        print(f"the index for{i} is {index}")



def main():
    setA = {1,2,3,4,5,6,7,8,9,"a","g"}
    hashing_func(setA)

main()