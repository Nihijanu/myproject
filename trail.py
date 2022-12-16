# l1=[10,20]
# l1 =l1*2
# print(l1)
import numpy
import numpy as np

arr=numpy.array([12,3.6,7])
ar1=numpy.array([2,3,4])
ar=ar1*arr
arr=arr*5
#error because they are in  string
ar3=numpy.array([[2,3,4],[4,5,6]])
print(ar3)
print(numpy.ndim(ar3))
print(arr)
print(ar)
arra=numpy.arange(1,10).reshape(3,3)
print(arra)
l=list(range(1,10,3))
print(type(l))
print(l)
ar5=numpy.arange(start=10,stop=-2,step=-3)
print(ar5)
ar4=numpy.arange(10,dtype=numpy.int64)
print(ar4.dtype)
print(ar4.itemsize)
arr1=numpy.arange(1,10).reshape(3,3)
print(arr1)
print(arr1[1:,1:])
print(np.zeros((2,2)))
arr2=np.arange(1,10).reshape(3,3)
print(arr2)
print(np.linalg.det(arr2))
A=np.arange(1,10).reshape(3,3)
B=np.arange(1,10).reshape(3,3)
print(np.dot(A,B))
print(A)
print(A.T)
print(arr2.max(axis=1))