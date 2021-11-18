import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy import loadtxt

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')

S = loadtxt('S_Positions.txt', float)

x = S[:,0]
y = S[:,1]
z = S[:,2]

ax.plot3D(x, y, z, 'green')

ax = fig.add_subplot(1, 2, 2, projection='3d')

SNewton = loadtxt('SNewton_Positions.txt', float)
SPrimePositions = loadtxt('SPrime_Positions.txt', float)

xNewton = SNewton[:,0]
yNewton = SNewton[:,1]
zNewton = SNewton[:,2]

xPrime = SPrimePositions[:,0]
yPrime = SPrimePositions[:,1]
zPrime = SPrimePositions[:,2]

ax.plot3D(xNewton, yNewton, zNewton, 'blue')
ax.plot3D(xPrime, yPrime, zPrime, 'red')

plt.show()
