import time
import matplotlib.pyplot as plt
n=0
x1=[]
roga=[]
razmer=[]
skor=[]
chust=[]
graf=[]
print("Эра |   Генетика траваядного животного   |  Генетика хищного животного ")
print("----------------------------------------------------------------------")
kogti=[]
razmer_h=[]
skor_h=[]
chust_h=[]
z=[[2,0],[3,2],[0,1],[4,1]]
zh=[[1,4],[3,0],[2,1],[3,1]]
while n<=500:
    x=zh[0][0]
    y=zh[0][1]
    q1=x/(x**2+2*y**2+1)
    x=zh[1][0]
    y=zh[1][1]
    q2=x/(x**2+2*y**2+1)
    x=zh[2][0]
    y=zh[2][1]
    q3=x/(x**2+2*y**2+1)
    x=zh[3][0]
    y=zh[3][1]
    q4=x/(x**2+2*y**2+1)
    ww=[q1,q2,q3,q4]
    w=sorted([q1,q2,q3,q4])

    w1=max(w)
    for i in ww:
        if w1==i:
            e=ww.index(i)
    w.remove(w1)
    a=[z[e][0],z[e][1]]

    w1=max(w)
    for i in ww:
        if w1==i:
            e=ww.index(i)
    w.remove(w1)
    b=[z[e][0],z[e][1]]

    w1=max(w)
    for i in ww:
        if w1==i:
            e=ww.index(i)
    w.remove(w1)
    c=[z[e][0],z[e][1]]
    if n%2==0:
        zh=[[b[0],a[1]],[c[0],a[1]+1],[a[0],b[1]],[a[0],c[1]]]
    else:
        zh=[[b[0]-1,a[1]],[c[0],a[1]],[a[0],b[1]],[a[0],c[1]]]

    if zh[0][0]<=z[0][0] and zh[0][0]<30:
        zh[0][0]=z[0][0]+1
        zh[1][1]=zh[1][1]-2
    else:
        zh[0][1]=z[0][1]+1
    if zh[1][1]<=z[1][1] and zh[1][1]<30:
        zh[1][1]=z[1][1]+1
        zh[0][0]=zh[0][0]-2
    if  zh[1][1]>50:
        zh[1][1]=z[1][1]-1
    if  zh[1][0]>50:
        zh[1][0]=z[1][0]-3
    if n>30:
        zh[1][0]=zh[1][0]+1
    if n>100:
        zh[1][0]=zh[1][0]-1
    if n>150:
        zh[1][0]=zh[1][0]-2
        
    x=z[0][0]
    y=z[0][1]
    q1=x/(x**2+2*y**2+1)
    x=z[1][0]
    y=z[1][1]
    q2=x/(x**2+2*y**2+1)
    x=z[2][0]
    y=z[2][1]
    q3=x/(x**2+2*y**2+1)
    x=z[3][0]
    y=z[3][1]
    q4=x/(x**2+2*y**2+1)
    ww=[q1,q2,q3,q4]
    w=sorted([q1,q2,q3,q4])

    w1=max(w)
    for i in ww:
        if w1==i:
            e=ww.index(i)
    w.remove(w1)
    a=[z[e][0],z[e][1]]

    w1=max(w)
    for i in ww:
        if w1==i:
            e=ww.index(i)
    w.remove(w1)
    b=[z[e][0],z[e][1]]

    w1=max(w)
    for i in ww:
        if w1==i:
            e=ww.index(i)
    w.remove(w1)
    c=[z[e][0],z[e][1]]
    if n%2==0:
        z=[[b[0],a[1]],[c[0]+1,a[1]],[a[0],b[1]],[a[0],c[1]]]
    else:
        z=[[b[0],a[1]],[c[0],a[1]],[a[0]-1,b[1]],[a[0],c[1]]]

    if zh[0][0]>=z[0][0] and z[0][0]<30 :
        z[0][0]=zh[0][0]+1
        z[1][1]=z[1][1]-2
    else:
        z[0][1]=zh[0][1]+1
    if zh[1][1]>=z[1][1] and z[1][1]<30:
        z[1][1]=zh[1][1]+1
        z[0][0]=z[0][0]-2
    if  z[1][1]>50:
        z[1][1]=z[1][1]-1
    if  z[1][0]>50:
        z[1][0]=zh[1][0]-3
    if n>30:
        z[1][0]=z[1][0]+1
    if n>100:
        z[1][0]=z[1][0]-1
    if n>150:
        z[1][0]=z[1][0]-2
        
    n=n+1
    graf.append(n)
    print(n,"  | ", z, " | ",zh)
    a1=[]
    for ii in z:
        a1.append(sum(ii))
    roga.append(a1[0])
    razmer.append(a1[1])
    skor.append(a1[2])
    chust.append(a1[3])

    a2=[]
    for ii2 in zh:
        a2.append(sum(ii2))
    kogti.append(a2[0])
    razmer_h.append(a2[1])
    skor_h.append(a2[2])
    chust_h.append(a2[3])

plt.style.use('seaborn')

plt.axes([0.05,.055,0.42,0.38])
plt.plot(graf,kogti, color='r',label='Хищное животное')
plt.plot(graf,roga, color='blue',label='Траваядное животное')
plt.xlabel('Эра')
plt.ylabel('Уровень развития')
plt.title('Рога/когти')
plt.legend(loc='lower center')


plt.axes([0.55,.055,0.42,0.38])
plt.plot(graf,razmer_h,'o', color='r',label='Хищное животное')
plt.plot(graf,razmer,'o',color='blue',label='Траваядное животное')
plt.xlabel('Эра')
plt.ylabel('Уровень развития')
plt.title('Размер')
plt.legend(loc='lower center')


plt.axes([0.05,.57,0.42,0.38])
plt.plot(graf,skor_h,'--', color='r',label='Хищное животное')
plt.plot(graf,skor,'--', color='blue',label='Траваядное животное')
plt.xlabel('Эра')
plt.ylabel('Уровень развития')
plt.title('Скорость')
plt.legend(loc='lower center')


plt.axes([0.55,.57,0.42,0.38])
plt.plot(graf,chust_h,'.', color='r',label='Хищное животное')
plt.plot(graf,chust,'.', color='blue',label='Траваядное животное')
plt.xlabel('Эра')
plt.ylabel('Уровень развития')
plt.title('Органы чуств')
plt.legend(loc='lower center')
plt.show()
time.sleep(222)
