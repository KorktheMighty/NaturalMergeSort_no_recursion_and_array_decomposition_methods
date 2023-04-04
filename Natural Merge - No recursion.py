import time
import random
import tracemalloc

def natural_merge_sort(arr):
    tracemalloc.start()
    
    def merge(arr, start1, end1, start2, end2):
        merged = []
        i = start1
        j = start2
        while i < end1 and j < end2:
            if arr[i] < arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1
        while i < end1:
            merged.append(arr[i])
            i += 1
        while j < end2:
            merged.append(arr[j])
            j += 1
        for k in range(start1, end2):
            arr[k] = merged[k-start1]
    
    n = len(arr)
    runs = []
    start = 0
    while start < n:
        end = start + 1
        while end < n and arr[end-1] <= arr[end]:
            end += 1
        runs.append((start, end))
        start = end
    while len(runs) > 1:
        merge_runs = []
        for i in range(0, len(runs), 2):
            if i+1 < len(runs):
                start1, end1 = runs[i]
                start2, end2 = runs[i+1]
                merge(arr, start1, end1, start2, end2)
                merge_runs.append((start1, end2))
            else:
                merge_runs.append(runs[i])
        runs = merge_runs
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return arr, current, peak


##########
#  MAIN  #
##########


# change the range value to effect array size
arr = [random.randint(0, 1000) for _ in range(500000)]
print(arr)
print()
start_time = time.time()
sorted_arr, current_mem, peak_mem = natural_merge_sort(arr)
end_time = time.time()
print(f"Sorted array: {sorted_arr}")
print(f"Time taken: {end_time - start_time:.5f} seconds")
print(f"Current memory usage: {current_mem / 10**6:.5f} MB")
print(f"Peak memory usage: {peak_mem / 10**6:.5f} MB")
