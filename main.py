import matplotlib.pyplot as plt
import numpy as np

import sorting
import random_list
import wait


# n_values = list(range(100, 1001, 100))
n_values = list(range(0, 151, 10))  


#lists to store timing results
merge_sort_times = []
insertion_sort_times = []

for n in n_values:
    data = random_list.generate_random_list(n, seed=42)  #use a fixed seed for reproducibility
    
    merge_time = wait.time_sort(sorting.merge_sort, data, number=1000)
    merge_sort_times.append(merge_time)
    
    insertion_time = wait.time_sort(sorting.insertion_sort, data, number=100)
    insertion_sort_times.append(insertion_time)
    
    print(f"n={n}: Merge Sort={merge_time:.6f}s, Insertion Sort={insertion_time:.6f}s")

plt.figure(figsize=(10, 6))
plt.plot(n_values, merge_sort_times, label='Merge Sort', marker='o')
plt.plot(n_values, insertion_sort_times, label='Insertion Sort', marker='s')
plt.xlabel('Input Size (n)')
plt.ylabel('Average Time (seconds)')
plt.title('Merge Sort vs Insertion Sort Performance')
plt.legend()
plt.grid(True)
plt.savefig('sorting_performance.png') 
plt.show()

