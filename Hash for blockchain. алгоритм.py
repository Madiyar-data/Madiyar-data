import binascii
# Создаю блок S0 по внутренней функции F0 
def S0(x):
    xxx=[]
    s0=[]
    xx=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    s=['9','0','4','b','d','c','3','f','1','a','2','6','7','5','8','e']
    tt=list(x)
    if len(tt)==1:
        for it in xx:
            if x==it:
                Q=s[xx.index(it)]
    else:
        for i in xx:
            xxx.append(bin(int(i, 16)))
        for i in s:
            s0.append(bin(int(i, 16)))
        for i in xxx:
            if i==x:
                Q=list(s0[xxx.index(i)])
                for uy in Q:
                    if uy=='b':
                        Q[Q.index(uy)]='0'
                Q=''.join(Q)
    return Q


# Создаю блок S1 по внутренней функции F0 
def S1(x):
    xxx=[]
    s1=[]
    xx=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in xx:
    
        xxx.append(bin(int(i, 16)))
        
    s=[3,12,6,13,5,7,1,9,15,2,0,4,11,10,14,8]
    for i in s:
        s1.append(bin(i))
    for i in xxx:
        if i==x:
            Q=list(s1[xxx.index(i)])
            for uy in Q:
                if uy=='b':
                    Q[Q.index(uy)]='0'
            Q=''.join(Q)
    return Q

# Линейное преобразование L
# Создаю блок c линейным преобразованием L по внутренней функции F0 
def L(x0, x1, x2, x3, y0, y1, y2, y3):
    L=[x0+(y1+x2),x1+(y2+x3+x0),x2+(y3+x0)+(y0+x1), x3+(y0+x1),y0+x1,y1+x2,y2+x3+x0,y3+x0]
    return L


# Перестановка P
# Создаю блок c перестановкой P по внутренней функции F0
def P(x):
    # перестановка 512 элементов,  композиция трех перестановок 512 элементов P = p0 ◦ p1 ◦ p2
    # p0 – перестановка 512 элементов
    for i in range(0,255):
        x[i]=x[i]
    for i in range(128,255):
        x[2*i+0]=x[2*i+1]
    for i in range(128,255):
        x[2*i+1]=x[2*i+0]

    # p1 – перестановка 512 элементов
    for i in range(0,255):
        x[i]=x[2*i]
    for i in range(0,255):
        x[i+256]=x[2*i+1]

    # p2 – перестановка 512 элементов
    for i in range(0,127):
        x[4*i+0] = x[4*i+0]
    for i in range(0,127):
        x[4*i+1] = x[4*i+1]
    for i in range(0,127):
        x[4*i+2] = x[4*i+3]
    for i in range(0,127):
        x[4*i+3] = x[4*i+2]
    return x

# Перестановка P0
# Создаю блок c перестановкой P0 по внутренней функции F0
# P0 – перестановка 128 элементов, аналогичная перестановке P,
# является композицией трех перестановок 128 элементов P0 = p'0 ◦ p'1 ◦ p'2.
def P0(x):
    # p'0 – перестановка 128 элементов
    for i in range(0,63):
        x[i]=x[i]
    for i in range(32,63):
        x[2*i+0]=x[2*i+1]
    for i in range(32,63):
        x[2*i+1]=x[2*i+0]

    #p'1 – перестановка 128 элементов
    for i in range(0,63):
        x[i]=x[2*i]
    for i in range(0,63):
        x[i+64]=x[2*i+1]

    #p'2 – перестановка 128 элементов
    for i in range(0,31):
        x[4*i+0]=x[4*i+0]
    for i in range(0,31):
        x[4*i+1]=x[4*i+1]
    for i in range(0,31):
        x[4*i+2]=x[4*i+3]
    for i in range(0,31):
        x[4*i+3]=x[4*i+2]
    return x


# Раундовое преобразование R
# Создаю блок c раундовым преобразованием R по внутренней функции F0

# Раундовое преобразование R(A, C) определяется на основе
# определенных выше S-блоков S0 и S1, линейного преобразования L и перестановки P 
def R(A,C):
    n=-1
    while n<511:
        n=n+1
        if C[0]=='0':
            A[n]=S0('0b'+str(int(A[n])))
            C.pop(0)
        elif C[0]=='1':
            C.pop(0)
            A[n]=S1('0b'+str(int(A[n])))

    for i in range(0,255):
        a11=list(A[2*i])
        a12=list(A[2*i+1])
        fo=[a11[len(a11)-4],a11[len(a11)-3],a11[len(a11)-2],a11[len(a11)-1], a12[len(a12)-4],a12[len(a12)-3],a12[len(a12)-2],a12[len(a12)-1]]
        l=L(int(fo[0]),int(fo[1]),int(fo[2]),int(fo[3]),int(fo[4]),int(fo[5]),int(fo[6]),int(fo[7]))
        for iu in l:
            if iu%2==0:
                l[l.index(iu)]=0
            elif iu%2!=0 and iu!=0:
                l[l.index(iu)]=1
    
        A[2*i]=str(l[0])+str(l[1])+str(l[2])+str(l[3])
        A[2*i+1]=str(l[4])+str(l[5])+str(l[6])+str(l[7])
    return(P(A))

# Раундовое преобразование R0
# Создаю блок c раундовым преобразованием R0 по внутренней функции F0
def R0(A):
    for i in A:
        n=A.index(i)
        A[n]=S0('0b'+str(int(A[n])))


    for i in range(0,63):
        a11=list(A[2*i])
        a12=list(A[2*i+1])
        fo=[a11[len(a11)-4],a11[len(a11)-3],a11[len(a11)-2],a11[len(a11)-1], a12[len(a12)-4],a12[len(a12)-3],a12[len(a12)-2],a12[len(a12)-1]]
        l=L(int(fo[0]),int(fo[1]),int(fo[2]),int(fo[3]),int(fo[4]),int(fo[5]),int(fo[6]),int(fo[7]))
        for iu in l:
            if iu%2==0:
                l[l.index(iu)]=0
            elif iu%2!=0 and iu!=0:
                l[l.index(iu)]=1
    
        A[2*i]=str(l[0])+str(l[1])+str(l[2])+str(l[3])
        A[2*i+1]=str(l[4])+str(l[5])+str(l[6])+str(l[7])
        
    A=P0(A)
    return A

# Создаю криптографический алгоритм с  применением выше указаных блоков
def str2hex(s):
    return binascii.hexlify(bytes(str.encode(s)))
def hex2str(h):
    return binascii.unhexlify(h)
print("Байтемиров Мадияр ИС-22")
print("Криптографический алгоритм с  применением блоков по внутренней функции F0")
print("\nXеш для блокчейна :")
t=1; nomer=1
while t==1:
    e=[]; x=[]; y=[];pp=[]
    rus=list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя")
    rind=list(range(192,256))
    print("--------------------------------------------------------------------------")
    print("")
    a1=input(str(nomer)+")Введите текст : ")
    a=list(a1)
    nomer=nomer+1
    for i in a:
        if i in rus:
            indexr=rus.index(i)        
            h=list(hex(rind[indexr]))
            h.pop(0)
            h.pop(0)
            e.append(''.join(h))
        else:
            hexstring = str2hex(i)
            e.append(hexstring.decode('utf-8'))
            unhexsring = hex2str(hexstring).decode('utf-8')    
    r=list(e[len(e)-1])
    r1=r[0]
    r2=r[1]
    for_p=256-len(a)
    n=0
    while n<for_p:   
        qq=0
        while qq<=n:
            r1=S0(r1)
            r2=S0(r2)
            qq=qq+1
        e.append(r1+r2)
        n=n+1
    Aee=[]
    Aeee=[]
    Cee=[]
    Ceee=[]
    for i in e:
        rt=list(bin(int(i,16)))
        for yi in rt:
            if yi=='b':
                asa=rt.index(yi)
                rt[asa]='0'
        Aee.append(rt[len(rt)-8]+rt[len(rt)-7]+rt[len(rt)-6]+rt[len(rt)-5])
        Aeee.append(rt[len(rt)-4]+rt[len(rt)-3]+rt[len(rt)-2]+rt[len(rt)-1])
        Cee.append(rt[len(rt)-8])
        Ceee.append(rt[len(rt)-4])
    A1=Aee+Aeee
    C1=Cee+Ceee
    Q=R(A1,C1)
    A1=R0(Q[0:128])
    A2=R0(Q[128:256])
    A3=R0(Q[256:384])
    A4=R0(Q[384:512])
    A=A1+A2+A3+A4
    n=0
    while n<=48:
        C=Cee+Ceee
        A=R(A,C)
        n=n+1
    w=[]
    for i in range(0,512,2):
        d=A[i]+A[i+1]
        w.append(d)
    for i in w:
        q=list(i)
        if len(q)!=8:
            w[w.index(i)]='01010101'
    hexx=[]
    for i in w:
        h=list(hex(int(i,2)))
        h.pop(0)
        h.pop(0)
        h=''.join(h)
        hexx.append(h)
    print("")
    for i in hexx:
        if len(list(i))==1:
            hexx[hexx.index(i)]='0'+i
    hexx=list(''.join(hexx))
    heh=[]
    for i in range(0,512,7):
        heh.append(hexx[i])
    HESH=''.join(heh[0:64])
    print("Хеш: ",HESH)
    print("Длина хеша: ",len(list(HESH))*4,"бит ")
    print("")
    print("")







