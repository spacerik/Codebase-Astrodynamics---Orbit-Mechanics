# Code inspired by this post on https://stackoverflow.com/questions/29060824/is-there-a-way-to-define-a-float-array-in-python
import numpy as np
import matplotlib.pyplot as plt
import math

m1 = 1.988e30 # (kg) mass of central body (mass of the sun is 1.988e30 kg, mass of Earth is 5.972E24 kg)
G = 6.67e-11 # (Nm^2kg^-2) gravitational constant
r1 = 696340.0E3 # Radius of the sun is 696340.0 km, radius of the Earth is 6371.0 km (only used for plotting)

dt = 3600 # (s) length of timestep (3600 seconds in 1 hour)
N = 24*365 # number of timesteps (24*365 is amount of hours in 1 year)
x = np.zeros(N+1)
y = np.zeros(N+1)
x[0] = 1.496e11 # (m) initial condition of object position on x-axis (1.496e11 is averagedistance Earth-Sun) 
y[0] = 0.0 # (m) initial condition of object position on y-axis
vx = np.zeros(N+1)
vy = np.zeros(N+1)
vx[0] = 0.0 # (m/s) initial condition of object velocity in x-axis direction
vy[0] = 29780.0 # (m/s) initial condition of object velocity in y-axis direction (Earth velocity around Sun is 29780.0 m/s)
ax = np.zeros(N+1)
ay = np.zeros(N+1)

def a(x,y):
    r=math.sqrt(x**2+y**2) # Distance from the central body to the object
    return (-G*m1)/r**2 # Acceleration of a body under a gravity force from a mass m1

for i in range (0,N):
    if x[i] == 0:
        ax[i]=0 # To prevent an impossible operations in the calculation of ax[i]
    else:    
        ax[i] = a(x[i],y[i])/math.sqrt(1+(y[i]**2/x[i]**2))*(x[i]/abs(x[i])) # Calculation of the accelleration ax[i]. Note that the sign/direction of ax[i] is arranged with the factor: (x[i]/abs(x[i]))
    if y[i] == 0:
        ay[i]=0 # To prevent an impossible operation in the calculation of ay[i]
    else:
        ay[i] = a(x[i],y[i])/math.sqrt(1+(x[i]**2/y[i]**2))*(y[i]/abs(y[i])) # Calculation of the accelleration ay[i]. Note that the sign/direction of ay[i] is arranged with the factor: (y[i]/abs(y[i]))
    vx[i+1] = vx[i] + ax[i]*dt # calculation of the velocity as a result of the initial velocity and the acceleration
    vy[i+1] = vy[i] + ay[i]*dt # calculation of the velocity as a result of the initial velocity and the acceleration
    x[i+1] = x[i] + vx[i]*dt # calculation of the position as a result of the initial position and the velocity
    y[i+1] = y[i] + vy[i]*dt # calculation of the position as a result of the initial position and the velocity   

plotlabel='Object position'
fig=plt.figure()    
ax=fig.add_subplot(111)
ax.set_aspect('equal')
fig.suptitle('Orbit propagation of object')
plt.scatter(x,y,label=plotlabel)
plt.legend(loc='upper left',fontsize='small')
plt.xlabel('X axis (m)')
plt.ylabel('Y axis (m)')
circle=plt.Circle((0,0),radius=r1, color='yellow') # Yellow is used for the colour of the Sun
ax.add_patch(circle)
plt.show()

#plt.savefig('test.png')