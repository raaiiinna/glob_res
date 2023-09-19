import numpy as np
from scipy import constants, integrate
#import matplotlib
#matplotlib.use('GTK3cairo')
import matplotlib.pyplot as plt
#import yt

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

#ds = yt.load("./m2.00jw/output_00015/info_00015.txt",fields=cell_fields, extra_particle_fields=epf)

#s = yt.ProjectionPlot(ds, "y", ("ramses", "Temperature"))
#s = yt.ProjectionPlot(ds, "y", ("gas", "temperature"), weight_field=("gas", "density"),
#    buff_size=(800, 800))
#s.annotate_particles(width=(5, 'pc'))
#s.save('test.png')

def kroupa(x,mtot=1):
    lx=np.log10(x)
    a1=np.log10(0.08)
    a2=np.log10(0.5)
    y=np.where(lx<a1,-0.3*(a1-a2)+0.7*(lx-a1), -0.3*(lx-a2))
    y=np.where(lx>a2,-1.35*(lx-a2),y)
    norm=mtot/11.8019
    y=x*norm*10**y
    return y

def kroupa_plot(mtot):
    x=np.linspace(-2,2,100)
    a1=np.log10(0.08)
    a2=np.log10(0.5)
    y=np.where(x<a1,-0.3*(a1-a2)+0.7*(x-a1), -0.3*(x-a2))
    y=np.where(x>a2,-1.35*(x-a2),y)
    norm=mtot/11.8019
    ax.plot(x,norm*10**y,color='black',linestyle='--')

def plot_mf(dir,num):
    m_frac=0.5
    kyr=3.15e10
    unit_time=0.470442691211163E+15/kyr
    #file=dir+'/output_00'+num+'/sink_000'+num+'.info'
    file='/home/rhatcher/scratch/Analysis/Data/'+'m'+dir+'jw'+'/output_00'+num+'/sink_00'+num+'.info'
    # mass in Msun, age in yr
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=age/1e3
    totmass=mass.sum()
    lmass=np.log10(mass)
    #plt.hist(lmass,bins=20, range=(-3.5,2.5),histtype='step', label=dir+f"M={totmass:f} Msun")
    Num_bins=40
    h,bine = np.histogram(lmass,bins=Num_bins, range=(-2.0,2.5))
    binc=(bine[1:]+bine[:-1])/2.0+np.log(m_frac)
    #+np.log10(0.4)
    #print(binc,h)
    #ax.plot(binc,h)
    ax.step(binc,h,where='mid',label=f"M={totmass:.0f} M$_\odot$ \n t={age[0]:.0f} kyr",color=clr)
    ax.legend()
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.set_xlim(-2.0,1.5)
    ax.set_ylim(1,100)
    #ax.set_ylim(0,3)
    ax.set_xlabel('log Mass [M$_\odot$]')
    ax.set_ylabel('N(per log bin)')
    #mtot=totmass*m_frac
    #kroupa_plot(mtot)

def plot_fs(dir,num):
    #file='m'+dir+'jw'+'/output_00'+num+'/sink_000'+num+'.info'
    file='/home/rhatcher/scratch/Analysis/Data/'+'m'+dir+'jw'+'/output_00'+num+'/sink_00'+num+'.info'
    id, mass, age = np.loadtxt(file, usecols=(0,1,8),skiprows=4, comments=' =',unpack=True)
    age=-(age-age[0])/1e3
    mass=np.cumsum(mass)
    ax1.plot(age,mass,label=f"log(Z/Z$_\odot$)=-{dir}",color=clr)
    #ax1.legend()
    #ax1.title.set_text('log(Z/Z$_\odot$)=-4.00')
    ax1.text(50, 1e3,'log(Z/Z$_\odot$)=-4.00',fontsize='large')
    ax1.set_xlim(0,450)
    ax1.set_ylim(10,2e3)
    ax1.set_yscale('log')
    ax1.set_xlabel('time [kyr]')
    ax1.set_ylabel('Mass [M$_\odot$]')
    return mass[-1:]

fig, (ax, ax1) = plt.subplots(1,2,figsize=(14,7))

dir='4.00'
num='012'
clr='red'
plot_mf(dir,num)
#ax=axs[0][1]
plot_fs(dir,num)
#print(dir, res)

dir='4.00'
num='015'
clr='darkorange'
#ax=axs[0][1]
plot_mf(dir,num)
#ax=axs[2][1]
plot_fs(dir,num)
#print(dir, res)

dir='4.00'
num='023'
clr='gold'
#ax=axs[0][0]
plot_mf(dir,num)
#ax=axs[0][1]
plot_fs(dir,num)
#print(dir, res)

dir='4.00'
num='034'
clr='limegreen'
#ax=axs[0][0]
plot_mf(dir,num)
#ax=axs[0][1]
plot_fs(dir,num)
#print(dir, res)

dir='4.00'
num='045'
clr='dodgerblue'
#ax=axs[0][0]
plot_mf(dir,num)
#ax=axs[0][1]
plot_fs(dir,num)
#print(dir, res)

dir='4.00'
num='056'
clr='mediumpurple'
#ax=axs[0][0]
plot_mf(dir,num)
#ax=axs[0][1]
plot_fs(dir,num)
#print(dir, res)

#additions from old doc
mtot=200.0
kroupa_plot(mtot)
lmin=0.01
lmax=100.0
ans, err = integrate.quad(kroupa, lmin, lmax)
print(ans,err)




#plt.show()
plt.savefig('mf_m4.00jw_try2.png')

