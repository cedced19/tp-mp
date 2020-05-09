
import numpy.random as rd
import numpy as np


def rand0(n):
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i][j]=rd.randint(1, 100)
    return np.linalg.qr(A)[0]


#print(rand0(3))

def N1 (A):
    ni,nj=A.shape
    S=0
    for i in range(ni):
        for j in range(nj):
            S+=abs(A[i][j])
    return S

#print(N1(np.ones((2,3))))


def test (n):
    mini = float('+inf')
    maxi = 0
    for i in range(10000):
        v=N1(rand0(n))
        if (v>maxi):
            maxi=v
        if (mini>v):
            mini=v
    return (mini,maxi)

print(test(3))



