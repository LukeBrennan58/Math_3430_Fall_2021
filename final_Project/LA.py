'''
Luke Brennan
'''

#0
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

#1
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

#2
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

#3
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

#4
def MxV(M:list, V:list):
    '''Computes the Matrix multiplication of the input vector and matrix
    
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

#5
def MxM(m1:list, m2:list):
    '''Computes the Matrix multiplication of the two input matrices
    
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

#Absolute Value 
def AbV(s:complex):
    
    '''Computes the absolute value of the input scalar
    
    Create a variable result
    Square the real and imaginary part of s and then take the square root
    *this will give you the distance from 0
    
    Parameters
    ----------
    s : A scalar represented as a float that may be real or imaginary

    Returns
    -------
    A positive float that represents the absolute value of the input scalar

    '''
            
    return((s.real**2 + s.imag**2)**0.5)

#6
def Pnorm(v:list, p:int=2):
    '''Computes the P-norm of the input vector
    
    Create a variable result
    Iterate through v raise each term to the power of p and add them all to result
    take the p root of the result
    
    Parameters
    ----------
    v : A vector list of scalars that may contain real or imaginary numbers
    p : A scalar represented as a float set default to 2

    Returns
    -------
    result : A positive float that represents the computed P-norm of the vector

    '''
    result:float = 0
    
    for i in v:
        result += AbV(i)**p
        
    return result**(1/p)

#7
def Inorm(v:list):
    
    '''Computes the Infinity norm of the input vector
    
    Create a variable result
    Iterate through the vector v and set the absolute value of the first term equal to the result
    Then check every subsequent term to see if the absolute value of the term is greater than the previously established result
    If a term is greater than set result equal to that term
    
    
    Parameters
    ----------
    v : A vector list of scalars that may contain real or imaginary numbers


    Returns
    -------
    result : A positive float that represents the computed Infinity norm of the vector

    '''
    
    result = 0
    term = 0
    
    for i in v:
        term = AbV(i)
        if term > result:
            result = term
        
    return result

#8
def PorI(v:list, p:int=2, c:bool=False):
    
    '''Computes either the P-norm or the Infinity norm of a vector based on what the user inputs as the third argument
    
    If c is True then call Inorm() to compute the infinity norm of the vector and return it
    Otherwise call Pnorm() to compute the P-norm of the vector and return that
    
    
    Parameters
    ----------
    v : A vector list of scalars that may contain real or imaginary numbers
    p : A scalar represented as a float set default to 2
    c : A boolean value set default to False

    Returns
    -------
    A positive float that either represents the computed Infinity norm or the P-norm of the input vector

    '''
    
    if c:
        return Inorm(v)
    else:
        return Pnorm(v, p)
    
#9
def Dot(v1:list, v2:list):

    
    '''Computes the inner product or dot product of two vectors
    
    Create an float result equal to 0
    iterate through a vector and if the current index of the first vector is a comlex number take the conjugate
    add the two corresponding indexes of the vectors to the result but use the conjugate if you took it in the last step
    
    
    Parameters
    ----------
    v1 : A vector list of scalars that may contain real or imaginary numbers
    v2 : A second vector list of scalars that may contain real or imaginary numbers

    Returns
    -------
    result : A float that represents the dot product of two vectors that may be imaginary or real

    '''
    
    result:float = 0
    
    for i in range(len(v1)):
        if type(v1[i]) == complex:
            result += v1[i].conjugate() * v2[i]
        else:
            result += v1[i] * v2[i]
    
    return result

#Matrix subtraction
def Msub(m1, m2):
    '''Subtracts two matrices
    
        Scalar matrix multiply the second matrix (m2) with -1
        Call matrix add function using the two matrix (m1, m2)
        
        Args:
            m1 : The first matrix (list lists of floats) in the matrix subtraction
            m2 : The second matrix(list lists of flaots) in the matrix subtraction that should be made negative
        
        Returns:
            The Difference between the two matrices (list lists of floats)
    '''
    
    m2 = SxM(-1, m2)
    return Madd(m1, m2)
    
#Vector subtraction
def Vsub(v1:list,v2:list):
    '''Subtracts two vectors
    
        Scalar Vector multiply the second vector (v2) with -1
        Call Vector add function using the two vectors (v1, v2)
        
        Args:
            v1 : The first vector (list of floats) in the vector subtraction
            v2 : The second vector (list of flaots) in the vector subtraction that should be made negative
        
        Returns:
            The Difference between the two vectors (list of floats)
    '''
    
    v2 = LA.SxV(-1,v2)
    return LA.Vadd(v1,v2)
