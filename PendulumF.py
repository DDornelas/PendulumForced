import matplotlib.pyplot as plt
import math
import numpy as np

class Pendulo:	
	def __init__(self, massa, l, theta, w):
		self.m=massa
		self.l=l
		self.theta=theta
		self.w=w
		self.w0=math.sqrt(g/l)
		self.T=2*np.pi*math.sqrt(l/g)
		self.k=massa*self.w0**2
		self.e=0.5*massa*((w*l)**2)+massa*g*(l-l*math.cos(theta))
		
	def accel(self, v, tt):
		a=(-(self.w0**2))*math.sin(self.theta)-gama*v+A*math.sin(wf*tt)
		return a
		
	def move(self, tt):
		at=self.accel(self.w, tt)
		self.theta=self.theta+self.w*dt+0.5*at*dt**2
		atmp=self.accel(self.w, tt)
		vtmp=self.w+0.5*(at+atmp)*dt
		atmp=self.accel(vtmp, tt)
		self.w=self.w+0.5*(at+atmp)*dt
		self.e=0.5*self.m*((self.w*self.l)**2)+self.m*g*(self.l-self.l*math.cos(self.theta))
		
g=9.8
gama=0.5
A=0.01
wf=2/3.0
dt=0.01
t1=0

p1=Pendulo(1, 10, np.pi/6, 0)
p2=Pendulo(1, 10, 0.4, 0)

tmax=20*p1.T
t=np.arange(0, tmax, dt)
thet1=np.zeros(t.size)
omega1=np.zeros(t.size)
energy1=np.zeros(t.size)
thet2=np.zeros(t.size)
omega2=np.zeros(t.size)
energy2=np.zeros(t.size)
dif=np.zeros(t.size)

print p1.theta

for i in range(t.size):
	p1.move(t[i])
	p2.move(t[i])
	p1.theta=(p1.theta+np.pi)%(2*np.pi)-np.pi
	p2.theta=(p2.theta+np.pi)%(2*np.pi)-np.pi
	thet1[i], omega1[i], energy1[i]=p1.theta, p1.w, p1.e
	thet2[i], omega2[i], energy2[i]=p2.theta, p2.w, p2.e
	dif[i]=(thet1[i]-thet2[i])**2

print p1.theta

plt.figure(figsize=(16,5), dpi=96)
plt.axis([0,140,-0.001,0.016])

ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'Tempo(s)')
plt.ylabel(r'Posi\c{c}\~{a}o($rad^{2}$)')

plt.title(r'Pendulum For\c{c}ado Diferen\c{c}a da Posi\c{c}\~{a}o Entre P\^{e}ndulos', fontsize=12)
plt.grid()
plt.plot(t, dif, 'r-', label="A=0,01")
plt.savefig("QD001.pdf", dpi=96)
plt.show()
