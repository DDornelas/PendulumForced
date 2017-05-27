import matplotlib.pyplot as plt
import math
import numpy as np

class Pendulo:	
	def __init__(self, massa, l, theta, w):
		self.m=massa
		self.l=l
		self.angulo=theta
		self.w=w
		self.w0=math.sqrt(g/l)
		self.T=2*np.pi*math.sqrt(l/g)
		self.e=0.5*massa*((w*l)**2)+massa*g*(l-l*math.cos(theta))
		
	def accel(self, v, t):
		a=(-(self.w0**2))*math.sin(self.angulo)-gama*v+A*math.sin(wf*t)
		return a
		
	def move(self, t):
		at=self.accel(self.w, t)
		self.angulo=self.angulo+self.w*dt+0.5*at*dt**2
		atmp=self.accel(self.w, t)
		vtmp=self.w+0.5*(at+atmp)*dt
		atmp=self.accel(vtmp, t)
		self.w=self.w+0.5*(at+atmp)*dt
		self.e=0.5*self.m*self.w*self.l+self.m*g*(self.l-self.l*math.cos(self.angulo))
		
g=9.8
gama=0.5
A=0
wf=0
dt=0.01
t1=0

p1=Pendulo(1, 10, np.pi/6, 0)

tmax=20*p1.T
t=np.arange(0, tmax, dt)
thet=np.zeros(t.size)
omega=np.zeros(t.size)
energy=np.zeros(t.size)

for i in range(t.size):
	p1.move(t[i])
	p1.angulo=(p1.angulo+np.pi)%(2*np.pi)-np.pi
	thet[i], omega[i], energy[i]=p1.angulo, p1.w, p1.e

plt.figure(figsize=(16,5), dpi=96)
plt.axis([0,130,-4,14])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'Tempo(s)')
plt.ylabel(r'Energia(J)')

plt.title(r'Pendulum For\c{c}ado Energia', fontsize=12)
plt.grid()
plt.plot(t,energy,'r-', linewidth=1, label="$\gamma=0.5$")
plt.legend(loc='upper right')
plt.savefig("ET05.pdf", dpi=96)
plt.show()
