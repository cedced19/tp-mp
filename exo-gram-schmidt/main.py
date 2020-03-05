

import numpy as np 
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt 
import scipy.integrate as integr 


def scalaire (P,Q):
    A=Polynomial(P)
    B=Polynomial(Q)
    C=(A*B).integ()
    return C(1)-C(-1)

#print(scalaire([1],[1]))

def norme (P):
    return np.sqrt(scalaire(P,P))

def gram_schmidt (n):
    base=np.array([[0]*(n)]*(n))
    for i in range(n):
        base[i][i]=1
    result = []

    result.append(base[0]/norme(base[0]))

    for i in range(1,n):
        vector=base[i]
        for k in range(0,i):
            vector=vector-scalaire(base[i],result[k])*result[k]
        result.append(vector/norme(vector))

    return(np.array(result))

print(gram_schmidt(5))

def valuate_P (P, x):
    d=len(P)
    S=0
    for i in range(len(P)):
        S+=P[d-1-i]
        S*=x
    return S

#print(valuate_P([0,0,1],5))

def tracer(arr):
    X=np.arange(-1,1,0.01)
    for P in arr:
        Y=[valuate_P(P,x) for x in X]
        plt.plot(X,Y)
    plt.show()

tracer(gram_schmidt(3))