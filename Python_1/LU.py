#!usr/bin/env/python 3
#https://en.wikipedia.org/wiki/LU_decomposition#Algorithms
'''
FOR TESTING  -- 
mat = [[2, -1, -2], 
       [-4, 6, 3], 
       [-4, -2, 8]]; 

'''
import numpy.linalg as lin #used just for inverse computation and matrix multiplication
import numpy as np
n=int(input('Enter the no. of rows of matrix'))
p=int(input('Enter the no. of columns of matrix'))
matrix=[[0]*p for i in range(0,n)]
#print(matrix)
m=matrix
for i in range(0,n):
	for j in range(0,p):
		m[i][j]=int(input('Enter element {0}{1}  '.format(i+1,j+1)))
for i in range(0,n):
	for j in range(0,p):
		print(float(m[i][j]),end="\t\t\t")
	print()
print()
a = m.copy()
x = []
for i in range(0,n):
	for j in range(i+1,n):
		while(m[i][i]==0&i<n):
			for l in range(0,p):
				m[i][l],m[j][l]=m[j][l],m[i][l]
			i+=1
		temp = float(m[j][i]/m[i][i])
		x.append(temp)
		for k in range(i,p):
			m[j][k]=m[j][k]-temp*m[i][k]	
print("\t\t\tTHE Upper MATRIX")		
for i in range(0,n):
	for j in range(0,p):
		print(float(m[i][j]),end="\t\t\t")
	print()

l = list(np.matmul(np.array(a),lin.inv(np.array(m))))

for i in range(n):
	for j in range(i,p):
		if i == j:
			pass
		else:
			l[j][i] = x.pop(0)

print("\t\t\tTHE Lower MATRIX")	
for i in range(0,n):
	for j in range(0,p):
		print(float(l[i][j]),end="\t\t\t")
	print()
	

