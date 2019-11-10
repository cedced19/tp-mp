#
#                 Electrocinétique
#
#        Shooting Method et Fonction de transfert
#


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve # newton
from scipy.optimize import bisect # dichotomie

pi = np.pi

##
#
#    I. Présentation de la méthode de tir sur un exemple simple
##

#       On se propose de déterminer, dans le cas d'un circuit RC,
#       la réponse en régime périodique établi à un signal carré.

#__  Expression du signal d'entrée __

def Ue( t ):
    """ Signal carré, de caractéristiques en unités arbitraires :
        période T = 2, valeur moyenne Uem = 0.5,
        valeur crête à crête Uepp = 1.0 """
    return np.piecewise( t, [ np.floor(t) % 2 ], [0.0, 1.0] )

ts = np.linspace(0, 4.5, 450 )
plt.figure()
plt.plot( ts, Ue( ts ), lw = 2 )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()

#__ Equation différentielle vérifiée par Us(t) __

def ODE( Us, t, tau = 1. ):
    return ( Ue(t) - Us ) / tau

Us = odeint(ODE, [0], ts, (0.5,) )  # Le paramètre est un tuple !

plt.figure()
plt.plot( ts, Ue( ts ), lw = 2 )
plt.plot( ts, Us, lw = 2, linestyle = '--' )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()

# Résolution pour différentes valeurs du paramètre tau

Ltau = [0.5, 1.0, 2] # Liste des valeurs de tau

plt.figure()
plt.plot( ts, Ue( ts ), lw = 2 )
for tau in Ltau :
    Us = odeint(ODE, [0], ts, (tau,) )
    plt.plot( ts, Us, lw = 2, linestyle = '--' )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()

#__ Détermination du régime périodique ( shooting method ) __

#   Il s'agit de déterminer la valeur de Us( 0 ) telle que :
#               Us( 2 ) = Us( 0 )

def f( initial_value ):
    """ Retourne l'écart  Us(T-) - Us(0+) """
    T = np.linspace(0, 2, 450)
    final_value = odeint(ODE, [ initial_value ], T )[-1][0]
    return final_value -  initial_value

X = np.linspace(0, 1)
Y = [ f( value ) for value in X ]

plt.figure()
plt.plot( X, Y, lw = 2 )
plt.grid()
plt.show()

xp = bisect( f, 0, 1 )

plt.figure()
plt.plot( X, Y, lw = 2 )
plt.plot( xp,f(xp), marker = '+', ms = 10, \
          mec = 'm',  mfc = 'none' , mew = 2 )
plt.grid()
plt.show()

# Solution en régime périodique établi Uspe,
# déterminée à partir de la valeur xp

Uspe = odeint(ODE, [ xp ], ts )

plt.figure() 
plt.plot( ts, Ue( ts ), lw = 2 )
plt.plot( ts, Uspe, color = 'magenta', lw = 2 )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()

##
#
#    II. Décomposition en série de Fourier et 
#             et Fonction de transfert  
##


# Décomposition du signal d'entrée en série de Fourier

def Uep(t, p):
    return 2*np.sin( (2*p+1)*pi*t ) / ( pi * (2*p+1) )
    
# Somme des n+1 premiers termes de la série de Fourier
def DSF_Ue( t, n):
    rep = 0.5 
    for p in range( n ):
        rep += Uep(t, p)
    return rep
    
plt.figure()
plt.plot( ts, Ue( ts ), lw = 2 )
plt.plot( ts, DSF_Ue( ts, 10 ), lw = 2 )
plt.ylim(-0.15, 1.15 ) 
plt.grid()
plt.show()


## à compléter .......

# A l'aide de la fonction de transfert, écrire une fonction
# Usp(t, p) renvoyant la tension de sortie, en régime sinusoïdal
# forcé, obtenue pour une tension d'entrée Uep(t). 

def Usp(t, p):
    omegaUe = (2*p+1)*pi
    H=1/(np.sqrt(1+omegaUe*omegaUe))
    return 2 * H * np.sin (omegaUe * t -np.arctan(omegaUe)) / ( pi * (2*p+1) )

# Ecrire une fonction DSF_Us(t, n), renvoyant 
# la somme des n+1 premiers termes de la décomposition
# en série de Fourier de la tension Us(t), obtenue en
# régime périodique pour le signal d'entrée Ue(t)

def DSF_Us(t, n):
    rep = 0.5 * np.ones_like(t)
    for p in range( n ):
        rep += Usp(t, p)
    return rep

# Vérifier les résultats par un tracé en comparant à Uspe
plt.figure() 
plt.plot( ts, Ue( ts ), lw = 2 )
plt.plot( ts, Uspe, color = 'magenta', lw = 2 )
plt.plot( ts, DSF_Us(ts, 42 ), color = 'red', lw = 2 )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()

# _____________________________________________________________ #

#  Reprendre l'étude ci-dessus dans le cas d'une tension
#  d'entrée Ve(t) = np.abs( np.sin( pi*t ) )
#  Les tracés seront faits sur [0, 2.5]

def Ve( t ):
    return np.abs( np.sin( pi*t ) )

ts = np.linspace(0, 2.5, 450 )
plt.figure()
plt.plot( ts, Ve( ts ), lw = 2 )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()

def Vep(t, p):
    return (-4/pi)*(np.cos(2*pi*p*t))/((4*p*p-1))
    
# Somme des n+1 premiers termes de la série de Fourier
def DSF_Ve( t, n):
    rep = 2/pi 
    for p in range(1, n ):
        rep += Vep(t, p)
    return rep
    
plt.figure()
plt.plot( ts, Ve( ts ), lw = 2 )
plt.plot( ts, DSF_Ve( ts, 10 ), lw = 2 )
plt.ylim(-0.15, 1.15 ) 
plt.grid()
plt.show()

def Vsp(t, p):
    omegaUe = 2*pi*p
    H=1/(np.sqrt(1+omegaUe*omegaUe))
    return (-4/pi) * H * np.cos (omegaUe * t -np.arctan(omegaUe)) / ((4*p*p-1) )

def DSF_Vs(t, n):
    rep =  2/pi  * np.ones_like(t)
    for p in range( n ):
        rep += Vsp(t, p)
    return rep

# Vérifier les résultats par un tracé en comparant à Uspe
plt.figure() 
plt.plot( ts, Ve( ts ), lw = 2 )
plt.plot( ts, DSF_Vs(ts, 42 ), color = 'red', lw = 2 )
plt.ylim(-0.05, 1.05 ) 
plt.grid()
plt.show()
