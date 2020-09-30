# Python3 program to rotate a matrix by 90 degrees 
N = 4

# An Inplace function to rotate 
# N x N matrix by 90 degrees in 
# anti-clockwise direction 
def rotateMatrix(mat): 
	
	# Consider all squares one by one 
	for x in range(0, int(N / 2)):
# Function to print the matrix 
def displayMatrix( mat ): 
	
	for i in range(0, N): 
		
		for j in range(0, N): 
			
			print (mat[i][j], end = ' ') 
		print ("") 
	
	


# Driver Code 
mat = [[0 for x in range(N)] for y in range(N)] 

# Test case 1 
mat = [ [1, 2, 3, 4 ], 
		[5, 6, 7, 8 ], 
		[9, 10, 11, 12 ], 
		[13, 14, 15, 16 ] ] 
		
''' 
# Test case 2 
mat = [ [1, 2, 3 ], 
		[4, 5, 6 ], 
		[7, 8, 9 ] ] 

# Test case 3 
mat = [ [1, 2 ], 
		[4, 5 ] ] 
		
'''

rotateMatrix(mat) 


displayMatrix(mat) 

