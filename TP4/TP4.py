

def binom(n,p):
    if (p==0):
        return 1
    if (p==1):
        return n
    return binom(n-1,p-1) + binom(n-1,p)

#print(binom(2,1))

def binom2(n,p):
    if (p==0):
        return 1
    if (p==1):
        return n
    return ((n)*(binom2(n-1,p-1)))//p

#print(binom2(8,5))

def somme(n):
    return n + somme(n-1)

def somme_rec(n, accu):
    if (n == 0):
        return accu
    return somme_rec(n-1, accu+n)

def base(n,b):
    k=n
    L=[]
    while (k!=0):
        L.append(k%b) 
        k = k//b
    return L

#print(base(42,2))

def base_rec(n,b):
    if (n==0):
        return []
    else:
        return [n%b] + base_rec(n//b,b) 

print(base_rec(6,2))

def lexico_inf(a,b):
    if (a[0]<b[0]):
        return True
    if (a[0]>b[0]):
        return False
    if (a[0]==b[0] and a[1]<=b[1]):
        return True 
    return False 

def lexico_rec(a,b):
    if (len(a)==0):
        return False
    if (a[0]>b[0]):
        return False
    if (a[0]<b[0]):
        return True
    return lexico_rec(a[1:],b[1:])

#print(lexico_rec([8,9],[9,9]))

def bell (n):
    a = [1,1]
    for i in range(2,n+1):
        S = 0
        for k in range(i):
            S+=binom2(i-1,k)*a[k]
        a.append(S)
    return a

#print(bell(3))

def parties_rec(E):
    if (len(E)==0):
        return [[]]
    S = parties_rec(E[1:])
    R = []
    for P in S:
        R.append(P+[E[0]])
    return R + S

#print(parties_rec([1,8,9,3]))

def Horner(P, x):
    if (len(P)==0):
        return P
    return P[0] + x*Horner(P[1:],x)


def generation(d):
    if (d==0):
        return [[0], [1]]
    L=generation(d-1)
    R=[]
    for P in L:
        R.append([0]+P)
        R.append([1]+P)
    return R

#print(generation(8))
