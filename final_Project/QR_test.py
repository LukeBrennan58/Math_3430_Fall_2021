import pytest
import LA
import QR

global m1, m2, m1A, m2A

m1 = [[1,2,3],[-1,1,2],[1,-2,0]]
m2 = [[1,-1,1],[1,0,1],[1,1,2]]

m1A = [[(14**.5)/14,(14**.5)/7, 3*(14**.5)/14],[-3*(10**.5)/10, 0, (10**.5)/10],[(35**.5)/35,-(35**.5)/7,3*(35**.5)/35]]
m2A = [[(3**.5)/3,-(3**.5)/3,(3**.5)/3],[(6**.5)/6,(6**.5)/3,(6**.5)/6],[-(2**.5)/2,0,(2**.5)/2]]

Error = 1/(10*(10**12))

#I could not figure out how to write the assert to check if matrices are very similiar so for now these tests all fail

def test_SGS():
    #Q =    14^.5/14        -3(10^.5)/10     35^.5/35
    #       14^.5/7         0               -35^.5/7
    #       3(14^.5)/14     10^.5/10        3(35^.5)/35
    
    assert QR.Msum(LA.Msub(QR.SGS(m1)[0],m1A)) < Error
    
    
    #Q =    3^.5/3          6^.5/6          -2^.5/2
    #       -3^.5/3         6^.5/3          0
    #       3^.5/3          6^.5/6          2^.5/2
    
    assert QR.Msum(LA.Msub(QR.SGS(m2)[0],m2A)) < Error
    
def test_Q():
    #Q =    14^.5/14        -3(10^.5)/10     35^.5/35
    #       14^.5/7         0               -35^.5/7
    #       3(14^.5)/14     10^.5/10        3(35^.5)/35
    
    assert QR.Msum(LA.Msub(QR.Q(m1),m1A)) < Error
    
    
    #Q =    3^.5/3          6^.5/6          -2^.5/2
    #       -3^.5/3         6^.5/3          0
    #       3^.5/3          6^.5/6          2^.5/2
    
    assert QR.Msum(LA.Msub(QR.Q(m2),m2A)) < Error
    
pytest.main()
