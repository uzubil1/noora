import random

# Creating a fixed-length array with initial values
array = [1, 2, 3, 4, 5]

# Shuffling elements in the array using the random module
random.shuffle(array)
print("Shuffled Array:", array)

# Selecting a random element from the array
random_element = random.choice(array)
print("Random Element:", random_element)




# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: 120





def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  # Return the index of the found element
    return -1  # If target is not found

array = [10, 20, 30, 40, 50]
print("Index of 30:", linear_search(array, 30))  # Output: 2



def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # If target is not found

sorted_array = [10, 20, 30, 40, 50]
print("Index of 40:", binary_search(sorted_array, 40))  # Output: 3




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array = [12, 11, 13, 5, 6]
insertion_sort(array)
print("Sorted Array:", array)  # Output: [5, 6, 11, 12, 13]
