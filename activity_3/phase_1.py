import random

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
       
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_sorted_data(size):
   
    random_data = [random.randint(1, 100) for _ in range(size)]
   
    insertion_sort(random_data)
    return random_data


small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
insertion_sort(small_data)
print("Sorted Data:", small_data) 




#phase 2


def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    while left <= right:
        mid = left + (right - left) // 2
       
        if sorted_array[mid] == target:
            return mid
       
        elif sorted_array[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
   
    return None


sorted_data = small_data  
target1 = 29
target2 = 100

index1 = binary_search(sorted_data, target1)
index2 = binary_search(sorted_data, target2)

print(f"Index of {target1}: {index1}")  
print(f"Index of {target2}: {index2}") 