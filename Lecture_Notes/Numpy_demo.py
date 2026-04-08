import numpy as npn     # numpy is implemented in C

arr1 = npn.array([1,2,3,4])
arr2 = npn.array([5,6,7,8])

arr3 = arr1+arr2
print(arr3)
print(type(arr3))   #ndarray : n dimensional array - this is 1-d array

arr_2d=npn.array([[1,2], [3,4], [5,6]])

print(arr_2d)   #this is a 2-d array. array within array
print(type(arr_2d))
print(arr_2d.ndim)

arr_3d=npn.array([
[[1,1,5], [2,2,5], [6,6,5]],
[[3,3,5], [4,4,5], [5,5,5]],
[[5,5,5], [6,6,5], [7,7,5]]
])

print(arr_3d) # this is 3d array aka array of 2d array. 4d array will be array of 3-d array and so on.

# shape i.e dimension of any 2d array or n-d array = rows , columns

print(arr_3d.shape)  # shape is (3 rows,3 columns,3 elements in each array)

print(arr_3d.ndim)  #ndim returns the number of dimensions

print(arr_3d.dtype) # returns the data type of the array - int32 in this case

#numpy uses homogeneos datatype. 

arr6 =npn.array([1,2,3])
arr7 = npn.array([3,4])

#arr8 = arr6 + arr7
#print(arr8) # if we have two 1-d arrays with dufferent lengths it will retun an error

arr9 = ([[1,2], [3,4], [4,5]])

print(arr9)