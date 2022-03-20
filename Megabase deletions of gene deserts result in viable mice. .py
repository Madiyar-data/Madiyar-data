import math
import time
import matplotlib.pyplot as plt
import numpy as np



s=8
sy=1.9
x=[1.5,0.75,0.75,1.25,2,2.5,2.75,3.25,3.25,3.5,4,4.5,5.5,6.25,7,8,8.25,s,7.5,6,5,3,4.5,6,7.5,7.75,7.5,7,6,4,4,4.75,4.5,3.5,3,2.5,2,1.75,2.25,2.5,2.5,2,1.5]
y=[5.5,5.75,6.25,6.25,6.5,6.5,6.65,6.75,6.25,6, 5.59,5.75,5.75, 5.5, 4.5,3.5,2.5,sy,1.5,1,1.1,0.75,1.5,1.45,2,2.25,2.75,3,2.5,2.25,2.5,2.58,3,3,3.25,2.75,2.75,3,3,3.5,4,5,5.5]

x1=[3,3.32]
y1=[3.25,4.25]

x2=[2.5,2.92,2.9]
y2=[6.5,7,6.65]

x3=[4.5,4.5,4.75,5.5,5.75]
y3=[3,3.5,4.7,4.82,4.5]
    
a=[0,1]
n=0
f=10
while n<f:
    a.append(a[len(a)-2]+a[len(a)-1])
    n=n+1

plt.style.use('dark_background')

plt.axes([0.55,0.4,0.42,0.52])

plt.bar(range(3,f+5),a, color='lime')



    
plt.xlabel('Поколение')
plt.ylabel('Количество')
plt.title('Возрастание числености')



plt.axes([0.05,0.4,0.39,0.52])
plt.plot(x,y,"--", color='lime')
plt.plot(x1,y1,"--", color='lime')
plt.plot(x2,y2,"--", color='lime')
plt.plot(x3,y3,"--", color='lime')
plt.plot(2,6,".", color='lime')

plt.xlabel('Ширина')
plt.ylabel('Рост')
#plt.ylim(0, 10)
plt.title('Параметры существа')
#plt.title('Cуществует точка зрения, что большая часть генома человека не функциональна. В 2004 году журнал Nature опубликовал статью, описывавшую мышей,',loc='right')
#plt.title('из генома которых были вырезаны значительные фрагменты некодирующей ДНК размером в 1,5 миллиона и 0,8 миллионов нуклеотидов.')
#plt.title('Было показано, что эти мыши не отличаются от обычных строением тела, развитием, продолжительностью жизни или способностью оставлять потомство ')
plt.legend(loc='upper left')


aa=[]
aa2=[]
d=20
for i in np.arange(0.0,d, 0.6):
    aa.append(math.cos(i))
for i in np.arange(0.0,d, 0.6):
    aa2.append(-math.cos(i))

q=[]
s=[]

plt.axes([0.05,.055,0.92,0.18])

plt.plot(np.arange(0.0,d, 0.6),aa, color='blue')

plt.plot(np.arange(0.0,d, 0.6),aa2, color='blue')
h=0

for i in aa:
    h=h+1
    if h%2==0:
        q=q+[i,-i]
    else:
        q=q+[-i,i]
for i in np.arange(0.0,d, 0.6):
    s=s+[i,i]

plt.plot(s,q,"--",color='blue')
#gen1=input('Введите последовательность нуклеотидов: ')
gen1=''
gen=gen1.split(' ')
if gen1=='' or gen1==' ':
    gen=['AT','GC','TA','CG','AT','GC','TA','CG','AT','GC','TA','CG','AT','GC'
    ,'TA','CG','CG','AT','GC','TA','CG','CG','AT','GC','TA','CG','CG','AT','GC','TA'
    ,'CG','AT','GC','TA']
    gen1=' '.join(gen)
n=-0.6
fn=0
plt.plot(0,1,"o", color='lime',label='Аденин')
plt.plot(0,1,"o", color='r',label='Тимин')
plt.plot(0,1,"o", color='white',label='Гуанин')
plt.plot(0,1,"o", color='yellow',label='Цитозин')
for i in gen:
    
    if i=='AT':
        plt.plot(n+0.6,aa[fn],"o", color='lime')
        plt.plot(n+0.6,aa2[fn],"o", color='r')
        n=n+0.6
        fn=fn+1
    elif i=='TA':
        plt.plot(n+0.6,aa[fn],"o", color='r')
        plt.plot(n+0.6,aa2[fn],"o", color='lime')
        n=n+0.6
        fn=fn+1
    elif i=='CG':
        plt.plot(n+0.6,aa[fn],"o", color='yellow')
        plt.plot(n+0.6,aa2[fn],"o", color='white')
        n=n+0.6
        fn=fn+1
    elif i=='GC':
        plt.plot(n+0.6,aa[fn],"o", color='white')
        plt.plot(n+0.6,aa2[fn],"o", color='yellow')
        n=n+0.6
        fn=fn+1
plt.title('Последовательность нуклеотидов в ДНК: '+gen1)
plt.legend(loc='upper right')


plt.show()
time.sleep(222)
