
import numpy as np 
import numpy.random as rd 
import matplotlib.pyplot as plt


def Dirichlet (n):
    A=rd.random((n,n))
    for i in range(n):
        A[0,i]=1.0
    for i in range(n):
        A[i,0]=0
        A[i,n-1]=0
        A[n-1,i]=0
    return A 
    
def Laplace(V,N):
    n=len(V)
    W=np.zeros((n,n)) # Créations d'un tableau de stockage
    for i in range(1,n-1):
        W[0,i]=1.0
    for k in range(N):
        for i in range(1,n-1):
            for j in range(1,n-1):
                W[i,j]=(1/4)*(V[i+1,j]+V[i-1,j]+V[i,j-1]+V[i,j+1])
        V=W
    return V

def Chrono (n,N):
    from time import clock
    t1 = clock()
    Laplace(Dirichlet(n),N)
    t2=clock()
    print(t2-t1)


def Show(V):
    plt.imshow(V)
    
def Laplace2(V,N):
    for k in range(N):
        V[1:-1, 1:-1]=0.25*(V[1:-1, :-2]+V[1:-1, 2:]+V[:-2, 1:-1]+V[2:, 1:-1])
    return V
    
def EquiV (V):
    n=len(V)
    y=np.linspace(-0.5,0.5,n)
    x=np.linspace(-0.5,0.5,n)
    
    X,Y = np.meshgrid(x,y)
    levels= np.array([0.02,0.05,1,0.04,0.2])
    plt.figure()
    plt.contour(X,Y,V,levels,linewidths=3)
    plt.plot([-0.5,-0.5,0.5,0.5],[-0.5,0.5,0.5,-0.5], 'k', lw=4) # V=0 sur les bords
    plt.plot([-0.5,0.5],[-0.5,-0.5], 'r', lw=4) # V=1 sur un seul bord
    plt.axis=('equal')
    plt.ylim(-0.6,0.6)
    plt.show()
    
def ObtenirE(V):
    return ((V[1:-1, :-2]-V[1:-1, 2:]),V[:-2, 1:-1]-V[2:, 1:-1])
    
def ObtenirEn(V):
    Ex,Ey=ObtenirE(V)
    n=np.sqrt(Ex*Ex+Ey*Ey)
    return (Ex/n, Ey/n)


def ObtenirEx2(V):
    n=len(V)
    Ex=np.zeros_like(V)
    for i in range(1,n-1):
        for j in range(1,n-1):
            Ex[i,j]=-(V[i,j+1]-V[i,j])

def EquiV_LDC (V):
    n=len(V)
    y=np.linspace(-0.5,0.5,n)
    x=np.linspace(-0.5,0.5,n)
    
    X,Y = np.meshgrid(x,y)
    Xc=X[1:-1,1:-1]
    Yc=Y[1:-1,1:-1]
    levels= np.array([0.02,0.05,1,0.04,0.2,0.1,0.4,0.3])
    plt.figure()
    plt.contour(X,Y,V,levels,linewidths=3)
    Enx,Eny=ObtenirEn(V)
    plt.quiver(Xc[5::15,5::15],Yc[5::15,5::15],Enx[5::15,5::15],Eny[5::15,5::15])
    plt.plot([-0.5,-0.5,0.5,0.5],[-0.5,0.5,0.5,-0.5], 'k', lw=4) # V=0 sur les bords
    plt.plot([-0.5,0.5],[-0.5,-0.5], 'r', lw=4) # V=1 sur un seul bord
    plt.axis=('equal')
    plt.ylim(-0.6,0.6)
    plt.show()

# On peut éventuellement voir que le potentiel au centre = 0,25 quand N grand