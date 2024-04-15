#Candies
def candies(n, arr):
    candies_arr = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies_arr[i] = candies_arr[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies_arr[i] = max(candies_arr[i], candies_arr[i + 1] + 1)

    return sum(candies_arr)

n1 = 3
arr1 = [1, 2, 2]
print('No of candies Required:', candies(n1, arr1))  

n2 = 10
arr2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
print('No of candies Required:', candies(n2, arr2))  

n3 = 8
arr3 = [2, 4, 3, 5, 2, 6, 4, 5]
print('No of candies Required:', candies(n3, arr3))  

#Cloud Day
def maximumPeople(n, populations, town_locations, m, cloud_locations, cloud_ranges):
    town_populations = dict(zip(town_locations, populations))

    clouds = sorted(zip(cloud_locations, cloud_ranges))

    max_sunny_population = 0

    for i in range(m):
        sunny_population = 0
        for location, population in town_populations.items():
            if any(abs(location - cloud[0]) <= cloud[1] for cloud in clouds if cloud != clouds[i]):
                continue 
            sunny_population += population

        max_sunny_population = max(max_sunny_population, sunny_population)

    return max_sunny_population

n = 2
populations = [10, 100]
town_locations = [5, 100]
m = 1
cloud_locations = [4]
cloud_ranges = [1]

print('Maximum People:', maximumPeople(n, populations, town_locations, m, cloud_locations, cloud_ranges))  

# Goodland Electricty
def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0

    while i < n:
        found_plant = False
        for j in range(min(i + k - 1, n - 1), i - k, -1):
            if arr[j] == 1:
                plants += 1
                found_plant = True
                i = j + k
                break

        if not found_plant:
            return -1

    return plants

n, k = 6, 2
arr = [0, 1, 1, 1, 1, 0]

print('Plants:', pylons(k, arr))  