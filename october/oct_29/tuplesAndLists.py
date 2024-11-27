#create 2 tules print their elements ,check their mutability since they are immutable



'''
tupleA = ('a','b','c','d')
tupleB = ('hello',3.14, False,3,'x')


lenghtA = len(tupleA)
lenghtB = len(tupleB)
print(lenghtA)
print(lenghtB)


for i in range(lenghtA):
    print(tupleA[i])


print()

for j in range(lenghtB):
    print(tupleB[j])


tupleA[0]=3 #tuple is immutable , u cat change the tuple'''

def mutater(a_list, an_int):
    print("mutater:", an_int, a_list)
    an_int *= 5
    a_list[0] *= 5
    print("mutater:", an_int, a_list)

def main():
    an_int = 7
    a_list = [an_int]
    print("before:", an_int, a_list)
    mutater(a_list, an_int)
    print("after:", an_int, a_list)

main()
