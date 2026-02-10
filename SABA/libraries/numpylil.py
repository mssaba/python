import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 0]])
arr3 = np.array([10, 20, 30, 40, 50])
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
random_arr = np.random.rand(3, 3)

""" print(arr1)
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
print("Power:", power_arr) """

# from scipy import stats
# arr4= np.array([10, 20, 30, 40, 50, 20])
# mean_val = np.mean(arr4)
# median_val = np.median(arr4)
# mode_val = stats.mode(arr4)
# std_dev = np.std(arr4)
# var_val = np.var(arr4)
# min_val = np.min(arr4)
# max_val = np.max(arr4)
# print("Mean:", mean_val)
# print("Median:", median_val)
# print("Standard Deviation:", std_dev)
# print("Mode:", mode_val)
# print("Variance:", var_val)
# print("Min:", min_val)
# print("Max:", max_val)

#concatenation & stacking

# c=np.concatenate((arr1, arr3))
# s=np.vstack((arr1,arr3))
# print('concatenate=',c)
# print('stacked=',s)





# random_int = np.random.randint(1,3)
# print("random_float:",random_int)
# rand_ints = np.random.randint(1, 100, (3, 3))
# print("Random Integers:", rand_ints)
# normals = np.random.normal(0, 1, (3, 3))
# print("Normal Distribution:", normals)

# empty_array = np.empty((2, 3))
# print(empty_array)


#arrange 
array1=np.arange(10)
print('Array:',array1)

#full
a=np.full((2,3),5)
print(a)

#linespace
b=np.linspace(0,5, num=10)
print(b)

#flattening
c=np.array([[1,2,3],
    [4,5,6]])
print(c.flatten())

# # Transposing the array 
# transposed_arr = np.transpose(arr)

# print("Original Array:")
# print(arr)
# print("\nTransposed Array:")
# print(transposed_arr)

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print("x=",x)

# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr) '''

a1=[[1,2],
    [2,3]]
a2=[[3,4],
    [5,6]]

print(np.matmul(a1,a2))
print(np.dot(a1,a2))