
def base(n,b):
    k=n
    L=[]
    while (k!=0):
        L.append(k%b) 
        k = k//b
    return L

def base_rec(n,b):
    if (n==0):
        return []
    else:
        return [n%b] + base_rec(n//b,b) 


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
        return Truef
    return lexico_rec(a[1:],b[1:])
    
def palindrome(s):
    if len(s)<2:
        return True
    else: 
        return (s[0]==s[-1]) and palindrome(s[1:-1])
        
def anagramme(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if (l1 == 0 or l2 == 0):
        return True
    if (l1 != l2):
        return False
    else:
        test = s2.find(s1[0])
        if (test != -1):
            return anagramme(s1[1:], s2[0:test]+s2[test+1:])
        else:
            return False 
def une_passe(l):
    def aux(l, b):
        n = len(l)
        if (n <= 1):
            return (l, b)
        else:
            if (l[-2]<=l[-1]):
                r = aux(l[:-1], b)
                return (r[0]+ [l[-1]], r[1])
            else:
                return (aux(l[:-2] + [l[-1]], True)[0]+ [l[-2]], True)
    return aux(l,False)
                
def drapeau_hollandais(l):
    r=une_passe(l)
    if (r[1] == False):
        return l
    else:
        return drapeau_hollandais(r[0])
        

import random 

def Generateur_Liste_Alea(n,a,b):
    return [random.uniform(a,b) for i in range(n)]


def esperance(l):
    return sum(l)/len(l)
    
def Generateur_Parties(n):
    if (n==1):
        return ([[0],[1]])
    S = Generateur_Parties(n-1)
    R = []
    for P in S:
        R.append(P+[0])
        R.append(P+[1])
    return R

def Partie(n):
    def parties_rec(E):
        if (len(E)==0):
            return [[]]
        S = parties_rec(E[1:])
        R = []
        for P in S:
            R.append(P+[E[0]])
        return R + S
    return parties_rec(list(range(n)))


def hanoi (n, a, b, c):
    if (n != 1):
        hanoi (1, a, b, c)
        hanoi(n-1, a, c, b)
        hanoi(n-1, c, b, a)
    if (n==1):
        print(a, ' vers ', b)

#hanoi(2, 'a', 'b', 'c')
hanoi(3, 'a', 'b', 'c')