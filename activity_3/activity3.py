import random
import array
import time

# Phase 1
def generated_sort_data():
    inp_user = int(input('Enter 1 if you want elements till 100 (and perform insertion sort) and 2 if you want elements till 1000'))
    if inp_user == 1:
        inp_u_no = int(input("Enter the number of elements in the Array : "))
        size = array.array('i',[random.randint(1, 100) for _ in range(inp_u_no)])
        for i in range(1, len(size)):
            while i > 0 and size[i] < size[i - 1]:
                size[i - 1], size[i] = size[i], size[i - 1]
                i = i - 1
        return size
    elif inp_user == 2:
        ar1 = array.array('i',[random.randint(1, 100) for _ in range(1000)])
        return ar1
    else:
        return None
# Phase 2
def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid 
        elif sorted_array[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    
    return None  


# Phase 3
def merge(left, right):
    new = []
    i = j = 0

    for k in range(len(left) + len(right)):
        if i < len(left) and (j >= len(right) or left[i] < right[j]):
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    return new

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def linear_search(ar2,target_1):
    for i in ar2:
        if i == target_1:
            print(f"Index is : {i}")
            return i
        else:
            print("Number is not found")
            return None

def main():
    x = generated_sort_data()
    print("Sorted Data:", x)
    
    target_1 = 29
    target_2 = 100
    
    index_1 = binary_search(x, target_1)
    index_2 = binary_search(x, target_2)
    
    print(f"Index of {target_1}: {index_1}")
    print(f"Index of {target_2}: {index_2}")

    y = generated_sort_data()
    print(merge_sort(y))

    z = generated_sort_data()

    target1 = int(input("Enter the target"))
    begin1 = time.perf_counter()
    result1 = linear_search(z,target1)
    end1 = time.perf_counter()
    time1 = end1-begin1
    print(f"The result is : {result1} and the time taken is : {time1}")

    begin2 = time.perf_counter() 
    result2 = binary_search(z, target_1)
    end2 = time.perf_counter()
    time2 = end2-begin2
    print(f"The result is : {result2} and the time taken is : {time2}")

if __name__=="__main__":
    main()