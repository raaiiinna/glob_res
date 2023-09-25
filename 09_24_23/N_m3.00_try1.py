import numpy as np
from scipy import constants, integrate
#import yt
#import matplotlib
#matplotlib.use('GTK3cairo')
import matplotlib.pyplot as plt
#import yt
'''
cell_fields = [
    "Density",
    "x-velocity",
    "y-velocity",
    "z-velocity",
    "Pressure",
    "metallicity",
    "H2-fraction",
    "HII-fraction",
    "HeII-fraction",
    "HeIII-fraction"]
epf = [("p1", "double"), ("p2", "double"),("p3", "double"),("p4", "double")]
'''
#ds = yt.load("./m2.00jw/output_00015/info_00015.txt",fields=cell_fields, extra_particle_fields=epf)

#s = yt.ProjectionPlot(ds, "y", ("ramses", "Temperature"))
#s = yt.ProjectionPlot(ds, "y", ("gas", "temperature"), weight_field=("gas", "density"),
#    buff_size=(800, 800))
#s.annotate_particles(width=(5, 'pc'))
#s.save('test.png')



#/home/rhatcher/scratch/Analysis/Data/m2.00jw


def kroupa(x,mtot=1):
    x=np.log10(x)
    a1=np.log10(0.08)
    a2=np.log10(0.5)
    y=np.where(x<a1,-0.3*(a1-a2)+0.7*(x-a1), -0.3*(x-a2))
    y=np.where(x>a2,-1.35*(x-a2),y)
    norm=mtot/3.1578
    y=norm*10**y/x
    return y

def kroupa_plot(mtot):
    x=np.linspace(-2,2,100)
    a1=np.log10(0.08)
    a2=np.log10(0.5)
    y=np.where(x<a1,-0.3*(a1-a2)+0.7*(x-a1), -0.3*(x-a2))
    y=np.where(x>a2,-1.35*(x-a2),y)
    norm=mtot/3.1578
    ax.plot(x,norm*10**y,color='black',linestyle='--')

def plot_N(dir,num):
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_00'+num+'/sink_00'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=-(age-age[0])/1e3
    nn = np.linspace(1,len(mass),len(mass))
    #print(nn)
    #mass=np.cumsum(mass)
    ax.plot(age,nn,label=num,color=clr)

def plot_fsN(dir,num):
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_00'+num+'/sink_00'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=-(age-age[0])/1e3
    mass=np.cumsum(mass)
    nn = np.linspace(1,len(id),len(id))
    ax1.plot(age,mass/nn,label=num,color=clr)

fig, (ax, ax1) = plt.subplots(1,2,figsize=(14,7))
'''
dir='m2.00jw'
num='67'
#plot_mf(dir,num)
plot_fs(dir,num)

dir='m2.67jw'
num='80'
#plot_mf(dir,num)
plot_fs(dir,num)

#dir='m2.67mr'
#num='46'
#plot_mf(dir,num)

#dir='/home/ricotti/SHELL/scratch-zt/m1.00jw'
#num='31'
#plot_mf(dir,num)

dir='m3.00jw'
num='55'
#plot_mf(dir,num)
plot_fs(dir,num)

dir='m3.50jw'
num='37'
#plot_mf(dir,num)
plot_fs(dir,num)
'''
'''
dir='m4.00jw'
num='10'
#plot_mf(dir,num)
plot_fs(dir,num)

dir='m4.00jw'
num='12'
#plot_mf(dir,num)
plot_fs(dir,num)

dir='m4.00jw'
num='12'
#plot_mf(dir,num)
plot_fs(dir,num)

dir='m4.00jw'
num='15'
#plot_mf(dir,num)
plot_fs(dir,num)
'''
dir='m3.00jw'
num='010'
clr='red'
plot_N(dir,num)
plot_fsN(dir,num)

#note: 15 not equally spaced with the others!
dir='m3.00jw'
num='015'
clr='darkorange'
plot_N(dir,num)
plot_fsN(dir,num)



dir='m3.00jw'
num='030'
clr='gold'
plot_N(dir,num)
plot_fsN(dir,num)

dir='m3.00jw'
num='060'
clr='limegreen'
plot_N(dir,num)
plot_fsN(dir,num)

dir='m3.00jw'
num='100'
clr='dodgerblue'
plot_N(dir,num)
plot_fsN(dir,num)

dir='m3.00jw'
num='121'
clr='mediumpurple'
plot_N(dir,num)
plot_fsN(dir,num)

#dir='m4.00jw'
#num='56'
#plot_mf(dir,num)
#plot_fs(dir,num)












#dir='Low-res/m3.00'
#num='11'
#plot_fs(dir,num)

#dir='Hi-res/m3.67'
#num='20'
#plot_fs(dir,num)

#dir='Hi-res/m3.67'
#num='20'
#plot_mf(dir,num)

#x=np.array([-1.,1.])
#y=10**(1.0-1.35*x)
#plt.plot(x,y,'-')
'''
mtot=200.0
kroupa_plot(mtot)
lmin=0.01
lmax=100.0
ans, err = integrate.quad(kroupa, lmin, lmax)
print(ans,err)
'''
ax.legend()
ax.set_xscale('linear')
ax.set_yscale('log')
ax.set_xlim(0,400)
ax.set_ylim(1,1e3)
ax.set_xlabel('time [kyr]')
ax.set_ylabel('N')


ax1.legend()
ax1.set_xlim(0,400)
ax1.set_ylim(1,1e3)
ax1.set_yscale('log')
ax1.set_xlabel('time [kyr]')
ax1.set_ylabel('<M> (Mass/N)')
fig.suptitle('m3.00jw')
plt.savefig('N_m3.00jw_try1.png')
