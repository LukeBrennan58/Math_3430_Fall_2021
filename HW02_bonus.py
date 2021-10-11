#Luke Brennan
#9/26/21

"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.

1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""

#Problem 00
'''
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
'''
def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#Problem 01
'''
Q1: What do we have?
    A Scalar stored as a float or an int and a vector stored as a list. Denoted as S and V.
Q2: What do we want?
    We want the product of the scalar and vector multiplication stored as a list
Q3: How will we get there?
    I will Iterate through the vector and multiply the scalar to each element

    I will set an empty list denoted as ‘result’
    Then I will iterate through the vector (V)
        While iterating I will append the current index of V times the scalar to the result
    I will then return the result as a list
'''
def Svector_mult(S, V):

    #first we check if the types are correct
    if not ((type(S) == float) or (type(S) == int)) and (type(V) == list):
        return 'error: input types are incorrect'
    
    result = [] #establishes an empty list to fill later
    
    for i in V:                 #iterates through and appends the new value to the blank list
        result.append(S * i)
        
    return result

#Problem 02
'''
Q1: What do we have?
    A scalar stored as a float or an int and a matrix stored as a list of lists where each sub list can represent either a column or a row it won’t matter for scalar multiplication. The scalar denoted as S and the matrix (list of lists) denoted as M.
Q2: What do we want?
    We want the product of the scalar and matrix multiplication stored as a list of lists where the sub lists represent whatever the user was representing them as
Q3: How will we get there?
    I will iterate through the matrix one row/column at a time and multiply the scalar to every element and piece each row/column back together in a result matrix

    I will set an empty list denoted as ‘result’
    I will iterate the length of M which will be the number of rows or columns whatever the user assumes when entering the matrix
        I will set a list variable (temp) to an empty list
        For each Row/Column I will iterate to each element
            I will append the scalar times the element to the list variable (temp)
        After completing one full row/column I will append it to the empty list (result)
    After the complete double iteration I will return the final result

'''
def Smatrix_mult(S, M):
    if not ((type(S) == float) or (type(S) == int)) and (type(M) == list):
        return 'error: input types are incorrect'
    result = [] #establishes an empty list to fill later
    
    for i in range(len(M)):     #iterates through the matrix
        temp = []               #for each row make a new blank list to fill
        for j in M[i]:          #now just use scalar vector multiplication method to solve each row
            temp.append(S*j)
        result.append(list(temp))
        
    return result

#Problem 03
'''
Q1: What do we have?
    Two matrices stored as lists of lists. They can be either a combination of rows or vectors
Q2: What do we want?
    A single matrix stored as a list of lists, where the list is the matrix addiction solution to  the two inputted matrices. Whether it is a combination of rows or columns depends on what the user assumed when inputting them
Q3: How will we get there?
    We will determine the size of the matrix and then iterate through every element and at each element to the same index in both matrices and store the result in a new matrix

    Check the size of the matrix and with two for loops create a matrix (list of lists) that is full  of 0s where the dimensions are that of the input matrix
    for each element in the size of one Row
        for each element in the size of one Column
            set the result index to the same index in the first matrix plus the same index in the second matrix

    return the result matrix
'''
def matrix_add(m1, m2):
    if not (type(m1) == list) and (type(m2) == list) and (type(m1[0]) == list) and (type(m2[0]) == list):
        return 'error: input types are incorrect'
    if not (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
        return 'error: matrices are not the same dimensions'
        
    R = len(m1)         #set R equal to the number of rows
    C = len(m1[0])      #set C equal to the number of columns
    
    temp = []           #temp variable to equal each row during the iteration
    result = []         #a blank list for appending each row to after solving
    
    for column in range(C):     #for each column append a 0 to the temp variable
        temp.append(0)          #this is so temp matches the width of the matrix
        
    for row in range(R):        #for each row in the matrix append the list of the proper length
        result.append(list(temp))
        #must have list() here or else all the rows must always be identical
        
        #the last block of code creates a matrix of the proper dimensions filled with 0s
        
    for i in range(R):
        for j in range(C):          #iterates through each position in the matrix one row at a time
            try:
                result[i][j] = m1[i][j] + m2[i][j]
            except IndexError:
                return 'error: matrix dimensions are incorrect'
            #Whatever position we are at this last line will add the number in that position of both matrices together
    
    return(result)

#Problem 04
'''
Q1: What do we have?
		A matrix stored as a list of lists where each sub list is a column (M)
		A Vector stored as a list of numbers (V)
Q2: What do we want?
		A Vector that is the result of matrix vector multiplication of the two inputs
Q3: How will we get there?
		We will use the linear combination of columns method to multiply each value in the vector to each column of the matrix and then add all of the resulting vectors together


Function name = Mvector_mult
	
		Set a result variable to a list the length of teh vector but filled with 0s
		
		for each element in the vector
			set a temp variable to the result of scalarvector multiplication of the current index of the vector and the matrix. The index of the vector will be a scalar and the current index of the matrix will be a column vector (list)
			
			for each element in the temp variable
				set the result list the itself plus the current index of the temp variable
		
		return the result variable
'''
def Mvector_mult(M, V):
    if not (type(M) == list and type(M[0]) == list and type(V) == list and (type(V[0]) == int or type(V[0]) == float)):
        return 'error: input types are incorrect'
    if not (len(M[0]) == len(V)):
        return 'error: input dimensions are incorrect'
        
    result = []
    
    for i in V:
        result.append(0)            #We create an empty vector that is the same length as the input vector
        
    for j in range(len(V)):
        temp = Svector_mult(V[j], M[j])     #for each value in V we will multiply that to the corrosponding row in the matrix using Problem 1
        
        for k in range(len(temp)):          #Now we construct the result matrix with the data we gathered from the first iteration
            result[k] += temp[k]
            
    return result

#Problem 05
'''
Q1: What do we have?
		Two matrices stored as lists of lists where each sub list represents a column of the matrix (m1,m2)
Q2: What do we want?
		The result of matrix multiplication of the two matrices stored as lists of lists where each sub list represents a column
Q3: How will we get there?
		We will iterate through the second matrix and mutiply the the first matrix to each column in the second. We will then append each resulting column to form the result matrix
		

Function name = Colmatrix_mult	
	
		for each element in the second matrix
			multiply the first matrix to the current column of the second matrix using matrix vector multiplication algorithm
			
			Put all the resulting column vectors into a single matrix
		
		return the resulting matrix
'''
def Colmatrix_mult(m1, m2):
    
    result = []
    for i in m2:
        result.append(Mvector_mult(m1, i))
        
    return result

#Test Inputs
def main():
    import numpy as np
    
    m1 = [[12,7,3],[4,5,6],[7,8,9]]
    m2 = [[5,8,1],[6,7,3],[4,5,9]]
    m3 = [[8,6,7],[5,3,0],[9,9,9]]
    s1 = 3
    s2 = 7
    v1 = [1,2,4]
    v2 = [8,7,9]
    v3 = [9,1,1]

    '''
    For Printing I will print my output using my function
    To check my function I will use numpy's matrix function and input the same variables
    Because numpy uses row matricies I have to use a few tranposition functions to change them into column matricies
    Also numpy uses a different value type that I convert to a list with the .tolist method so it matches what my outputs look like
    '''
    print("\nProblem #0")
    print("Test 1 = ",add_vectors(v1,v2))
    print("Should be = ",np.matrix.tolist(np.add(v1,v2)))
    print("\nTest 2 = ",add_vectors(v2,v3))
    print("Should be = ",np.matrix.tolist(np.add(v2,v3)))
    
    print("\n\nProblem #1")
    print("Test 1 = ",Svector_mult(s1, v1))
    print("Should be = ",np.matrix.tolist(np.multiply(s1,v1)))
    print("\nTest 2 = ",Svector_mult(s2, v2))
    print("Should be = ",np.matrix.tolist(np.multiply(s2,v2)))
    
    print("\n\nProblem #2")
    print("Test 1 = ",Smatrix_mult(s1, m1))
    print("Should be = ",np.matrix.tolist(np.multiply(s1,m1)))
    print("\nTest 2 = ",Smatrix_mult(s2, m2))
    print("Should be = ",np.matrix.tolist(np.multiply(s2,m2)))

    print("\n\nProblem #3")
    print("Test 1 = ",matrix_add(m1, m2))
    print("Should be = ",np.matrix.tolist(np.add(m1,m2)))
    print("\nTest 2 = ",matrix_add(m2, m3))
    print("Should be = ",np.matrix.tolist(np.add(m2,m3)))
    
    print("\n\nProblem #4")
    print("Test 1 = ",Mvector_mult(m3, v1))
    print("Should be = ",np.matrix.tolist(np.dot(np.transpose(m3),np.transpose(v1))))
    print("\nTest 2 = ",Mvector_mult(m1, v2))
    print("Should be = ",np.matrix.tolist(np.dot(np.transpose(m1),np.transpose(v2))))
    
    print("\n\nProblem #5")
    print("Test 1 = ",Colmatrix_mult(m1, m2))
    print("Should be = ",np.matrix.tolist(np.transpose(np.dot(np.transpose(m1),np.transpose(m2)))))
    print("\nTest 2 = ",Colmatrix_mult(m2, m3))
    print("Should be = ",np.matrix.tolist(np.transpose(np.dot(np.transpose(m2),np.transpose(m3)))))

    #Scrapped Printing method
    '''print("\nProblem #1")
    print("\n",s1,"*",v1,"=", Svector_mult(s1, v1))
    print("\n",s2,"*",v2,"=", Svector_mult(s2, v2))

    print("\n\nProblem #2")
    print("\n",s1,"*",m1,"=", Smatrix_mult(s1, m1))
    print("\n",s2,"*",m2,"=", Smatrix_mult(s2, m2))
    
    print("\n\nProblem #3")
    print("\n",m2,"+",m1,"=", matrix_add(m2, m1))
    print("\n",m3,"+",m2,"=", matrix_add(m3, m2))
    
    print("\n\nProblem #4")
    print("\n",m3,"*",v1,"=", Mvector_mult(m3, v1))
    print("\n",m1,"*",v2,"=", Mvector_mult(m1, v2))
    
    print("\n\nProblem #5")
    print("\n",m1,"*",m2,"=", Colmatrix_mult(m1, m2))
    print("\n",m2,"*",m3,"=", Colmatrix_mult(m2, m3))'''
    
    

main()
