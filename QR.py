import LA

#Extra functions
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

#11
def SGS(A:list):
    '''Calculates the Gramm Schmidt (Q) and a corresponding matrix (R)
        
        Create an 2 empty matrices full of zeros that have the same dimensions as A
        Create a temp variable and set it equal to A (v)
        Iterate through the input matrix (v) for each element in v:
            Set the current index on the diagnal of R to the P-norm of the current element v
            Set the current column of Q to the Scalar Vector Multiplication of 1/(current index of the diagnal on R) and the current index of v
            Iterate from the current index to the size of A for each index:
                Using the column of the second index and the row of the first set it equal to the inner product of the first current index of Q and the second current index of v
                Change the current second index of the temp variable representing A (v) to the difference of that same index of v and the Scalar vector multiplication of the same index of R just changed and the first current index column of Q
        After completing the iteration return a list where the first element is Q and the second is R
        
        Args:
            A : A matrix (list of lists of floats) where each sub list represents a column 
        
        Returns:
            [Q,R] : A list of the two values Q and R
            Q : An orthonormal set of vectors that have the same span as the input matrix A
            R : A corresponding matrix such that Q * R = A
        
        
    '''
    v:list = []
    R:list = []
    Q:list = []
    temp:list = []
    for k in range(len(A[0])):
        temp.append(0)
    for k in range(len(A)):
        R.append(list(temp))
        Q.append(list(temp))
        
    v = list(A)
    for i in range(len(v)):
        R[i][i] = LA.Pnorm(v[i])
        Q[i] = LA.SxV(1/R[i][i],v[i])
        
        for j in range(i,len(v)):
            R[j][i] = LA.Dot(Q[i],v[j])
            v[j] = Vsub(v[j],LA.SxV(R[j][i],Q[i]))
    
    return [Q, R]

#12
def Q(A:list):
    '''Returns an orthonormal list of vectors that shares the same span as the input matrices columns
    
        
        Args:
            A : A matrix (list of lists of floats) where each sub list represents a column 
            
        Returns:
            Q : An orthonormal set of vectors that share the same span as the input matrix's columns
    '''
    return SGS(A)[0]
    
    
'''Gramm Schmidt Alternate Method

def proj(u:list, v:list):
    return LA.SxV(LA.Dot(v,u)/(LA.Pnorm(u)**2),u)

def e(u:list):
    return LA.SxV(1/(LA.Pnorm(u)),u)

def GS(v:list):
    
    u:list = []
    for k in range(len(v)):
        u.append(0)
    
    for i in range(len(v)):
        
        c:int = int(i)
        u[i] = v[i]

        uc:int = 0
        while c > 0:
            u[i] = Vsub(u[i],proj(u[uc],v[i]))
            c = c-1
            uc = uc + 1
        
        u[i] = e(u[i])
    return u'''

'''Unstable Gramm Schmidt


def USGS(A:list):
    v:list = []
    R:list = []
    Q:list = []
    temp:list = []
    for k in range(len(A[0])):
        temp.append(0)
    for k in range(len(A)):
        R.append(list(temp))
        Q.append(list(temp))
        
    v = list(A) 
    for i in range(len(v)):
        
        for j in range(i):
            R[i][j] = LA.Dot(Q[j],v[i])
            v[i] = Vsub(v[i],LA.SxV(R[i][j],Q[j]))
            
        R[i][i] = LA.Pnorm(v[i])
        Q[i] = LA.SxV(1/R[i][i],v[i])
    return [Q,R]'''

            
            
            
            
            
            
            