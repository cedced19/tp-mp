import numpy as np 
import matplotlib.pyplot as plt
from math import *

def Draw(u,f,n):
    x=u
    List_X=[u]
    List_Y=[0]
    for k in range(n):
        y=f(x)
        List_X.append(x)
        List_Y.append(y)
        List_Y.append(y)
        List_X.append(y)
        x=y
    plt.plot(List_X,List_Y,"r")
    X_MIN,X_MAX,Y_MIN,Y_MAX=min(List_X),max(List_X),min(List_Y),max(List_Y)
    plt.axis([0,X_MAX+0.5,0,Y_MAX+0.5])
    plt.plot([X_MIN-1,X_MAX+0.5],[X_MIN-1,X_MAX+0.5],"b")
    x=np.linspace(0,X_MAX+0.5,200)
    y=[f(k) for k in x]
    plt.plot(x, y,"g")
    
    plt.show()
    


def f (x):
    return 1/(2-sqrt(x))

Draw(2.8,f, 50)
plt.clf()
Draw(1.1,f, 50)
plt.clf()
Draw(2.5,f, 50)