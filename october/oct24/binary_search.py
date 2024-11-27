import time


def binary_search(array_a,start,stop,target_value):
    #calculate the mid point
    mid = (start +stop)//2
    print("printingthe midpoint:",mid)
    if start>stop:
        return -1
    if array_a[mid] < target_value:
        return binary_search(array_a,mid+1,stop,target_value)
    elif array_a[mid] > target_value:
        return binary_search(array_a,start,mid-1,target_value)
    elif array_a[mid]== target_value:
        return mid


def main():
    array_a=[20,30,40,60,70,80,90]
    target_value=int(input('enter the value u want to search:'))
    begin=time.perf_counter()
    result = binary_search(array_a,0,len(array_a)-1,target_value)
    end=time.perf_counter()
    elapsed=end-begin
    if result ==-1:
        print('target value not found')
    else:
        print('target value found',array_a.index(target_value))

    print('***********printing time taken by binary search*********', elapsed)

main()