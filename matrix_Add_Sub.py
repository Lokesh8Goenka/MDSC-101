#add, subtract, mutiply

rows = int(input("Enter the no of rows of mat 1: \n"))
cols = int(input("Enter the no of columns of mat 1: \n"))

rows2 = int(input("Enter the no of rows of mat 2: \n"))
cols2 = int(input("Enter the no of columns of mat 2: \n"))

if rows2 != cols:
	print("Operatins can't be performed due to the variation in size.")
	exit()



mat1 = []
print("Enter the elements of the first matrix.\n")
for i in range(0, rows):
	list_i = []
	mat1.append(list_i)
	for j in range(0, cols):
		list_i.append(int(input("")))


mat2 = []
print("Enter the elements of the second matrix.\n")
for i in range(0, rows2):
	list_i = []
	mat2.append(list_i)
	for j in range(0, cols2):
		list_i.append(int(input("")))

print(mat1)
print("\n")
print(mat2)

#add mat3[0][0] = mat1[0][0] + mat2[0][0]
mat3 = []
print("Sum\n")
for i in range(0, rows):
	list_i = []
	mat3.append(list_i)
	for j in range(0, cols):
		list_i.append(mat1[i][j] + mat2[i][j])
		
print("Addition ", mat3)	

#Difference mat4[0][0] = mat1[0][0] - mat2[0][0]
mat4 = []
print("Difference")
for i in range(0, rows):
	list_i = []
	mat4.append(list_i)
	for j in range(0, cols):
		list_i.append(mat1[i][j] - mat2[i][j])
print("Difference ", mat4)

#Multiplication mat1 * mat2
mat5 = []
if rows2 == cols:	
	for i in range(0, rows):
		list_i = []
		for j in range(0,cols2):
			mat5.append(list_i)
			temp = 0
			for k in range(0, rows2):
				# print("mat1", mat1[i][k])
				# print("mat2", mat2[k][j])
				temp += mat1[i][k] * mat2[k][j] 
				# print("mat5", mat5[i][j])
			
			list_i.append(temp)
	print(mat5)	
else:
	print("Try again!, Can not do matrix multiplication.")