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

def plot_mf(dir,num):
    kyr=3.15e10
    unit_time=0.470442691211163E+15/kyr
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_000'+num+'/sink_000'+num+'.info'
    # mass in Msun, age in yr
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=age/1e3
    totmass=mass.sum()
    lmass=np.log10(mass)
    #plt.hist(lmass,bins=20, range=(-3.5,2.5),histtype='step', label=dir+f"M={totmass:f} Msun")
    Num_bins=15
    h,bine = np.histogram(lmass,bins=Num_bins, range=(-3.0,2.0))
    binc=(bine[1:]+bine[:-1])/2.0+np.log10(0.4)
    ax.plot(binc,h,label=f"M={totmass:.0f} Msun t={age[0]:.0f} kyr",color=clr)

def plot_fs(dir,num):
    file='/home/rhatcher/scratch/Analysis/Data/'+dir+'/output_000'+num+'/sink_000'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=-(age-age[0])/1e3
    mass=np.cumsum(mass)
    ax1.plot(age,mass,label=num,color=clr)

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
dir='m3.50jw'
num='11'
clr='red'
plot_mf(dir,num)
plot_fs(dir,num)

#note: 15 not equally spaced with the others!
dir='m3.50jw'
num='15'
clr='darkorange'
plot_mf(dir,num)
plot_fs(dir,num)



dir='m3.50jw'
num='20'
clr='gold'
plot_mf(dir,num)
plot_fs(dir,num)

dir='m3.50jw'
num='25'
clr='limegreen'
plot_mf(dir,num)
plot_fs(dir,num)

dir='m3.50jw'
num='47'
clr='dodgerblue'
plot_mf(dir,num)
plot_fs(dir,num)

dir='m3.50jw'
num='71'
clr='mediumpurple'
plot_mf(dir,num)
plot_fs(dir,num)

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
ax.set_xlim(-2,2.0)
ax.set_ylim(1,500)
ax.set_xlabel('log Mass [M$_\odot$]')
ax.set_ylabel('N(per log bin)')


ax1.legend()
ax1.set_xlim(0,400)
ax1.set_ylim(10,1e3)
ax1.set_yscale('log')
ax1.set_xlabel('time [kyr]')
ax1.set_ylabel('Mass')
fig.suptitle('m3.50jw')
plt.savefig('mf_m3.50jw_try2.png')

