import time
import random
from datetime import datetime
from pagoda import Pagoda

def batch_operations(pagoda, num_operations):
    #Perform a batch of insert and delete operations and measure the total times
    total_insert_time = 0
    total_delete_time = 0

    # Measure how long it takes to perform num_operations inserts in a Pagoda of depth x
    # and calculate the total time per trial
    for i in range(num_operations):
        start_insert = time.perf_counter()
        pagoda.insert(random.randint(1, 1000000))
        end_insert = time.perf_counter()
        total_insert_time += end_insert - start_insert

    # Measure how long it takes to perform num_operations deletions in a Pagoda of depth x
    # and calculate the total time per trial
    for i in range(num_operations):
        if not pagoda.isEmpty():
            start_delete = time.perf_counter()
            pagoda.delete()
            end_delete = time.perf_counter()
            total_delete_time += end_delete - start_delete
    #return these times
    return total_insert_time, total_delete_time

def test_pagoda_operations(depth, num_operations, num_trials, filename):
    start_test = time.perf_counter()
    pagoda = Pagoda()

    # Pre-build the Pagoda to the desired initial depth using randomly generate ints
    for i in range(depth):
        pagoda.insert(random.randint(1, 1000000))
    #initialize the trial
    total_insert_time = 0
    total_delete_time = 0
    #perform each trial
    for i in range(num_trials):
        insert_time, delete_time = batch_operations(pagoda, num_operations)
        total_insert_time += insert_time
        total_delete_time += delete_time
    end_test = time.perf_counter()
      # Calculate total time for this depth
    total_test_time = end_test - start_test

    # Write results to file with a timestamp
    avg_insert_time_per_trial = total_insert_time / num_trials
    avg_delete_time_per_trial = total_delete_time / num_trials

    # Write results to file with a timestamp
    with open(filename, 'a') as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\nTest Run at {current_time}\n")
        file.write("-" * 50 + "\n")
        file.write(f"Depth: {depth}, Trials: {num_trials}, Operations per Batch: {num_operations}\n")
        file.write(f"Average Insert Time per Trial: {avg_insert_time_per_trial:.5f}s\n")
        file.write(f"Average Delete Time per Trial: {avg_delete_time_per_trial:.5f}s\n")
        file.write(f"Total Time for Test: {total_test_time:.5f}s\n")
        file.write("-" * 50 + "\n")

        print(f"Depth: {depth}, Total Time for Test: {total_test_time:.5f}s, Average Insert Time per Trial: {avg_insert_time_per_trial:.5f}s, Average Delete Time per Trial: {avg_delete_time_per_trial:.5f}s")

def main():
    depths = [100000, 250000, 500000, 750000, 1000000, 1250000, 1500000, 1750000, 2000000, 2500000, 5000000, 10000000]
    num_operations = 10000  # Define the number of operations per batch here
    num_trials = 30       # Define the number of trials here
    filename = "pagoda_performance_tests.txt"
    for depth in depths:
        test_pagoda_operations(depth, num_operations, num_trials, filename)

if __name__ == '__main__':
    main()



