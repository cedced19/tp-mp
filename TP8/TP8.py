import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

#plt.imshow(M,cmap="gray",interpolation="nearest")


def d (pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def Voisins (M,point):
    n,n =  np.shape(M)
    L=[]
    for i in range(n):
        for j in range(n):
            if (d(point,(i,j))==1):
                L.append((i,j))
    return L
    
M = np.ones((5,5))

print(Voisins(M, (2,2)))
print(Voisins(M, (4,4)))
print(Voisins(M, (0,2)))




def Comp_Connexe (M,point):
    if (M[point]==0):
        return []
    def Est_Inclu(L,el):
        test = False
        for l in L:
            if (el==l):
                test = True
        return test
    L=[point]
    done=[point]
    init=Voisins(M,point)
    while (len(init)!=0):
        el = init.pop()
        done.append(el)
        print(el, done, init, L)
        if (Est_Inclu(L,el) == False) and (M[el]==1):
            L.append(el)
            voisins = Voisins(M,el)
            for v in voisins: ## On peut aussi les passer à 0: beaucoup plus efficace
                if (not Est_Inclu(done,v)):
                    init.append(v)
    return L 
    
def Couleur_Aleat():
    return (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    
def Afficher_Matrice():
    n=30
    M=[[(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)) for i in range(n+1) ] for i in range(n+1)]
    plt.imshow(M)


print(M)
print(Comp_Connexe(M, (0,2)))


M = np.eye(5)
print(M)
print(Comp_Connexe(M, (0,2)))
N = np.ones((5,5)) - np.eye(5)
print(N)
print(Comp_Connexe(N, (0,2)), len(Comp_Connexe(N, (0,2))))

Afficher_Matrice()

def Color_Compos_Connexe(M,point):
    n,n =  np.shape(M)
    Mp=[[(M[i,j],M[i,j],M[i,j]) for i in range(n) ] for j in range(n)]
    Mp[point[0],point[1]]=(0.5,0.5,0.5)
    print(Mp)
    plt.figure()
    plt.imshow(M,interpolation="nearest",cmap="gray")
    plt.show()
    
Color_Compos_Connexe(N, (0,2))
