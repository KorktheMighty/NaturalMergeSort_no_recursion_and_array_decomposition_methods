import time
import random
import tracemalloc

def natural_merge_sort(arr):
    tracemalloc.start()
    
    def merge(arr, left, right, end):
        temp = []
        i, j = left, right
        while i < right and j < end:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i < right:
            temp.append(arr[i])
            i += 1
        while j < end:
            temp.append(arr[j])
            j += 1
        arr[left:end] = temp
    n = len(arr)
    if n <= 1:
        return arr
    runs = [(start, start + 1) for start in range(0, n - 1, 2) if arr[start] > arr[start + 1]]
    sorted_runs = runs if len(runs) > 0 else [(i, i + 1) for i in range(n - 1)]
    while len(sorted_runs) > 1:
        next_runs = []
        for i in range(0, len(sorted_runs) - 1, 2):
            left, mid = sorted_runs[i]
            right, end = sorted_runs[i + 1]
            merge(arr, left, right, end)
            next_runs.append((left, end))
        if len(sorted_runs) % 2 == 1:
            next_runs.append(sorted_runs[-1])
        sorted_runs = next_runs
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return arr, current, peak

##########
#  MAIN  #
##########

# change the range value to effect array size
arr = [random.randint(0, 1000) for _ in range(500000)]
start_time = time.time()
sorted_arr, current_mem, peak_mem = natural_merge_sort(arr)
end_time = time.time()
print(f"Sorted array: {sorted_arr}")
print(f"Time taken: {end_time - start_time:.5f} seconds")
print(f"Current memory usage: {current_mem / 10**6:.5f} MB")
print(f"Peak memory usage: {peak_mem / 10**6:.5f} MB")
