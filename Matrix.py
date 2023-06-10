matrix=[
   [1,2,3],
    [4,5,6],
    [7,8,9]
]
'''
#change the value of matrix :
matrix[0][2]=10 
print(matrix[0][2])'''
#print matrix elements using nested loops:
for row in matrix:
    for col in row:
        print(col)