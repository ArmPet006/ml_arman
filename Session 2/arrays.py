import numpy as np

arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr1d)
print(arr2d)

arr = np.array([1,2,3,4,5])
print(arr[2])
print(arr[1:4])


x = [1,2,3]
y = [4,5,6]
print(x+y)
sum1 = np.array([1,2,3])
sum2 = np.array([4,5,7])
print(sum1 + sum2)
print(sum1 * sum2)

resizeArr = np.array([1,2,3,4,5,6])
print(resizeArr.reshape((2,3)))

statArr = np.array([1,2,3,4,5,6])

mean = np.mean(statArr)
max_val = np.max(statArr)
total = np.sum(statArr)
print(f'Mean: {mean}, Max: {max_val}, Sum: {total}')

