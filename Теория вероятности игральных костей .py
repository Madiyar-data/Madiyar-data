import matplotlib.pyplot as plt
a=[1,2,3,4,5,6]
n=0
s=[]
s1=[]
s3=[]
s4=[]
for q in range(0,50):
    n=0
    for i1 in a:
        for i2 in a:
            for i3 in a:
                for i4 in a:
                    for i5 in a:
                        for i6 in a:
                            for i7 in a:
                                for i8 in a:
                                    if i2+i1+i3+i4+i5+i6+i7+i8==q:
                                        n=n+1
    s.append(n)
#print(s)
#print(list(range(0,18)))


for q in range(0,30):
    n=0
    for i1 in a:
        for i2 in a:
            if i2+i1==q:
                n=n+1
    s1.append(n)

for q in range(0,30):
    n=0
    for i1 in a:
        for i2 in a:
            for i3 in a:
                if i2+i1+i3==q:
                    n=n+1
    s3.append(n)

for q in range(0,30):
    n=0
    for i1 in a:
        for i2 in a:
            for i3 in a:
                for i4 in a:
                    if i2+i1+i3+i4==q:
                        n=n+1
    s4.append(n)

plt.style.use('dark_background')
plt.axes([0.55,.57,0.42,0.38])
#plt.plot(data,fact4,"--", color='blue',label='Фактический результат')
plt.bar(range(0,50),s, color='darkviolet')#,label='Ожидаемый результат')
plt.xlabel('Общее число при выпадении')
plt.ylabel('Кол-во вариантов выпадения')
plt.title('При 8 игральных кубиках')
#plt.legend(loc='upper left')


plt.axes([0.05,.57,0.42,0.38])
plt.bar(range(0,30),s4,color='red',label='При 4 игральных кубиках')
plt.bar(range(0,30),s3,color='blue',label='При 3 игральных кубиках')
plt.bar(range(0,30),s1,color='lime',label='При 2 игральных кубиках')

#plt.plot(range(0,20),s1,'.', color='lime',label='Ожидаемый результат')
plt.xlabel('Общее число при выпадении')
plt.ylabel('Кол-во вариантов выпадения')
plt.title('При 2, 3 и 4 игральных кубиках')
#plt.legend(loc='upper left')
plt.legend(loc='upper right')



plt.axes([0.05,.055,0.42,0.38])
plt.bar(range(0,30),s3,color='blue')
plt.xlabel('Общее число при выпадении')
plt.ylabel('Кол-во вариантов выпадения')
plt.title('При 3 игральных кубиках')


plt.axes([0.55,.055,0.42,0.38])
plt.bar(range(0,30),s1,color='lime')
plt.xlabel('Общее число при выпадении')
plt.ylabel('Кол-во вариантов выпадения')
plt.title('При 2 игральных кубиках')




plt.show()
