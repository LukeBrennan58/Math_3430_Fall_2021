
#Problem 00
def Vadd(v1:list,v2:list):
    '''Adds two vectors together
    

    Parameters
    ----------
    v1 : A vector list of floats. First term in vector addition
    v2 : A vector list of floats. Second term in vector addition

    Returns
    -------
    result : A vector list of floats that is the resultant of the two vectors

    '''
    result:list = []
    for i in v1:
        result.append(0)
          
    for j in range(len(result)):
        result[j] = v1[j] + v2[j]
      
    return result

#Problem 01
def SxV(S:float, V:list):
    
    '''Multiplies a Scalar to a vector.
    
    Create an empty list called result
    iterate through the input vector V and append the product of the current index and the scalar to result

    Parameters
    ----------
    S : A float scalar to be the first factor
    V : A vector list of floats to be the second factor

    Returns
    -------
    result : A new vector list of floats that represents the product of the input scalar S and vector V

    '''
    
    #first we check if the types are correct
    
    
    result:list = [] #establishes an empty list to fill later
    
    for i in V:                 #iterates through and appends the new value to the blank list
        result.append(S * i)
        
    return result

#Problem 02
def SxM(S:float, M:list):
    
    '''Multiplies a Scalar to a matrix.
    
    Create an empty list called result
    iterate through the matrix assigning each column vector to i
    call SxV to multiply the scalar to each column vector
    append the new column vector to the result list

    Parameters
    ----------
    S : A float scalar to be the first factor
    M : A Matrix list of lists of floats represented as a list of column vectors to be the second factor

    Returns
    -------
    result : A new matrix list of lists of floats to be the product of the input scalar S and the matrix M

    '''
    
    
    
    result:list = [] #establishes an empty list to fill later
    
    for i in M:
        result.append(SxV(S, i))

    return result

#Problem 03
def Madd(m1:list, m2:list):
    '''Performs matrix addition between two input matrices
    
    Create an empty list called result
    iterate through the columns of the first matrix
    compute matrix addition between the corresponding column in both matrices and append it to the result

    Parameters
    ----------
    m1 : A matrix list of lists of floats represted by a list of columns. The first term in the matrix addition
    m2 : A matrix list of lists of floats represted by a list of columns. The second term in the matrix addition

    Returns
    -------
    result : A new matrix list of lists of floats to be the result of matrix addition between the matrices m1 and m2

    '''

    result:list = []         #a blank list to store result
        
    for i in range(len(m1)):                     #iterate for each column in the matrix
        result.append(Vadd(m1[i],m2[i]))    #append the matrix addition of the matching columns in the two matrices
        
    return(result)

#Problem 04
def MxV(M:list, V:list):
    '''Computes the Matrix dot product of the input vector and matrix
    
    Create an empty list called result
    fill the result with 0s equal to the length of the input vector
    iterate through the input vector and use SxV to compute the scalar vector multiplication of the current element of the vector to the corrosponding column in the matrix
    use Vadd to add the found vector to the result and reassign the result to the result vector
    
    Parameters
    ----------
    V : A vector list of floats to be the first term in the matrix multiplication
    M : A matrix list of lists of floats represted by a list of columns to be the second term in the matrix multiplication

    Returns
    -------
    result : A new vector list of floats that represents the matrix multiplication of the input vector and matrix

    '''
        
    result:list = []
    
    for i in V:
        result.append(0)            #We create an empty vector that is the same length as the input vector
        
    for j in range(len(V)):
        temp:list = SxV(V[j], M[j])     #for each value in V we will multiply that to the corrosponding row in the matrix using Problem 1
        result = Vadd(result, temp)         #We will add the found vector to the result and reassign it to result
            
    return result

#Problem 05
def MxM(m1:list, m2:list):
    
    '''Computes the Matrix dot product of the two input matrices
    
    Create an empty list called result
    iterate through the second input matrix and use VxM to multiply the corresponding column to the first input matrix 
    append the result of VxM to result
    
    
    Parameters
    ----------
    m1 : A matrix list of lists of floats represted by a list of columns. The first term in the matrix multiplication
    m2 : A matrix list of lists of floats represted by a list of columns. The second term in the matrix multiplication

    Returns
    -------
    result : A new matric list of lists of floats represented by a list of columns that is the result of the matrix multiplication of the two input matrices m1 and m2

    '''
    
    result:list = []
    for i in m2:
        result.append(MxV(m1, i))
        
    return result
    