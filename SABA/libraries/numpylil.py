import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 0]])
arr3 = np.array([10, 20, 30, 40, 50])
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
random_arr = np.random.rand(3, 3)

print(arr1)
print(arr2)
print(zeros)
print(ones)
print(identity)
print(random_arr)

#array properties
print(arr2.shape)
print(arr2.size)
print(arr1.dtype)
print(arr2.ndim)

#indexing and slicing
print(arr2[0])#prints first row
print(arr2[1,2])#prints element in 1st rown 2 nd column
print(arr1[1:4])
a=np.array([[[1, 2, 3, 4, 5],[2,4,6,8,9]]])
print(a[0,1,2])#prints first inedx 2nd rows element

#reshaping & transposing
r=arr1.reshape(5,1)
t=arr2.T
print(r)
print(t)

# Mathematical Operations

sum_arr = arr1 + arr3
prod_arr = arr1 * arr3
div_arr = arr3 / arr1
sqrt_arr = np.sqrt(arr3)
power_arr = np.power(arr1, 3)
print("Sum:", sum_arr)
print("Product:", prod_arr)
print("Division:", div_arr)
print("Square Root:", sqrt_arr)
print("Power:", power_arr)