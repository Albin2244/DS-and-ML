import numpy as np
n=np.random.randint(10,size=(2,2))
print(n)

print("determinant")
print(np.linalg.det(n))

print("inverse")
print(np.linalg.inv(n))

print("matrix Rank")
print(np.linalg.matrix_rank(n))

print("Transpose as 1-dimensional array:")
print(n.T.flatten())



           output
  ==========================

[[6 3]
 [8 5]]
determinant
6.0
inverse
[[ 0.83333333 -0.5       ]
 [-1.33333333  1.        ]]
matrix Rank
2
Transpose as 1-dimensional array:
[6 8 3 5]

Process finished with exit code 0
