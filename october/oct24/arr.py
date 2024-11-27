



def insert_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1] > arr[j] and j > 0: #swopping condition
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-= 1
    return arr


arr = [2, 6, 5, 1, 3, 4]

arr1=insert_sort(arr)
print(arr1)