
import time




def generated_sort_data(size):
    for i in range(1, len(size)):
        while i > 0 and size[i] < size[i - 1]:
            size[i - 1], size[i] = size[i], size[i - 1]
            i = i - 1

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

def main():
    small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]

    
    generated_sort_data(small_data)
    print("Sorted Data:", small_data)
   
    
    target_1 = 29
    start_time = time.perf_counter()
    index_1 = binary_search(small_data, target_1)
    end_time = time.perf_counter()
    print(f"Index of {target_1}: {index_1}")
    print(f"Time taken for binary search of {target_1}: {end_time - start_time:.6f} seconds")
    


    target_2 = 100
    start_time = time.perf_counter()
    index_2 = binary_search(small_data, target_2)
    end_time = time.perf_counter()
    print(f"Index of {target_2}: {index_2}")
    print(f"Time taken for binary search of {target_2}: {end_time - start_time:.6f} seconds")

    
    


main()
