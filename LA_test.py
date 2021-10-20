import pytest
import LA

global m1
global m2
global m3
global s1
global s2
global s3
global s4
global v1
global v2
global v3
global v4
global v5
m1 = [[12,7,3],[4,5,6],[7,8,9]]
m2 = [[5,8,1],[6,7,3],[4,5,9]]
m3 = [[8,6,7],[5,3,0],[9,9,9]]
s1 = 3
s2 = 7
s3 = -9
s4 = 3-4j
v1 = [1,2,4]
v2 = [8,7,9]
v3 = [9,1,1]
v4 = [7+24j,4,7]
v5 = [5,5-12j,8+15j]


def test_Vadd():
    #[9,9,13]
    assert LA.Vadd(v1, v2) == [9,9,13]
    
    #[17,8,10]
    assert LA.Vadd(v2, v3) == [17,8,10]
    
def test_SxV():
    #[3,6,12]
    assert LA.SxV(s1, v1) == [3,6,12]
    
    #[56,49,63]
    assert LA.SxV(s2, v2) == [56,49,63]
    
def test_SxM():
    #[[36,21,9],[12,15,18],[21,24,27]]
    assert LA.SxM(s1, m1) == [[36,21,9],[12,15,18],[21,24,27]]
    
    #[[35,56,7],[42,49,21],[28,35,63]]
    assert LA.SxM(s2, m2) == [[35,56,7],[42,49,21],[28,35,63]]
    
def test_Madd():
    #[[17,15,4],[10,12,9],[11,13,18]]
    assert LA.Madd(m1, m2) == [[17,15,4],[10,12,9],[11,13,18]]
    
    #[[13,14,8],[11,10,3],[13,14,18]]
    assert LA.Madd(m3, m2) == [[13,14,8],[11,10,3],[13,14,18]]
    
def test_MxV():
    #[48,49,51]
    assert LA.MxV(m1, v1) == [48,49,51]
    
    #[118,158,110]
    assert LA.MxV(m2, v2) == [118,158,110]

def test_MxM():
    #[[99,83,72],[121,101,87],[131,125,123]]
    assert LA.MxM(m1, m2) == [[99,83,72],[121,101,87],[131,125,123]]
    
    #[[104,141,89],[43,61,14],[135,180,117]]
    assert LA.MxM(m2, m3) == [[104,141,89],[43,61,14],[135,180,117]]

def test_AbV():
    #9
    assert LA.AbV(s3) == 9
    
    #5
    assert LA.AbV(s4) == 5

def test_Pnorm():
    #25^2 + 4^2 + 7^2 = 690 --> 690^(1/2)
    assert LA.Pnorm(v4) == 690**(1/2)
    
    #5^3 + 13^3 + 17^3 = 7235 --> 7235^(1/3)
    assert LA.Pnorm(v5, 3) == 7235**(1/3)
    
def test_Inorm():
    #25
    assert LA.Inorm(v4) == 25
    
    #17
    assert LA.Inorm(v5) == 17
    
def test_PorI():
    #9^2 + 1^2 + 1^2 = 83 --> 83^(1/2)
    assert LA.PorI(v3) == 83**(1/2)
    
    #9
    assert LA.PorI(v2,4,True) == 9
    
def test_Dot():
    #(7-24i)5 + 4(5-12i) + 7(8+15i)
    #35 - 120i + 20 - 48i +56 +105i = 111-63i
    assert LA.Dot(v4, v5) == 111-63j
    
    #5(1) + (5+12i)2 + (8-15i)4
    #5 + 10 + 24i + 32 - 60i = 47-36i
    assert LA.Dot(v5, v1) == 47-36j
    
pytest.main()