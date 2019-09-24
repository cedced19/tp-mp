import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integr
import numpy.random as rd


def f(x):
    return np.exp(-1*(x**2))
    
#integr.quad(f, 0 , 1)


def Rectangle(n):
    S=0
    h=0
    for i in range(0,n):
        S+=f(h) * (1/n)
        h+=1/n
    return S
    

#Rectangle(100)

def Trapezes(n):
    S=0
    h=0
    f1=f(0)
    for i in range(0,n):
        h+=1/n
        f2=f(h)
        S+=(f2+f1)* (1/2) * (1/n)
        f1=f2
    return S
    
#Trapezes(100)

    
    

def tracer(F):
    I,e=integr.quad(f, 0 , 1)
    x=[]
    y=[]
    n=1
    for i in range(1,5):
        x.append(i)
        val=F(n)
        lim = (10**(-i))
        while(abs(I-val)>lim):
            n+=(10**(i-1))
            val=F(n)
        y.append(n)
    plt.plot(x,y)
    plt.semilogy() # echelle log
    plt.grid()
    plt.show()




def calcul(F):
    I,e=integr.quad(f, 0 , 1)
    x=[]
    y=[]
    n=1
    for i in range(1,5):
        x.append(i)
        val=F(n)
        lim = (10**(-i))
        while(abs(I-val)>lim):
            n+=1
            val=F(n)
        y.append(n)
    return x, y


def tracer2():
    x,yt=calcul(Trapezes)
    x,yr=calcul(Rectangle)
    plt.figure()
    plt.semilogy() # echelle log
    plt.plot(x,yt, marker="o")
    plt.plot(x,yr, marker="x")
    plt.legend(('trapèzes', 'rectangles'), loc="upper left")
    plt.title("Compaire")
    plt.grid()
    plt.show()
        
def Test_Imshow():
    plt.figure()
    plt.imshow(np.zeros((10,10)))
    plt.show()

def Mandel(n,p):
    M=np.zeros((n,n))
    x=np.linspace(-2,2,n)
    y=np.linspace(-2,2,n)
    for i in range(n):
        for j in range(n):
            c=x[i]+1j*y[j]
            z=0
            for k in range(0,p):
                z=z**2+c
                if (abs(z)>=4):
                    M[i,j]=k
                    break
    plt.figure()
    plt.imshow(M)
    plt.show()
    
def Julia(n,p,c):
    M=np.zeros((n,n))
    x=np.linspace(-2,2,n)
    y=np.linspace(-2,2,n)
    for i in range(n):
        for j in range(n):
            z0=x[i]+1j*y[j]
            z=z0
            for k in range(0,p):
                z=z**2+c
                if (abs(z)>=4):
                    M[i,j]=k
                    break
    plt.figure()
    plt.imshow(M)
    plt.show()
    
#Julia(500,40,-0.123+1j*0.745)

def Spirale(n):
    M=np.zeros((n,n))
    
    i,j=(n-1)//2,n//2-1
    M[i,j]=1
    M[i,j+1]=2
    
    u=[0,1]
    
    k=3
    j+=1
    while(k<=n**2):
        if (M[i-u[1],j+u[0]]==0):
            u=[-u[1],u[0]]
        i+=u[0]
        j+=u[1]
        M[i,j]=k
        k+=1
    return M 
    
print(Spirale(5))
