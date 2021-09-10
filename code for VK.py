import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df2=pd.read_csv('C:/Users/Мадияр/Desktop/dataset_vk.csv')
df2
df2.shape
list(df2)    # 2221

df=df2   # 2222

r=[]
d=[]
j=[]
dd=[]
jj=[]
for i in df['posts']:
    aa=str(i).split(' ')
    if 'наук' in aa:
        r.append(i)
    elif ('бог' or 'Бог') in aa:
        d.append(i)
    elif ('президент' or 'политика' or 'правительство') in aa:
        j.append(i)
    elif ('нож' or 'пистолет' or 'оружие') in aa:
        dd.append(i)
   
print(len(r), "человек упоминули слово 'наука' в своих постах" )
print(len(d), "человек упоминули слово 'бог' в своих постах")
print(len(j), "человек упоминули про политику в своих постах")
print(len(dd), "человек упоминули про холодное оружие в своих постах")
print(len(df['posts']))


df=df.query("bdate!='not specified'")  # 2223

df=df2
mas=[]
for i in df['bdate']:# 2224
    mas.append(len(i))
df['E']=mas
df

df=df.query("E>5 & bdate!='not specified'") # 2225

df # 2226
das=[]
mas=[]  # 222
for i in df['bdate']:
    u=list(i)
    mas.append(u[len(u)-4]+u[len(u)-3]+u[len(u)-2]+u[len(u)-1])   # 2227
df['date_of_Birth']=mas
df=df.drop(['E'],axis=1)
for data_r in df['date_of_Birth']:
    das.append(int(data_r))


chi=[]
kol=[]
a=list(range(min(das)-1,max(das)+1))

for ii in a:
    kol.append(das.count(ii))
    chi.append(ii)
    
plt.axes([0.05,.055,0.32,0.38])
plt.bar(chi,kol,color='lime')
plt.xlabel('Дата рождение')
plt.ylabel('Количество')
plt.title('Количество людей по дате рождения')


df_pol = df.groupby('political').aggregate({'date_of_Birth':'count'})

asi=[]
for iti in df_pol['date_of_Birth']:
    asi.append(iti)
asr=['political','communist','conservative','indifferent','liberal','libertarian','moderate','monarchist','socialist','ultraconservative']        
print(df_pol)

plt.axes([0.43,.055,0.58,0.38])

plt.bar('communist',asi[0],alpha=0.9,color='r')
plt.bar('conservative',asi[1],alpha=0.8,color='blue')
plt.bar('indifferent',asi[2],alpha=0.7,color='green')
plt.bar('liberal',asi[3],alpha=0.5,color='cyan')
plt.bar('libertarian',asi[4],alpha=0.5,color='dodgerblue')
plt.bar('moderate',asi[5],alpha=0.5,color='m')
plt.bar('monarchist',asi[6],alpha=0.5,color='orange')
plt.bar('socialist',asi[7],alpha=0.5,color='lime')


plt.xlabel('Отношение политике')
plt.ylabel('Количество')
plt.title('Политика')

plt.axes([0.05,.57,0.92,0.38])
plt.bar("Упоминули слово 'наука' в своих постах",len(r),alpha=0.7,color='green')
plt.bar("Упоминули слово 'бог' в своих постах",len(d),alpha=0.8,color='yellow')
plt.bar("Упоминули про политику в своих постах",len(j),alpha=0.7,color='blue')
plt.bar("Упоминули про холодное оружие в своих постах",len(dd),color='r')
plt.ylabel('Количество')
plt.title("Анализ пользователей в приложении 'Вконтакте'")
plt.show()


