
import math

def estPremier(n):
    if (n<=1):
        return False
    if (n==2):
        return True
    p=2
    d=(math.sqrt(n))
    while (p<=d): 
        if n%p == 0:
            return False
        p+=1
    return True

#print(estPremier(17))

def liste_premiers (n):
    L = []
    for i in range(n+1):
        if estPremier(i):
            L.append(i)
    return L 

#print(liste_premiers(30))

def valuation_p_adique (n,p):
    k=n
    i=0
    while (k%p) == 0:
        i+=1
        k=k//p
    return i

#print(valuation_p_adique(40,2))
#print(valuation_p_adique(40,5))
#print(valuation_p_adique(40,7))

def val(n,p):
    if (n%p) == 0:
        return 1+val(n//p,p)
    else:
        return 0


#print(val(40,2))
#print(val(40,5))
#print(val(40,7))


def decomposition_facteurs_premiers(n):
    L=[]
    for p in liste_premiers(n):
        tmp = val(n,p)
        if(tmp!=0):
            L.append([p,tmp])
    return L

print(decomposition_facteurs_premiers(40))