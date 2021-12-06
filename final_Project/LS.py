import LA
import QR

#matrix transpose
def T(m:list):
    '''Finds the conjugate transpose of the matrix
    
        iterate through m to make an empty list of lists with the same dimensions but full of 0s
        iterate through each element of the matrix starting with the column then each element in each column
        if the number is complex set mT to the conjugate 
        flip the indexes and then set mT equal to the new index in order to transpose the matrix
        
        Args:
            m : a matrix list of lists. There can be floats or complex numbers in the matrix
        
        Returns:
            mT : a matrix list of lists that is the conjugate transpose of the input matrix m
    '''
    mT:list = []
    temp:list = []
    
    for k in range(len(m[0])):
        temp.append(0)
    for k in range(len(m)):
        mT.append(list(temp))
        
    for i in range(len(m)):
        for j in range(len(m[i])):
            if type(m[j][i]) == complex():
                mT[i][j] = m[j][i].conjugate()
            else:
                mT[i][j] = m[j][i]
            
    return mT

#upper triangular matrix solver
def backsub(A:list, b:list):
    '''Solves an upper triangular matrix using the back substitution method
    
        iterate through b and create a vector the same length of b but full of 0s, call it result
        iterate through the range of b backwards
            set a temp variable (num) equal to the current index of b
            now iterate through each column in A
                subtract the current index of A ([j][i]) times the current j index of the result matrix
            divide num by the current diagnal position of A
            set current i index of result to num
        
        Args:
            A : an upper triangular matrix stored as a list of lists (0s below the diagnal)
            b : a vector represented by a list
        
        Returns:
            result : a vector that represents the solution to the matrix where A * result = b
    '''
    
    num:float = 0
    size:int = len(b)
    result:list = []
    
    for k in b:
        result.append(0)
    
    for i in range(len(b))[::-1]:
        num = b[i]
        
        for j in range(len(A)):
            num = num - (A[j][i] * result[j])
            
        num = num / A[i][i]
        result[i] = num
        
    return result

#15
def LS(A:list, b:list):
    '''Finds the conjugate transpose of the matrix
    
        Take the QR factorization of A using gramm schmidt function (SGS)
        Find the Transpose of Q by calling the transpose function (T)
        Multiply the transpose of Q and b using Matrix vector multiplication function (MxV)
        Solve Rx = (Q*)b using the backsub function and calling R and (Q*)b (backsub)
    
        Args:
            A : a matrix list of lists with the elements either complex or floats
            b : a vector represented by a list of either floats or complex numbers
        
        Returns:
            result : A vector that is the closest possible solution to Ax = b 
            
    '''
    QT:list = T(QR.SGS(A)[0])
    return backsub(QR.SGS(A)[1],LA.MxV(QT,b))
