#Q1
import time
import random
import matplotlib.pyplot as plt

# Generate random numbers
numbers = [random.randint(1, 10000) for _ in range(1000)]

# Define sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Measure time taken for each sorting algorithm
bubble_start = time.time()
bubble_sorted = bubble_sort(numbers.copy())
bubble_time = time.time() - bubble_start

selection_start = time.time()
selection_sorted = selection_sort(numbers.copy())
selection_time = time.time() - selection_start

quick_start = time.time()
quick_sorted = quick_sort(numbers.copy())
quick_time = time.time() - quick_start

# Plotting the results
plt.bar(['Bubble Sort', 'Selection Sort', 'Quick Sort'], [bubble_time, selection_time, quick_time])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.show()

#Q2
import heapq

def merge_sorted_lists(lists):
    merged_list = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    while heap:
        val, list_idx, idx = heapq.heappop(heap)
        merged_list.append(val)
        if idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][idx + 1], list_idx, idx + 1))
    return merged_list

sorted_lists = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
print(merge_sorted_lists(sorted_lists))

#Q3
import heapq

def find_k_largest_elements(arr, k):
    return heapq.nlargest(k, arr)

arr = [3, 1, 6, 2, 8, 4, 5, 7]
k = 3
print(find_k_largest_elements(arr, k))

#Q4
def max_activities(activities):
    activities.sort(key=lambda x: x[1])
    max_activities_count = 1
    last_end_time = activities[0][1]
    selected_activities = [activities[0]]
    for activity in activities[1:]:
        if activity[0] >= last_end_time:
            max_activities_count += 1
            last_end_time = activity[1]
            selected_activities.append(activity)
    return max_activities_count, selected_activities

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
max_count, max_activities = max_activities(activities)
print("Maximum activities that can be performed by a single person:", max_count)
print("Selected activities:")
for activity in max_activities:
    print(activity)

#Q5
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(intervals[i][1], merged[-1][1]))
        else:
            merged.append(intervals[i])
    return merged

intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
print('Overlapping intervals:', merge_intervals(intervals))
