

import arrays as a  

def linear_search(an_array, target):
   
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None 

def main():
   
    array_d = a.Array(100)
    
  
    for i in range(100):
        array_d[i] = i + 1
    
    
    targets = [1, 50, 100, 101] 
    
    for target in targets:
        result = linear_search(array_d, target)
        if result is not None:
            print(f"Target {target} found at index: {result}")
        else:
            print(f"Target {target} not found.")


if __name__ == "__main__":
    main()
