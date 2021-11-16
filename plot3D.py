import matplotlib.pylab as plt

from mpl_toolkits import mplot3d
from numpy import loadtxt
'''from mpl_toolkits.mplot3d import Axes3D'''
fig = plt.figure()
ax = plt.axes(projection="3d")
'''
SPositions = loadtxt('S_Positions.txt', float)

x = SPositions[:,0]
y = SPositions[:,1]
z = SPositions[:,2]

ax.plot3D(x, y, z, 'gray')

plt.show()
'''
SPrimePositions = loadtxt('SPrimeNewton_Positions.txt', float)

xPrime = SPrimePositions[:,0]
yPrime = SPrimePositions[:,1]
zPrime = SPrimePositions[:,2]

ax.plot3D(xPrime, yPrime, zPrime, 'blue')

plt.show()
