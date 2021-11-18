# author: Leonardo Loreti
# date: 18/11/2021

from numpy import sqrt, sin, cos

'''Note: the reference frames are in standard position'''

# Light speed
c = 299792458

# Lorentz factor
def gamma(v): 
    return 1/sqrt(1-(v*v)/(c*c))

# Relativistic velocity addition
def velocityAddition(u, v):

    uPrime = []
    uPrime.append( (u[0]-v)/(1-(v*u[0])/(c*c)) )
    uPrime.append( u[1]/(gamma(v)*(1-(v*u[0])/(c*c))) )
    uPrime.append( u[2]/(gamma(v)*(1-(v*u[0])/(c*c))) )

    return uPrime

# four vector position
t = 0
x = 0
y = 0
z = 0
s = [c*t, x, y, z]

# We don't need to store the time component for the others
# reference frames
sPrime = [x, y, z]
sNewton = [x, y, z]

# relative velocity between frames
v = 0.65*c

# Passage of time in S inertial frame of reference
dt = 0.0001

# tri-vector velocity in S
ux = sin(t)
uy = cos(t)
uz = 1
u = [ux, uy, uz]

f = open("S_Positions.txt", "a")
g = open("SPrime_Positions.txt", "a")
h = open("SNewton_Positions.txt", "a")

# Every inertial frame was at the same point in t=0
f.write(str(x) + " " + str(y) + " " + str(z) + "\n")
g.write(str(x) + " " + str(y) + " " + str(z) + "\n")
h.write(str(x) + " " + str(y) + " " + str(z) + "\n")

while t<6:
    # Passage of time in S
    t = t + dt

    # Evolution of velocity in S
    ux = sin(t)
    uy = cos(t)
    u = [ux, uy, uz]

    xPrevious = s[1]

    # New position in S reference frame
    s = [s[0], s[1] + ux*dt, s[2] + uy*dt, s[3] + uz*dt]

    xNext = s[1]

    # New position in S' reference frame by Newton's Mechanics
    sNewton = [sNewton[0]+(ux-v)*dt, sNewton[1]+uy*dt, sNewton[2]+uz*dt]

    h.write(str(sNewton[0]) + " " + str(sNewton[1]) + " " + str(sNewton[2]) + "\n")

    # Passage of time in S' reference frame
    dtPrime = gamma(v)*(dt-(v*(xNext-xPrevious))/(c*c))

    # Velocity of the particle at new time t, seen from S' 
    uPrime = velocityAddition(u, v)

    # New position in S' reference frame
    sPrime = [sPrime[0]+uPrime[0]*dtPrime, sPrime[1]+uPrime[1]*dtPrime, sPrime[2]+uPrime[2]*dtPrime]

    f.write(str(s[1]) + " " + str(s[2]) + " " + str(s[3]) + "\n")
    g.write(str(sPrime[0]) + " " + str(sPrime[1]) + " " + str(sPrime[2]) + "\n")
    h.write(str(sNewton[0]) + " " + str(sNewton[1]) + " " + str(sNewton[2]) + "\n")

f.close()
g.close()
h.close()