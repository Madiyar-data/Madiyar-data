import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b=-2
l=0.1
def ne(x):
    f1=F(nei(x,w1))
    f2=F(nei(x,w2))
    f3=F(nei([f1,f2],w3))
    return f3


def F(x):
    return 1/(1+math.exp(-x))

def F_(x):
    return (x*(1-x))

def Q(y,d,f1x):
    e=y-d
    return e*f1x

def w(w1,l,q,f):
    return w1-l*q*f

#e=y-d
w1=[0.15242,
        -0.2142,
        0.72452]

w2=[-0.642,
        0.2342,
            -0.2545]

w3=[-0.2242,
        0.914242]

x=[[1,1,b,1],
   [0,0,b,0],
    [1,1,b,1],
   [1,1,b,1],
   [0,1,b,0],
    [1,0,b,1],
    [0,0,b,0],]


def nei(x,w):
    return np.dot(x,w)+b
nn=0

print(ne([0,0,0]))
print(ne([1,1,1]))
print(ne([1,0,0]))
print(ne([0,1,0]))
print('w1=',w1)
print('w2=',w2)
print('w3=',w3)
print("")
def neiro(x,x1):
    f1=F(nei(x,w1))
    f2=F(nei(x,w2))
    f3=F(nei([f1,f2],w3))
    
    q11=Q(f3,x1,F_(f3))
    w3[0]=w3[0]-l*q11*f1
    w3[1]=w3[1]-l*q11*f2

    q22=Q(f2,x1,F_(f2))
    w2[0]=w2[0]-l*q22*x[0]
    w2[1]=w2[1]-l*q22*x[1]
    w2[2]=w2[2]-l*q22*x[2]

    q21=Q(f1,x1,F_(f1))
    w1[0]=w1[0]-l*q21*x[0]
    w1[1]=w1[1]-l*q21*x[1]
    w1[2]=w1[2]-l*q21*x[2]


    return f3
#print(f3)
Qy=[]
Qy1=[]
Qx=[]
Qy2=[]
Qy3=[]
while nn<5000:
    Qx.append(nn)
    nn=nn+1
    for i in x:
        x1=[i[0],i[1],i[2]]
        x2=i[3]
        neiro(x1,x2)
    #x=random.sample(x,len(x))
    Qy.append((ne([1,1,b])))
    Qy1.append((ne([0,0,b])))
    Qy2.append((ne([0,1,b])))
    Qy3.append((ne([1,0,b])))
print(ne([0,0,0]))
print(ne([1,1,1]))
print(ne([0,0,1]))
print(ne([0,1,1]))
print('w1=',w1)
print('w2=',w2)
print('w3=',w3)







#ph=[419.66,461.62,507.7,558.5,614.42,675.8,743.45]
#ye=[2021,2022,2023,2024,2025,2026,2027]

plt.axes([0.05,.05,0.425,0.9])
plt.plot(Qx,Qy, color='blue',label='11')
plt.plot(Qx,Qy1, color='r',label='00')
plt.plot(Qx,Qy2, color='g',label='01')
plt.plot(Qx,Qy3, color='yellow',label='10')
plt.xlabel('эпоха')
plt.ylabel('Вывод')
plt.title('neiron')
plt.legend(loc='lower center')
plt.show()
