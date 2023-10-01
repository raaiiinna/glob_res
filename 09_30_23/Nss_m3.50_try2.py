import numpy as np
from scipy import constants, integrate
#import yt
#import matplotlib
#matplotlib.use('GTK3cairo')
import matplotlib.pyplot as plt







def mn(dir,num,a):
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_00'+num+'/sink_00'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=-(age-age[0])/1e3
    mass=np.sum(mass)
    n = len(id)
    l = 1
    if a == l:
        return mass/n
    else: 
        return age[-1]




dir = 'm2.00jw'

MN = []
ages = []

for i in range(10,99+1):
    try:
        MN.append(mn(dir,'0'+str(i),1))
        ages.append(mn(dir,'0'+str(i),0))
    except:
        pass

for i in range(100,104+1):
    try:
        MN.append(mn(dir,str(i),1))
        ages.append(mn(dir,str(i),0))
    except:
        pass


#print(MN)
#print(ages)

plt.plot(ages,MN,label=dir,color='red')





dir = 'm2.67jw'

MN = []
ages = []

for i in range(11,99+1):
    MN.append(mn(dir,'0'+str(i),1))
    ages.append(mn(dir,'0'+str(i),0))

for i in range(100,142+1):
    MN.append(mn(dir,str(i),1))
    ages.append(mn(dir,str(i),0))
#print(MN)
#print(ages)

plt.plot(ages,MN,label=dir,color='gold')

 
dir = 'm3.00jw'

MN = []
ages = []

for i in range(10,99+1):
    MN.append(mn(dir,'0'+str(i),1))
    ages.append(mn(dir,'0'+str(i),0))

for i in range(100,121+1):
    MN.append(mn(dir,str(i),1))
    ages.append(mn(dir,str(i),0))
#print(MN)
#print(ages)

plt.plot(ages,MN,label=dir,color='limegreen')



dir = 'm3.50jw'

MN = []
ages = []

for i in range(11,71+1):
    MN.append(mn(dir,'0'+str(i),1))
    ages.append(mn(dir,'0'+str(i),0))

#print(MN)
#print(ages)



plt.plot(ages,MN,label=dir,color='dodgerblue')

dir = 'm4.00jw'

MN = []
ages = []

for i in range(12,56+1):
    MN.append(mn(dir,'0'+str(i),1))
    ages.append(mn(dir,'0'+str(i),0))

#print(MN)
#print(ages)

plt.plot(ages,MN,label=dir,color='mediumpurple')




plt.legend()
plt.xlabel('time [kyr]')
plt.ylabel('M/N')
plt.title('Ratio of Total Mass to Number of Stars Over Time')
plt.yscale('log')
plt.savefig('Nss_m3.50jw_try2.png')


