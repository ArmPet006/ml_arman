import numpy as np

random_array = np.random.randint(0, 100, size = 10)
print("The array: ", random_array)

mean = np.mean(random_array)
print("Mean: ", mean)

max_val = np.max(random_array)
print("Max: ", max_val)

min_val = np.min(random_array)
print("Min: ", min_val)

array_sum = np.sum(random_array)
print("Sum: ", array_sum)

sorted_array = np.sort(random_array)
print("Sorted array: ", sorted_array)

shuffled_array = np.random.permutation(random_array)
print("Shuffled array: ", shuffled_array)

squared_array = np.square(random_array)
print("Squared array: ", squared_array)

sqrt_array = np.sqrt(random_array)
print("Square root array: ", sqrt_array)
