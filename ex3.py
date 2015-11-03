__author__ = 'student'
inp=open('input.txt','r')
a=inp.readlines()
for x in range(len(a)):
    a[x]=a[x].rstrip()
for x in range(len(a)):
    for y in range(len(a[x])):
        t=''
        if a[x][y]=='!' or a[x][y]=='.' or a[x][y]=='?' or a[x][y]==',':
            a[x]=list(a[x])
            a[x][y]=' '
            for u in range(len(a[x])):
                t+=str(a[x][u])
            a[x]=str(t)
Slova=dict()
for x in range(len(a)):
    a[x]=a[x].lower()
b=''
for x in range (len(a)):
    a[x]+=' '
for x in range(len(a)):
    i=0
    for y in range(len(a[x])):
        if a[x][y]==' ' and a[x][y-1]!=' ':
            b+=a[x][i:y]
            i=y
            b+=' '
p=0
slova={}
n=0
c=[]
for x in range(1,len(b)):
    if b[x]==' ' and b[x-1]!=' ':
        c.append(b[n:x])
    if b[x]==' ':
        n=x+1
print(c)
for word in c:
    if word in slova:
        slova[word]+=1
    else:
        slova[word]=1
m=0
for word in slova:
    if slova[word]>m:
        m=slova[word]
for word in slova:
    if slova[word]==m:
        print(word,'vstrechaetsya',m,'raz')
