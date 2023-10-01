import numpy as np
from scipy import constants, integrate
#import yt
#import matplotlib
#matplotlib.use('GTK3cairo')
import matplotlib.pyplot as plt


#use id=7




def star_mass(dir,num, start,end,a):
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_00'+num+'/sink_00'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    #age=-(age-age[0])/1e3
    for i in range(start,end+1):
        if id[i] == a:
            return mass[i]
        else:
            pass
    
def star_age(dir,num, start,end,a):
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_00'+num+'/sink_00'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    #age=-(age-age[0])/1e3
    for i in range(start,end+1):
        if id[i] == a:
            return age[i]
        else:
            pass

# def mass(a):
#     for i in range(0,6):
#         if id[i] == a:
#             return mass[i]
#         else:
#             pass

dir = 'm3.50jw'
a = 7
masses = []
ages = []
for n in range(10,71+1):
    try:
        masses.append(star_mass(dir,'0'+str(n),0,173,a))
        ages.append(star_age(dir,'0'+str(n),0,173,a))
    except:
        pass

ages= (ages-ages[0])/1e3
#is this time since formation??

#print(masses)
#print(ages)
#f"M={totmass:.0f} M$_\odot$ \n t={age[0]:.0f} kyr"
plt.plot(ages,masses,label=f"Id={a:.0f}")
plt.legend()
plt.xlabel('time since formation [kyr]')
plt.ylabel('Mass (Msol)')
plt.title(dir+': Growth of Stars Over Time')
#plt.yscale('log')
plt.savefig('Star_m3.50jw_try1.png')




