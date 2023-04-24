'''
s=input().split()
for i in range(len(s)):
    s[i]=len(s[i])
s=sorted(s)
for i in range(len(s)-1):
    if s[i]!=0:
        k=1
        j=i+1
        while s[i]==s[j]:
            k+=1
            s[j]=0
            if j+1<len(s):
                j+=1
        s[i]=str(s[i])+':'
        print(s[i],k)
if s[len(s)-1]!=0:
    s[len(s)-1]=str(s[len(s)-1])+':'
    print(s[len(s)-1],1)
'''
'''
s=input().split()
for i in range(len(s)-1):
    k=False
    if s[i]!=-1:
        for j in range(i+1,len(s)):
            if s[j]==s[i]:
                k=True
                s[j]=-1
        if k:
            print(s[i],end=' ')
'''
'''
n=int(input())
k=1
f=1
while f<=n:
    for i in range(k):
        print(k,end=' ')
    k+=1
    f+=k
f-=k
for i in range(n-f):
    print(k,end=' ')
'''
'''
s=input().split()
n=input()
k=False
for i in range(len(s)):
    if s[i]==n:
        print(i,end=' ')
        k=True
if k==False:
    print('None')
'''
'''
s=input().split()
s='_'.join(s)
print(s)
'''
'''
print('_'.join(input().split()))
'''
'''
s=list(input())
s[0]=s[0].upper()
for i in range(len(s)):
    if s[i]=='_':
        s[i]=''
        s[i+1]=s[i+1].upper()
print(''.join(s))
'''
'''
n=int(input())
print(n,end=' ')
while n!=1:
    if n%2==0:
        n=n//2
        print(n, end=' ')
    else:
        n=3*n+1
        print(n,end=' ')
'''
'''
k=True
while k:
    n=input()
    if n=='End':
        print('Good bye!')
        break
    print('Processing', '"'+n+'"', 'command...')
'''
'''
n=int(input())
k=n
name=1
up,down,left,right=0,n-1,0,n-1
s=[[0 for i in range(n)] for j in range(n)]
s[0][0]=1
while k>0:
    for i in range(left,right+1):
        s[i][up]=name
        name+=1
    up+=1
    for j in range(up,down+1):
        s[right][j]=name
        name+=1
    right-=1
    k-=1
    if k>0:
        for i in range(right,left-1,-1):
            s[i][down]=name
            name+=1
        down-=1
        for j in range(down,up-1,-1):
            s[left][j]=name
            name+=1
        left+=1
    k-=1
for j in range(n):
    for i in range(n):
        print(s[i][j],end=' ')
    print()
'''
'''
k=0
s=input().split()
for i in range(len(s)):
    if s[i]=='A':
        k+=1
print("%0.2f" % (k/len(s)))
'''
'''
p=input().split()
n,m=int(p[0]),int(p[1])
s=[[0 for i in range(m)] for j in range(n)]
for j in range(n):
    v=input()
    for i in range(m):
        s[j][i]=v[i]
for i in range(n):
    for j in range(m):
        up,down,right,left=False,False,False,False
        if s[i][j]!='*':
            k=0
            if (i!=0):
                up=True
            if (i!=n-1):
                down=True
            if (j!=0):
                left=True
            if (j!=m-1):
                right=True
            if up:
                if s[i - 1][j] == '*':
                    k+=1
                if left:
                    if s[i - 1][j-1] == '*':
                        k += 1
                if right:
                    if s[i - 1][j+1] == '*':
                        k += 1
            if down:
                if s[i + 1][j] == '*':
                    k+=1
                if left:
                    if s[i + 1][j-1] == '*':
                        k += 1
                if right:
                    if s[i + 1][j+1] == '*':
                        k += 1
            if right:
                if s[i][j+1] == '*':
                    k+=1
            if left:
                if s[i][j-1] == '*':
                    k+=1
            s[i][j]=k
for j in range(n):
    for i in range(m):
        print(s[j][i],end='')
    print()
'''
'''
s=input().split()
if s[1]=='plus':
    print(int(s[0])+int(s[2]))
elif s[1]=='minus':
    print(int(s[0])-int(s[2]))
elif s[1]=='multiply':
    print(int(s[0])*int(s[2]))
elif s[1]=='divide':
    print(int(s[0])//int(s[2]))
'''
'''
def calc(a, op, b):
    c = {
        "plus": a + b,
        "minus": a - b,
        "multiply": a * b,
        "divide": a // b
    }
    return c[op]

s = input().split()
print(calc(int(s[0]), s[1], int(s[2])))
'''
'''
def modify_list(l):
    for i in range(len(l)-1,-1,-1):
        if int(l[i]) % 2 == 0:
            l[i] = int(l[i]) // 2
        else:
            del(l[i])
'''

'''
import pandas as pd
import scipy.stats as stats﻿
URL = 'https://stepik.org/media/attachments/lesson/8083/genetherapy.csv'﻿
﻿data = pd.read_csv(URL)﻿
A = data[data["Therapy"] == "A"]["expr"]
B = data[data["Therapy"] == "B"]["expr"]
C = data[data["Therapy"] == "C"]["expr"]
D = data[data["Therapy"] == "D"]["expr"]
﻿stats.f_oneway(A, B, C, D)
'''
'''
p=input()
a=0
d={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
i=0
while i<len(p):
    if ((i+1)<len(p))and(p[i]+p[i+1]) in d:
        a+=int(d[p[i]+p[i+1]])
        i+=2
    else:
        a+=int(d[p[i]])
        i+=1
print(a)
'''
'''
p=input().split()
l=input()
d={'6':6,'7':7,'8':8,'9':9,'1':10,'J':11,'Q':12,'K':13,'A':14}
f,s=p[0],p[1]
if f[0]=='1':
    f=str(1)+f[2]
if s[0]=='1':
    s=str(1)+s[2]
if f[1]==s[1]:
    if int(d[f[0]])>int(d[s[0]]):
        print('First')
    elif int(d[f[0]])==int(d[s[0]]):
        print('Error')
    else:
        print('Second')
elif f[1]==l:
    print('First')
elif s[1]==l:
    print('Second')
else:
    print('Error')
'''
