#Q1
import time
import matplotlib.pyplot as plt

# Iterative algorithm 
def iterative_sum(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return total

# Recursive algorithm 
def recursive_sum(N):
    if N == 1:
        return 1
    else:
        return N + recursive_sum(N - 1)

# Measure time taken for iterative approach
iterative_times = []
N_values = range(1, 1001, 10)  
for N in N_values:
    start_time = time.time()
    iterative_sum(N)
    end_time = time.time()
    iterative_times.append(end_time - start_time)

# Measure time taken for recursive approach
recursive_times = []
for N in N_values:
    start_time = time.time()
    recursive_sum(N)
    end_time = time.time()
    recursive_times.append(end_time - start_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('Value of N')
plt.ylabel('Time taken (seconds)')
plt.title('Time taken to compute sum of first N natural numbers')
plt.legend()
plt.grid(True)
plt.show()

#Q2
import time
import random
import matplotlib.pyplot as plt

array = [random.randint(1, 1000) for _ in range(10000)]
array.sort()  

# Linear search function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary search function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_search_time(search_function, arr, key):
    start_time = time.time()
    search_function(arr, key)
    return time.time() - start_time

search_keys = [random.randint(1, 1000) for _ in range(5)]
linear_search_times = []
binary_search_times = []

for key in search_keys:
    linear_search_times.append(measure_search_time(linear_search, array, key))
    binary_search_times.append(measure_search_time(binary_search, array, key))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(1, 6), linear_search_times, label='Linear Search')
plt.plot(range(1, 6), binary_search_times, label='Binary Search')
plt.xlabel('Search')
plt.ylabel('Time (seconds)')
plt.title('Time Taken for Linear and Binary Search')
plt.xticks(range(1, 6))
plt.legend()
plt.grid(True)
plt.show()

#Q3
def string_to_integer(s):
    s = s.replace(',', '')
    if len(s) == 0:
        return 0
    return string_to_integer(s[:-1]) * 10 + int(s[-1])

print(string_to_integer("13,531"))

#Q4
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("pots&pans"))

#Q5
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("racecar"))
print(is_palindrome("gohangasalamiimalasagnahog"))
