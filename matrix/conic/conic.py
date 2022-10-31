
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
from sympy import *

import sys                                          #for path to external scripts

sys.path.insert(0,'/sdcard/Ajay/matrix/CoordGeo')         #path to my scripts



#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from conics.funcs import *


#if using termux
import subprocess
import shlex
#end if
#for line
#n=np.array(([2,-1])) #normal vector
#n1=np.array(([-15,5]))
n2=np.array(([-2,1]))
n3=np.array(([12,36]))
#c=-9
#c1=13
c2=3
c3=227
e1=np.array(([1,0]))
#x1 = c/(n@e1) #X-intercept
#A1 =  x1*e1
#x2 = c1/(n1@e1) #X-intercept
#A2 =  x2*e1
x3 = c2/(n2@e1) #X-intercept
A3 =  x3*e1
x4 = c3/(n3@e1) #X-intercept
A4 =  x4*e1
#Direction vector
#m1=omat@n
#m2=omat@n1
m3=omat@n2
m4=omat@n3
#Generating all lines
k1 = -10
k2 = 8
#AB = line_dir_pt(m1,A1,k1,k2)
#CD = line_dir_pt(m2,A2,k1,k2)
EF = line_dir_pt(m3,A3,k1,k2)
GH = line_dir_pt(m4,A4,k1,k2)

#for parabola
V = np.array([[1,0],[0,0]])
u = np.array(([-1,-0.5]))
f = 7

def affine_transform(P,c,x):
    return P@x + c

#Transformation 
lamda,P = LA.eigh(V)
if(lamda[1] == 0):  # If eigen value negative, present at start of lamda 
    lamda = np.flip(lamda)
    P = np.flip(P,axis=1)
    
eta = u@P[:,0]
a = np.vstack((u.T + eta*P[:,0].T, V))
b = np.hstack((-f, eta*P[:,0]-u)) 
center = LA.lstsq(a,b,rcond=None)[0]
O = center 
n = np.sqrt(lamda[1])*P[:,0]
c = 0.5*(LA.norm(u)**2 - lamda[1]*f)/(u.T@n)
F = np.array(([0,0.5]))
fl = LA.norm(F)

#pmeters to generate parabola
num_points = 1700
delta = 50*np.abs(fl)/10
p_y = np.linspace(-2*np.abs(fl)-delta,2*np.abs(fl)+delta,num_points)
a = -2*eta/lamda[1]   # y^2 = ax => y'Dy = (-2eta)e1'y


p_x = parab_gen(p_y,a)
p_std = np.vstack((p_x,p_y)).T

##Affine transformation
p = np.array([affine_transform(P,center,p_std[i,:]) for i in range(0,num_points)]).T
plt.plot(p[0,:], p[1,:])

#Computation
x = Symbol('x')
# m is the vector perpendicular to normal chord ie m^tx = c
m2 = Matrix([-x, 1])
omat = Matrix(([0, -1], [1, 0]))
print('omat:',omat)
# n is the vector along the normal chord ie h + kn = x 
n2 = omat*m2
# Conic parameters
V2 = Matrix(([1,0],[0,0]))
print('v:',V)
u2 = Matrix([0, -2])
f2 = Matrix([0])
# Point from which normal drawn
h2 = Matrix([1,2])
# Equation solving
eq1 = n2.T*((V2*h2 + u2)*(V2*h2 + u2).T - (h2.T*V2*h2 + 2*u2.T*h2 + f2)[0,0]*V2)*n2
eq2 = (m2.T*V2*n2)**2
eq3 = ((V2*h2 + u2).T*(n2*(m2.T*V2*n2) - m2*(n2.T*V2*n2)))**2
eq = eq1[0,0]*eq2[0,0] - eq3[0,0]
print(expand(eq))
print(solveset(eq, x))

#Plotting all lines
#plt.plot(AB[0,:],AB[1,:],label='$line1$')
#plt.plot(CD[0,:],CD[1,:],label='$line1$')
plt.plot(EF[0,:],EF[1,:],label='$36y+12x-227=0$')
plt.plot(GH[0,:],GH[1,:],label='$y-2x-3=0$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')
plt.legend(loc='best')
plt.annotate("q1",(2,7))
plt.scatter(2,7, color='black')
plt.annotate("q2",(-5/6,217/36))
plt.scatter(-5/6,217/36, color='yellow')

plt.xlim(-5,5)
plt.ylim(0,18)

#if using termux
#plt.savefig(os.path.join(script_dir, fig_relative))
#subprocess.run(shlex.split("termux-open "+os.path.join(script_dir, fig_relative)))
#else
#plt.show()

plt.savefig('/sdcard/Ajay/matrix/conic/conicfig.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Ajay/matrix/conic/conicfig.pdf"))

