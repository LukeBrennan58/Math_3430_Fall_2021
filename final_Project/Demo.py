import LA
import QR
import LS
global m1, m2, m3, m4, m5, s1, s2, s3, s4, v1, v2, v3, v4, v5, v6, v7

m1 = [[12,7,3],[4,5,6],[7,8,9]]
m2 = [[5,8,1],[6,7,3],[4,5,9]]
m3 = [[8,6,7],[5,3,0],[9,9,9]]
m4 = [[1,2,3],[-1,1,2],[1,-2,0]]
m5 = [[1,-1,1],[1,0,1],[1,1,2]]
m6 = [[1,2,3],[1,1,2],[2,1,2]]
m7 = [[3,2,1],[-1,1,-2],[1,-2,5]]
s1 = 3
s2 = 7
s3 = -9
s4 = 3-4j
v1 = [1,2,4]
v2 = [8,7,9]
v3 = [9,1,1]
v4 = [7+24j,4,7]
v5 = [5,5-12j,8+15j]
v6 = [3,3,1]
v7 = [3,-1,4]



def main():
    c = 1
    print("\n","Hello I am Luke and this is the interface for my Linear Algebra library")
    while(c != 0):
        print("\n\t","Please select an option from the following menu (0 to exit)",
              "\n\t\t","1.  Vector addition",
              "\n\t\t","2.  Scalar-Vector multiplication",
              "\n\t\t","3.  Scalar-Matrix multiplication",
              "\n\t\t","4.  Matrix addition",
              "\n\t\t","5.  Matrix-Vector multiplication",
              "\n\t\t","6.  Matrix-Matrix multiplication",
              "\n\t\t","7.  Vector P-norm",
              "\n\t\t","8.  Vector Infinity norm",
              "\n\t\t","9.  Vector P-norm/Infinity norm",
              "\n\t\t","10. Vector Inner Product",
              "\n\t\t","11. Matrix QR factorization (Gramm Schmidt)",
              "\n\t\t","12. Orthonormal list of vectors with same span",
              "\n\t\t","13. Matrix QR factorization (Householder)",
              "\n\t\t","14. Matrix-Vector Least Squares Solution")
        try:
            c = int(input())
                
            if c == 1:
                print("\n\n","Vadd() is the function for vector addition",
                      "\n", "This function preforms vector addition on two lists as if they were vectors",
                      "\n\t", "Example:",v1,"+",v2,"=", LA.Vadd(v1,v2))
                c = int(input())
                
            elif c == 2:
                print("\n\n","SxV() is the function for scalar-vector multiplication",
                      "\n", "This function multiplies one float to a list as if it was a vector",
                      "\n\t", "Example:",s1,"x",v1,"=", LA.SxV(s1,v1))
                c = int(input())
                 
            elif c == 3:
                print("\n\n","SxM() is the function for scalar-matrix multiplication",
                      "\n", "This function multiplies one float to a list of lists as if it was a matrix",
                      "\n\t", "Example:",s1,"x",m1,"=", LA.SxM(s1,m1))
                c = int(input())
                
            elif c == 4:
                print("\n\n","Madd() is the function for matrix addition",
                      "\n", "This function adds to sets of lists of lists together as if they were matrices",
                      "\n\t", "Example:",m2,"+",m1,"=", LA.Madd(m2,m1))
                c = int(input())
                
            elif c == 5:
                print("\n\n","MxV() is the function for matrix-vector multiplication",
                      "\n", "This function multiplies a list of lists to a list as if they were a matrix and a vector",
                      "\n\t", "Example:",m1,"x",v1,"=", LA.MxV(m1,v1))
                c = int(input())
                
            elif c == 6:
                print("\n\n","MxM() is the function for matrix-matrix multiplication",
                      "\n", "This function multiplies together two sets of lists of lists as if they were matrices",
                      "\n\t", "Example:",m2,"x",m1,"=", LA.MxM(m2,m1))
                c = int(input())
                
            elif c == 7:
                print("\n\n","Pnorm() is the function for the vector p-norm",
                      "\n", "This function treats a list like a vector and calculates the p-norm",
                      "\n\t", "Example: The p-norm of",v4, "is", LA.Pnorm(v4))
                c = int(input())
                
            elif c == 8:
                print("\n\n","Inorm() is the function for the vector infinity-norm",
                      "\n", "This function treats a list like a vector and calculates the infinity-norm",
                      "\n\t", "Example: The infinity norm of",v4, "is", LA.Inorm(v4))
                c = int(input())
                
            elif c == 9:
                print("\n\n","PorI() is the function that calculates the p-norm or infinity-norm of a vector",
                      "\n", "This function treats a list like a vector and calculates the infinity-norm or the p-norm",
                      "\n\t", "Example: The p-norm of",v4, "is", LA.PorI(v4))
                c = int(input())
               
            elif c == 10:
                print("\n\n","Dot() is the function for the inner product of two vectors",
                      "\n", "This function treats the lists like vectors and calculates the inner product",
                      "\n\t", "Example: <",v1,",",v2,"> =", LA.Dot(v1,v2))
                c = int(input())
                
            elif c == 11:
                qr = QR.SGS(m4)
                Q = qr[0]
                R = qr[1]
                print("\n\n","SGS() is the function for QR factorization of a matrix using the gramm schmidt method",
                      "\n", "This function treats the list of lists like a matrix and finds an orthonomal set of vectors Q and another set of vectors R so that Q x R = the input matrix",
                      "\n\t", "Example: Q x R = A",
                      "\n\t", "A =",m4,
                      "\n\t", "Q =",Q,
                      "\n\t", "R =",R)
                c = int(input())
            
            elif c == 12:

                print("\n\n","Q() is the function for finding an orthonormal set of vectors that share the same span",
                      "\n", "This function calls SGS() and returns the Q from the result",
                      "\n\t", "Example: An orthonormal set of vectors that share the same span as", m4, "is", QR.Q(m4))

                c = int(input())
                
            elif c == 14:
                print("\n\n","LS() is the function that finds the least squares solution to the problem Ax = b",
                      "\n", "This function treats the list like a vector and the list of lists like a matrix and finds the least squares solution",
                      "\n\t", "Example: Ax = b",
                      "\n\t", "A =",m6,
                      "\n\t", "b =",v6,
                      "\n\t", "x =",LS.LS(m6,v6))
                c = int(input())
            else:
                print("\nIncorrect input")
                
        except ValueError:
            print("")
        
        
    
main()