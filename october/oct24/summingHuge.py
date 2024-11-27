

'''This python code will calculate the time for a huge summation operation '''


import time

sum = 0


#calculate the time it takes to sum the number till 1 mil

begin = time.perf_counter( )

for i in range(1000000):
    sum = sum + i



end = time.perf_counter()
elapsed_time = end- begin 
print(elapsed_time)