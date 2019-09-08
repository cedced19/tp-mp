import numpy as np 
import matplotlib.pyplot as plt
from math import *
import scipy.integrate as integr

def Iteres_1(n):
    res=np.arange(n+1)+1
    while n>0:
        res=np.sin(res)
        n-=1
    return res
    
def Iteres_2(n):
    res=(n+1)*[1.]
    for i in range(n):
        res[i+1]=np.sin(res[i])
    return res
    
def x(n):
    res=1
    while n>0:
        res=np.sin(res)
        n-=1
    return res 
    
def Iteres_3(n):
    res=list(range(n+1))
    for i in res:
        res[i]=x(i)
    return res 

    
def Draw(n):
    x=1
    List_X=[x]
    List_Y=[0]
    for k in range(n):
        y=np.sin(x)
        List_X.append(x)
        List_Y.append(y)
        List_Y.append(y)
        List_X.append(y)
        x=y
    plt.plot(List_X,List_Y,"r")
    x=np.arange(0,1,0.01)
    y=[np.sin(k) for k in x]
    plt.plot(x,y,"r")
    plt.plot(x, x, "g")
    plt.show()
    
    
def Draw_Serie(n):
    x=1
    List_X=[x]
    List_Y=[0]
    for k in range(n):
        y=(np.sin(x)+x)*(-1)
        List_X.append(x)
        List_Y.append(y)
        List_Y.append(y)
        List_X.append(y)
        x=y
    plt.plot(List_X,List_Y,"r")
    x=np.arange(-max([max(List_Y),max(List_X)]),max([max(List_Y),max(List_X)]),0.01)
    plt.plot(x, x, "g")
    plt.show()
    
    
L=[1,3,3,-1]
    
def Formatage(L):
    n=len(L)
    M=[]
    i=0
    while(i<n-1):
        if (L[i]==L[i+1]):
            M.append(0)
        else:
            if (L[i]<L[i+1]):
                M = M + (L[i+1]-L[i])*[1]
            else:
                M = M + (L[i]-L[i+1])*[-1]
        i+=1
    return M 
    

def Trace(L):
     M=Formatage(L)
     X=range(len(M)+1)
     Y=[L[0]]
     for i in range(1,len(M)):
         Y.append(Y[i-1]+M[i-1])
     Y.append(Y[-1]+M[-1])
     plt.plot(X, Y, "g")
     plt.show()


     
def Sol():
    def f(x,t):
        return -x+cos(10*t)
    T = np.arange(0,2.01,0.01)
    X=integr.odeint(f,3,T)
    plt.plot(T,X)
    plt.show()



     
def Resolution():
    def f(x,t):
        return np.array([x[0]*(2-x[1]),x[1]*(x[0]-1)])
    T = np.arange(-10,10,0.01)
    x0=np.array([2,1])
    X=integr.odeint(f,x0,T)
    
    plt.plot(T,X[:,0], "b")
    plt.plot(T,X[:,1], "r")
    plt.grid()
    plt.title("un titre")
    
    plt.show()