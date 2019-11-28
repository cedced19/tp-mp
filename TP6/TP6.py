

# Exercice 4

from math import *
from numpy.polynomial import Polynomial

def ps(p, q):
    integre=((p*q).integ())
    return (integre(1)-integre(0))

#print(ps(Polynomial([1]),Polynomial([0,1])))

def baseortho(m):
    if (m==0):
        return [Polynomial([1])]
    else:
        nouveau_monome = Polynomial([0]*(m)+[1])
        #print(nouveau_monome)
        l = baseortho(m-1)
        coeff=[1]*(m+1)
        #print(coeff)
        for i in range(m):
            coeff[i]=-ps((nouveau_monome), l[i])
        norme = sqrt(ps(Polynomial(coeff),Polynomial(coeff)))
        return l + [Polynomial(coeff)/norme]

#print(baseortho(1))

# Exercice 5

import numpy as numpy
import numpy.linalg as alg

P = [2,-1,1,1,-5,1]

def Base (n):
    L=[P]
    for i in range(0,5):
        L + [Polynomial(L[0]).deriv().coef]
    return L

print(Base(5))





