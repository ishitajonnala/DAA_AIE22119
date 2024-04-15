#Q1
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    total_benefit = 0
    included_items = []  
    for value, weight in items:
        if weight <= capacity:
            included_items.append((value, weight))  
            total_benefit += value
            capacity -= weight
        else:
            fraction = capacity / weight
            included_items.append((value, weight*fraction))  
            total_benefit += value * fraction
            break  
        
    print("Optimal Solution:")
    for item in included_items:
        print("Value:", item[0], ", Weight:", item[1])

    return total_benefit

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print("Maximum total benefit:", fractional_knapsack(items, capacity))

#Q2
def maximize_sum(arr):
    arr.sort()
    total_sum = sum(arr[i]*i for i in range(len(arr)))
    return total_sum

arr = [2, 5, 3, 4, 0]
print("Maximum sum:", maximize_sum(arr))


#Q3
def min_sum_of_product(array_one, array_two):
    array_one.sort()
    array_two.sort(reverse=True)

    min_sum = sum(a*b for a, b in zip(array_one, array_two))
    return min_sum

array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
print("Minimum sum of product:", min_sum_of_product(array_one, array_two))
