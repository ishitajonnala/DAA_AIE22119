#Q1
def find_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return complement, num
        seen.add(num)
    return None

arr = [8, 7, 2, 5, 3, 1]
target_sum = 10
print('Pair with the given sum:', find_pair_with_sum(arr, target_sum))

#Q2
def max_product_pair(arr):
    if len(arr) < 2:
        return None
    max_num = max(arr)
    arr.remove(max_num)
    second_max = max(arr)
    return max_num, second_max

arr = [1, 7, 4, 2, 8, 6, 3, 9, 5]
print('Pair with maximum product: ', max_product_pair(arr))

#Q3
def sort_array(arr):
    first_wrong = None
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            if first_wrong is None:
                first_wrong = i
            else:
                second_wrong = i + 1
                break
        i += 1

    arr[first_wrong], arr[second_wrong] = arr[second_wrong], arr[first_wrong]

    return arr

input1 = [3, 8, 6, 7, 5, 9]
input2 = [3, 5, 6, 9, 8, 7]

output1 = sort_array(input1)
output2 = sort_array(input2)

print("Sorted array 1:", output1)
print("Sorted array 2:", output2)

#Q4
def segregate_zeros_ones(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = [0, 1, 0, 1, 1, 0, 0, 1]
print('Segeregatd Array: ' , segregate_zeros_ones(arr))

#Q5
def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inversion_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inversion_count += mid - i + 1
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return inversion_count

def merge_sort(arr, temp, left, right):
    inversion_count = 0
    if left < right:
        mid = (left + right) // 2
        inversion_count += merge_sort(arr, temp, left, mid)
        inversion_count += merge_sort(arr, temp, mid + 1, right)
        inversion_count += merge(arr, temp, left, mid, right)
    return inversion_count

def inversion_count(arr):
    temp = arr.copy()
    return merge_sort(arr, temp, 0, len(arr) - 1)

arr = [10, 1, 2, 4, 13, 9, 5]
print("Inversion count:", inversion_count(arr))

#Q6
# a. 𝑂(𝑛^2) Algorithm
def has_sum_quadratic(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

arr = [8, 4, 1, 6]
target = 10
print(' 𝑂(𝑛^2) ', has_sum_quadratic(arr, target))
# b. 𝑂(𝑛𝑙𝑜𝑔𝑛) Algorithm
def has_sum_linear_logn(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return False

arr = [8, 4, 1, 6]
target = 10
print('𝑂(𝑛𝑙𝑜𝑔𝑛)', has_sum_linear_logn(arr, target))

