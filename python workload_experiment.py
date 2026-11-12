# import the time module to measure excution time
import time
#test 3 different workload sizes
for n in [10000, 100000, 1000000]:
    #record the starting time 
    start = time.perf_counter()
    #initialise the sum to 0 
    total = 0
    # add all number from 1 to n 
    for i in range(1, n+1):
        total = total + i 
    #record the ending time
    end = time.perf_counter()
    # calculate the total execution time
    execution_time= end - start 
    print("Numbers added:", n)
    print("Sum:", total)
    print("Time taken:", execution_time, "seconds")