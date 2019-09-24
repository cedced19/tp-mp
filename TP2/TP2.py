



#1
def Inverse (sigma):
    L=len(sigma)*[0]
    for i in range(len(sigma)):
        L[sigma[i]]=i
    return L

#print(Inverse(L))

#2a

def Rond(sigma1,sigma2):
    L=len(sigma1)*[0]
    for i in range(len(sigma2)):
        L[i]=sigma1[sigma2[i]]
    return L

#print(Rond(L, Inverse(L)))
#print(Rond(Inverse(L), Inverse(L)))

#print(Rond(L, L))

def Ordre(sigma):
    def compare(L):
        exist=False
        for i in range(len(L)):
            if (L[i] != i):
                exist=True
        return exist

    ordre=1
    L=sigma
    while compare(L):
        ordre+=1
        L=Rond(L,sigma)
    return ordre

#print(Ordre(L))


def ListePermutation(n):
    if (n==1):
        return [[0]]
    else:
        tmp=ListePermutation(n-1)
        L=[]
        for sigma in tmp:
            for k in range(len(sigma)+1):
                N=sigma[:]
                N.insert(k,n-1)
                L.append(N)
        return L

#print(ListePermutation(3))

def pgcd (a, b):
    if (a < b):
        (a,b)=(b,a)
    q=a//b
    r=a%b
    while (r != 0):
        a=b
        b=r
        q=a//b
        r=a%b
    return b

def pgcd_rec (a,b):
    if (b==0):
        return a
    else:
        return(pgcd_rec(b,a%b))

#print(pgcd(12,3))

def ppcm_rec(L):
    if (len(L)==2):
        return (L[0]*L[1])/(pgcd(L[0],L[1]))
    else:
        return ppcm_rec([ppcm_rec(L[1:]), L[0]])

#print(ppcm_rec([5,6,8]))

def Decomp_Transpo(sigma): #
    if (len(sigma)==2):
        return [sigma]
    else:
        lon=len(sigma)
        if (sigma[lon-1] == lon-1):
            return Decomp_Transpo(sigma[:-1])
        t=0
        
        for k in range(lon):
            if (sigma[k]==lon-1):
                t=k
                break
        L=sigma[:]
        L[t]=sigma[-1]
        L=sigma[:-1]
        
        return Decomp_Transpo(L) + [[t, lon-1]]

L=[2,5,1,3,4,0]
print(Decomp_Transpo(L))
print(Decomp_Transpo([0,2,1]))

def Est_Alternee(sigma):
    decomp = Decomp_Transpo(sigma)
    return  bool(len(decomp)%2)

#print(Est_Alternee(L))

def Liste_Alternee(n):
    L=ListePermutation(n)
    La=[]
    for item in L:
        #print(Decomp_Transpo(item), item, Est_Alternee(item))
        if (Est_Alternee(item)):
            La.append(item)
    return La


#print(Liste_Alternee(3))