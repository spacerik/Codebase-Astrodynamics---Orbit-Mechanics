# Code based on this post on https://stackoverflow.com/questions/29060824/is-there-a-way-to-define-a-float-array-in-python
import numpy as np
import matplotlib.pyplot as plt
import math

dt = 3600 # (s) length of timestep (3600 seconds in 1 hour)
N = 24*365 # number of timesteps (24*365 is amount of hours in 1 year)
x = np.zeros(N+1)
y = np.zeros(N+1)
x[0] = 1.496e11 # (m) initial condition of object position on x-axis (1.496e11 is averagedistance Earth-Sun) 
y[0] = 0.0 # (m) initial condition of object position on y-axis
vx = np.zeros(N+1)
vy = np.zeros(N+1)
vx[0] = 0.0 # (m/s) initial condition of object velocity in x-axis direction
vy[0] = 29000 # (m/s) initial condition of object velocity in y-axis direction
ax = np.zeros(N+1)
ay = np.zeros(N+1)
m1 = 1.988e30 # (kg) mass of central body (mass of the sun is 1.988e30 kg)
G = 6.67e-11 # (Nm^2kg^-2) gravitational constant

def a(x,y):
    r=math.sqrt(x**2+y**2)
    return (-G*m1)/r**2 # Acceleration of a body under a gravity force from a mass m1

for i in range (0,N):
    r = x[i],y[i]
    if x[i] == 0:
        ax[i]=0
    else:    
        if x[i] < 0:
            ax[i] = a(x[i],y[i])/math.sqrt(1+(y[i]**2/x[i]**2))*-1.0
        else:
            ax[i] = a(x[i],y[i])/math.sqrt(1+(y[i]**2/x[i]**2))
    if y[i] == 0:
        ay[i]=0
    else:
        if y[i] < 0:
            ay[i] = a(x[i],y[i])/math.sqrt(1+(x[i]**2/y[i]**2))*-1.0
        else:
            ay[i] = a(x[i],y[i])/math.sqrt(1+(x[i]**2/y[i]**2))
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    x[i+1] = x[i] + vx[i]*dt 
    y[i+1] = y[i] + vy[i]*dt    
plt.plot(x,y)
plt.show()