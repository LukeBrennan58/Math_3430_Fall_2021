import pytest
import LA
import QR
import LS

global m1, m2, m3, v1, v2, Error

m1 = [[1,2,3],[1,1,2],[2,1,2]]
m2 = [[3,2,1],[-1,1,-2],[1,-2,5]]


v1 = [3,3,1]
v2 = [3,-1,4]

Error = 1/(10*(10**12))

def test_LS():
    
    #[5,-12,5]
    assert LA.Pnorm(QR.Vsub(LS.LS(m1,v1), [5,-12,5])) < Error
    
    #[0.4,-1.8,0]
    assert LA.Pnorm(QR.Vsub(LS.LS(m2,v2), [0.4,-1.8,0])) < Error
    
pytest.main()