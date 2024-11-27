import arrays as a



array_a = a.Array(10)


'''print("Array A:", array_a)
print("Element at index 3:", array_a[3])


for index in range(len(array_a)):
    array_a[index] = index * 5


print("Modified Array A:", array_a)

array_b = a.Array(5, "abc")

print("Array B:", array_b)'''



'''def while_fill(an_array):
   
    index = 0
    length = len(an_array)
    
   
    while index < length:
        an_array[index] = index
        index += 1

def main():
    array_a = a.Array(10)
 
    print( array_a)
    
   
    while_fill(array_a)
    
   
    print( array_a)
'''


def for_fill(an_array):
 
  for i in range(len(an_array)):
    an_array[i] = i
  return an_array

array_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original array:",array_a)
array_a = for_fill(array_a)
print("Modified array:",array_a)

def main():
    array_a = a.Array(10)
 
    print( array_a)
    
   
    for_fill(array_a)
    
   
    print( array_a)

if __name__=="__main__":
    main()