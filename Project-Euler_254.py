def fact(n):
    q=1
    for i in range(1,n+1):
        q*=i
    return q

def f(l):
    l=list(str(l))
    p=0
    for i in range(len(l)):
         p+=fact(int(l[i]))
    return p
    
def sf(l):
    s=0
    l=list(str(f(l)))
    for i in range(len(l)):
        s+=int(l[i])
    return s
def g(n,r):
    x=1
    for i in range(1,r):
        if sf(i)==n:
            x=i
            break
    return x

def sg(l,r):
    s=0
    l=list(str(g(l,r)))
    for i in range(len(l)):
        s+=int(l[i])
    return s

def sommeSg(n,r):
    s=0
    for i in range(1,n+1):
        s+=sg(i,r)
    return s%r

if __name__ == '__main__':

    q=int(input(""))
    p,n=[],[]
    j=1
    for i in range(q):
        p.append(0)
        n.append(0)
    for i in range(q):
        entree=input().split(" ")
        p[i]=int(entree[0])
        n[i]=int(entree[1])

    for i in range(q):
        print(sommeSg(p[i],n[i]))

