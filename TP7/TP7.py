import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

n=5
M=[[random.binomial(1,0.7) for i in range(n+1) ] for i in range(n+1)]
print(np.shape(M))
plt.imshow(M,cmap="binary",interpolation="nearest")


# Ou

random.binomial(1,0.7,(5,5))

#
#def Chiffre(code,k):
#    a = code
#    r=0
#    for i in range(k+1):
#        r = a%2
#        a= a//2
#    return r
# Plus simple


def Chiffre(code,k):
    return (code // 2**k) %2

def Chiffres(code):
    return [Chiffre(code,8-i) for i in range(1,9)]
    

print([Chiffres(i) for i in range(30+1)])

def NouvelEtat(code,tableau):
    new = tableau[:]
    long = len(tableau)
   
    def getNumber(i):
        left=(i+1)%long
        right=(i-1)%long
        return tableau[left]*4+tableau[i]*2+tableau[right]
    for i in range(long):
        new[i]=Chiffre(code,getNumber(i))
    return new
    
def Graphique(code,tableau,n):
    M=[tableau]
    for i in range(1,n):
        M.append(NouvelEtat(code,M[-1]))
    plt.figure()
    plt.title("Code " + str(code) + " Taille du tableau " + str(len(tableau)) + " Nombre d'étapes " + str(n))
    plt.imshow(M,cmap="binary",interpolation="nearest")
    plt.show()
    
    
def Tableau(n,p):
    return [random.binomial(1,p) for i in range(2*n+1)]
    

Graphique(2,[0,1,0,1,1,0],5)
Graphique(150,Tableau(100,0.8),100)
Graphique(89,Tableau(100,0.4),100)
Graphique(150,Tableau(100,0.5),100)
Graphique(150,50*[0]+[1]+50*[0],100)


####################

def Cn (n):
    S=0
    for i in range(1,n+1):
        P=1
        for j in range(1,n+1):
            if (i!=j):
                P*=j
        S+=P
    return S 

print(Cn(3))


def Eratosthene(n):
    B=[True]*(n+1)
    B[0]=False 
    B[1]=False
    for i in range(2,n+1):
        if (B[i]==True):
            for j in range(2*i,n+1,i): # boucle avec un pas de i
                B[j]=False
    return B
    
print(Eratosthene(1000))

Prem = [i for i in range(1001) if (Eratosthene(1000)[i]==True)]
Test = [ Cn(p-1) % (p*p) for p in Prem]


####################

def tirage():
    return random.binomial(1,0.5)
    
# Notons 1 -> P  et 0 -> F
def premiere_apparition():
    test = False
    actuel=tirage()
    n=0
    while True:
        essai=tirage()
        if (actuel==1) and (essai==0):
            return n+1
        actuel=essai
        n+=1

print(premiere_apparition())

def esperance(n):
    E=0
    for i in range(n):
        E+=premiere_apparition()*1/n
    return E 
    
print(esperance(10000))

